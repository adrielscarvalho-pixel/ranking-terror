"""Monta o ranking de terror a partir dos dados coletados (IMDb, Rotten Tomatoes,
Metacritic, JustWatch BR) e gera ranking.json, README.md e index.html."""
import json, sys, os, html
sys.path.insert(0, os.path.dirname(__file__))
from notes import NOTES

S, OUT = sys.argv[1], sys.argv[2]
D = f'{S}/data'
cand = {x['id']: x for x in json.load(open(f'{D}/horror_candidates.json'))}
rt = json.load(open(f'{D}/rt.json'))
mc = json.load(open(f'{D}/mc.json'))
jw = json.load(open(f'{D}/jwbr.json'))
tiers = json.load(open(f'{D}/tiers.json'))
tmdb = json.load(open(f'{D}/tmdb.json'))
# EMBED_POSTERS=1 embute os pôsteres como data: URI (para ambientes que bloqueiam imagens externas)
EMBED = os.environ.get('EMBED_POSTERS') == '1'

def poster_src(path, size='w342'):
    if not path:
        return None
    if not EMBED:
        return f'https://image.tmdb.org/t/p/{size}{path}'
    import base64, subprocess
    cache = f'{D}/posters/w185{path}'
    if not os.path.exists(cache):
        os.makedirs(os.path.dirname(cache), exist_ok=True)
        subprocess.run(['curl', '-s', '-o', cache, f'https://image.tmdb.org/t/p/w185{path}'], check=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(open(cache, 'rb').read()).decode()

SNAPSHOT = '26–28/out/2026'
IMDB_DATA = '27/10/2026'
N_UNIVERSO = len(cand)
N_RT = len(rt)

# Curadoria de gênero: marcados como Horror no IMDb, mas o RT não marca Horror
# e a premissa central não é de terror.
EXCLUIDOS_GENERO = {
    'tt1751634': 'fantasia sombria; o RT classifica como Drama/Fantasia',
    'tt22207786': 'thriller de tribunal/serial killer; o RT classifica como Suspense/Crime/Drama',
    'tt31314754': 'drama de true crime; o RT classifica como Crime/Drama',
    'tt1179933': 'thriller de confinamento; o RT classifica como Suspense',
    'tt8633478': 'thriller psicológico; o RT classifica como Suspense',
    'tt4093826': 'mistério surreal de David Lynch; o RT classifica como Drama/Crime/Suspense',
    'tt7721046': 'comédia; o RT classifica só como Comédia',
    'tt7908628': 'sitcom de humor com tema de vampiros: mais comédia do que terror',
    'tt5580540': 'sitcom de humor com tema de mortos-vivos: mais comédia do que terror',
}
# Mantidos apesar de o RT não marcar Horror: a premissa central é de terror.
MANTIDOS_NOTA = {
    'tt11041332': 'O RT classifica como Drama/Suspense, mas há canibalismo, sobrevivência e uma entidade sobrenatural no centro: mantida.',
    'tt13623632': 'O RT classifica como Drama/Ficção científica, mas é o xenomorfo de Alien, cânone do sci-fi horror: mantida.',
    'tt7984734': 'O RT classifica como Suspense/Drama, mas é terror psicológico e folclórico de Robert Eggers: mantido.',
    'tt2798920': 'O RT classifica como Ficção científica/Aventura, mas o centro é terror cósmico e de mutação: mantido.',
    'tt8550800': 'O RT classifica como Crime/Drama, mas a entidade sobrenatural de Stephen King está no centro: mantida.',
    'tt8068860': 'O RT classifica como Drama/Suspense, mas é terror psicológico com ocultismo: mantida.',
    'tt6905686': 'O RT classifica só como Drama, mas os monstros de Lovecraft estão no centro: mantida.',
}
# Obra oficialmente limitada que o IMDb cataloga como tvSeries.
TIPO_OVERRIDE = {'tt11540908': 'mini'}

def bayes(x, n, prior, k):
    return (n * x + k * prior) / (n + k)

PESOS = {'tm': 0.30, 'mc': 0.25, 'imdb': 0.30, 'pop': 0.15}

def score(r, kind):
    c = (rt[r['id']].get('critics') or {})
    a = (rt[r['id']].get('audience') or {})
    T, n = int(c['score']), c.get('reviewCount') or 0
    comp = {'tm': bayes(T, n, 70, 20)}
    m = mc.get(r['id'])
    if m and m[1] >= 10:
        comp['mc'] = bayes(m[0], m[1], 60, 10)
    film = kind == 'film'
    comp['imdb'] = 10 * bayes(r['imdb'], r['votes'], 5.9 if film else 7.0, 10000 if film else 5000)
    if a.get('score'):
        comp['pop'] = float(a['score'])
    wsum = sum(PESOS[k] for k in comp)
    return round(sum(PESOS[k] * v for k, v in comp.items()) / wsum, 1), {k: round(v, 1) for k, v in comp.items()}

def clean_offers(o, ano):
    if not o:
        return {'assinatura': [], 'outros': 'Sem oferta legal encontrada no Brasil'}
    import re
    CANAL = re.compile(r'\s+(Amazon|Apple TV)\s+channel$', re.I)
    def base(name):
        name = CANAL.sub('', name)
        for suf in (' Standard with Ads', ' with Ads', ' Player', ' Channel'):
            name = name.replace(suf, '')
        return {'Amazon Prime Video': 'Prime Video', 'Disney Plus': 'Disney+', 'Paramount Plus': 'Paramount+',
                'Paramount Plus Premium': 'Paramount+', 'Paramount+': 'Paramount+', 'MGM Plus': 'MGM+'}.get(name, name)
    gratis = {base(p) for p in o.get('FREE', []) + o.get('ADS', [])}
    direct, channel = [], {}
    for p in o.get('FLATRATE', []) + o.get('FREE', []) + o.get('ADS', []):
        b = base(p)
        m = CANAL.search(p)
        if m:
            label = f'{b} (canal no Prime Video)' if m.group(1).lower() == 'amazon' else f'{b} (canal na Apple TV)'
            if m.group(1).lower() == 'amazon' or b not in channel:
                channel[b] = label
        elif b not in direct:
            direct.append(b)
    subs = [f'{b} (grátis)' if b in gratis else b for b in direct] + [v for b, v in channel.items() if b not in direct]
    outros = []
    # JustWatch às vezes lista sessões especiais de filmes antigos; só mostra cinema para lançamentos recentes
    if o.get('CINEMA') and ano >= 2025:
        outros.append('em cartaz nos cinemas')
    rb = sorted({base(p).replace('Amazon Video', 'Amazon').replace('Apple TV Store', 'Apple TV') for p in o.get('RENT', []) + o.get('BUY', [])})
    if rb:
        outros.append('aluguel/compra: ' + ', '.join(rb))
    return {'assinatura': subs, 'outros': '; '.join(outros)}

def where(r):
    j = jw.get(r['id']) or {}
    return j.get('pt_title'), clean_offers(j.get('offers'), r['year']), j.get('path')

items = []
for r in tiers:
    if r['id'] in EXCLUIDOS_GENERO:
        continue
    kind = TIPO_OVERRIDE.get(r['id'], r['kind'])
    idx, comp = score(r, 'film' if kind == 'film' else 'tv')
    c = rt[r['id']]['critics']; a = rt[r['id']].get('audience') or {}
    pt, offers, path = where(r)
    m = mc.get(r['id'])
    items.append(dict(
        id=r['id'], categoria={'film': 'filme', 'series': 'série', 'mini': 'minissérie'}[kind], tier=r['tier'],
        titulo=r['title'], titulo_br=pt, ano=r['year'], diretor=NOTES[r['id']][0], nota=NOTES[r['id']][1],
        imdb=r['imdb'], imdb_votos=r['votes'], tomatometer=int(c['score']), rt_criticas=c.get('reviewCount'),
        rt_media=c.get('averageRating'), popcornmeter=int(a['score']) if a.get('score') else None,
        metascore=m[0] if m else None, mc_criticas=m[1] if m else None,
        indice=idx, componentes=comp, onde_assistir=offers,
        obs=MANTIDOS_NOTA.get(r['id']),
        poster=poster_src((tmdb.get(r['id']) or {}).get('poster')),
        links=dict(imdb=f"https://www.imdb.com/title/{r['id']}/", rt=rt[r['id']]['url'],
                   tmdb=f"https://www.themoviedb.org/{tmdb[r['id']]['tipo']}/{tmdb[r['id']]['tmdb_id']}" if r['id'] in tmdb else None,
                   justwatch=f'https://www.justwatch.com{path}' if path else None)))

def ranked(cat):
    xs = [x for x in items if x['categoria'] == cat and x['tier'] in (1, 2)]
    xs.sort(key=lambda x: (x['tier'], -x['indice']))
    for i, x in enumerate(xs, 1):
        x['posicao'] = i
    return xs

filmes, series, minis = ranked('filme'), ranked('série'), ranked('minissérie')
radar = sorted([x for x in items if x['tier'] == 3], key=lambda x: -x['indice'])

FRONTEIRA = [
    ('The Last of Us', 'série, 2023', 'HBO Max', 'IMDb 8,4 (755 mil votos) · RT 94% (média das temporadas)', 'O IMDb não marca como Horror (Ação/Aventura/Drama). Entraria no topo das séries se a regra fosse “Horror no IMDb ou no RT”.'),
    ('All of Us Are Dead', 'série, 2022', 'Netflix', 'IMDb 7,6 (96 mil) · RT 89%', 'O IMDb não marca como Horror, e o RT fica abaixo de 90%. Zumbis num colégio coreano: é terror, mas falha nos dois critérios.'),
    ('Acompanhante Perfeita (Companion)', 'filme, 2025', 'HBO Max, Netflix', 'IMDb 6,9 (195 mil) · RT 93%', 'O IMDb classifica como Ficção científica/Suspense, sem Horror.'),
    ('Sandman', 'série, 2022', 'Netflix', 'IMDb 7,6 · RT 81%', 'Excluída na curadoria de gênero: é fantasia sombria, e o RT não a classifica como terror.'),
    ('Red Rooms', 'filme, 2023', 'Telecine (canal no Prime Video)', 'IMDb 7,1 · RT 96%', 'Excluído na curadoria de gênero: thriller psicológico de tribunal. Excelente, mas não é terror.'),
    ('Devil in Disguise: John Wayne Gacy', 'minissérie, 2025', 'Prime Video', 'IMDb 7,4 · RT 96%', 'Excluída na curadoria de gênero: drama de true crime.'),
    ('O Que Fazemos nas Sombras', 'série, 2019–2024', 'Disney+', 'IMDb 8,5 · RT 96%', 'Excluída na curadoria de gênero: é uma sitcom com vampiros. Ótima, mas o objetivo é fazer rir, não dar medo.'),
    ('Santa Clarita Diet', 'série, 2017–2019', 'Netflix', 'IMDb 7,8 · RT 89%', 'Excluída na curadoria de gênero: sitcom gore com uma morta-viva, mais comédia do que terror.'),
    ('Twin Peaks: O Retorno', 'série, 2017', 'MUBI', 'IMDb 8,5 · RT 94%', 'Excluída na curadoria de gênero: mistério surreal de David Lynch, com momentos de terror, mas sem ser uma obra de terror.'),
    ('Rua Cloverfield, 10', 'filme, 2016', 'aluguel/compra', 'IMDb 7,2 · RT 91%', 'Excluído na curadoria de gênero: thriller de confinamento; o RT não o classifica como terror.'),
    ('Fuja (Run)', 'filme, 2020', 'Netflix', 'IMDb 6,7 · RT 88%', 'Excluído na curadoria de gênero: thriller psicológico.'),
    ('Tumbbad', 'filme, 2018', '—', 'IMDb 8,2 (78 mil) · RT 87% (30 críticas)', 'Falha no Tomatometer (abaixo de 90% para o Radar e de 85% com amostra de 40 críticas para o ranking). Clássico indiano de folk horror, vale a busca.'),
]

os.makedirs(f'{OUT}/dados', exist_ok=True)
if not EMBED:
  json.dump(dict(gerado_em=SNAPSHOT, metodo=dict(pesos=PESOS), filmes=filmes, series=series, minisseries=minis,
               radar=radar), open(f'{OUT}/dados/ranking.json', 'w'), ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- README
def fmt_votes(v):
    return f'{v/1000:.0f} mil' if v >= 1000 else str(v)

def br(x):
    return str(x).replace('.', ',')

def onde(x):
    o = x['onde_assistir']
    s = ', '.join(o['assinatura'])
    if o['outros']:
        s = (s + ' · ' if s else '') + o['outros']
    return s or '—'

def row(x):
    img = f'<img src="{x["poster"]}" width="46" alt=""> ' if x.get('poster') else ''
    t = img + f"**{x['titulo_br'] or x['titulo']}**" + (f" <br><sub>{x['titulo']}</sub>" if x['titulo_br'] and x['titulo_br'] != x['titulo'] else '')
    ms = f"{x['metascore']}" if x['metascore'] is not None and (x['mc_criticas'] or 0) >= 10 else (f"{x['metascore']}*" if x['metascore'] else '—')
    pc = f"{x['popcornmeter']}%" if x['popcornmeter'] else '—'
    return f"| {x.get('posicao', '')} | {t} | {x['ano']} | **{br(x['indice'])}** | {br(x['imdb'])} ({fmt_votes(x['imdb_votos'])}) | {x['tomatometer']}% ({x['rt_criticas']}) | {ms} | {pc} | {onde(x)} |"

HDR = '| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |\n|---:|---|---:|---:|---|---|---:|---:|---|'

def section(xs, tier_names):
    out = []
    for tier, name in tier_names:
        sub = [x for x in xs if x['tier'] == tier]
        if not sub:
            continue
        out.append(f'### {name}\n\n{HDR}\n' + '\n'.join(row(x) for x in sub) + '\n')
    return '\n'.join(out)

def notes_block(xs):
    lines = []
    for x in xs:
        extra = f" _Nota de curadoria: {x['obs']}_" if x['obs'] else ''
        lines.append(f"- **{x.get('posicao', '•')}. {x['titulo_br'] or x['titulo']}** ({x['ano']}, dir./criação: {x['diretor']}): {x['nota']}{extra}")
    return '\n'.join(lines)

top = lambda xs, n: ', '.join(f"{x['titulo_br'] or x['titulo']} ({br(x['indice'])})" for x in xs[:n])

readme = f"""# 🩸 Ranking do Terror 2016–2026: filmes, séries e minisséries

> Curadoria baseada em dados, não em achismo. Coleta feita em **{SNAPSHOT}**.
> As notas mudam com o tempo; os dados brutos e os scripts estão nesta pasta para refazer tudo.

**Site:** https://adrielscarvalho-pixel.github.io/ranking-terror/ (pôsteres, filtros por streaming e busca).

## Resumo

- **Pódio dos filmes:** {top(filmes, 3)}
- **Pódio das séries:** {top(series, 3)}
- **Pódio das minisséries:** {top(minis, 3)}

---

## 1. Método

### 1.1 Universo analisado (sem escolher a dedo)
1. Usei a base **oficial e completa do IMDb** (`title.basics` + `title.ratings`, datasets.imdbws.com, atualizada em {IMDB_DATA}).
2. Filtrei **todo** título com gênero **Horror** e ano de estreia **≥ 2016**, nos tipos filme, série e minissérie: **{str(N_UNIVERSO)} obras** com ao menos 3 mil votos.
3. Para os **{N_RT}** com nota competitiva (filmes ≥ 6,4 e séries ≥ 6,8), busquei automaticamente a página no **Rotten Tomatoes** (Tomatometer, nº de críticas, média e Popcornmeter) e a disponibilidade no **JustWatch Brasil**.
4. Para os finalistas, coletei o **Metascore** direto no Metacritic.

### 1.2 Portas de entrada (corte obrigatório)

| | **Elite** (corte principal) | **Também recomendados** |
|---|---|---|
| **Filmes** | IMDb ≥ 7,0 **e** Tomatometer ≥ 90% | IMDb ≥ 6,5 **e** Tomatometer ≥ 85% |
| **Séries / minisséries** | IMDb ≥ 7,5 **e** Tomatometer ≥ 90% | IMDb ≥ 7,0 **e** Tomatometer ≥ 80% |

**Relevância mínima** (votos no IMDb, proporcional ao tempo de mercado):

| Ano de estreia | Filmes | Séries/minisséries |
|---|---:|---:|
| 2016–2024 | 50 mil | 20 mil |
| 2025 | 20 mil | 10 mil |
| 2026 | 5 mil | 5 mil |

Também exijo amostra crítica mínima: ≥ 40 críticas no RT para filmes e ≥ 20 para séries.

### 1.3 Só terror de verdade
- **Filtro 1:** gênero Horror no IMDb (requisito obrigatório).
- **Filtro 2:** checagem com a classificação de gênero do Rotten Tomatoes. Se o RT não marca Horror, decide a curadoria, sempre pela premissa central:
  - **excluídos:** Sandman (fantasia), Red Rooms (thriller de tribunal), Devil in Disguise (true crime), Twin Peaks: O Retorno (mistério surreal), Rua Cloverfield, 10 e Fuja (thrillers), além das sitcoms O Que Fazemos nas Sombras, Santa Clarita Diet e Los Espookys. Terror-comédia com sustos de verdade (Widow's Bay, Casamento Sangrento) fica;
  - **mantidos, com justificativa:** Yellowjackets, Alien: Earth, O Farol, Aniquilação, The Outsider, Servant e Lovecraft Country.

### 1.4 Índice do Medo (0–100)

`Índice = 30% Tomatometer + 25% Metascore + 30% IMDb×10 + 15% Popcornmeter`

- **Crítica pesa 55%:** o Tomatometer mede consenso; o Metascore mede intensidade.
- **Público pesa 45%:** IMDb e Popcornmeter.
- **Ajuste por confiança (média bayesiana):** obra com poucas críticas ou poucos votos é puxada para a média do gênero, para que um 100% com 8 críticas não vença um 97% com 440.
  - Tomatometer: prior de 70% com peso de 20 críticas.
  - Metascore: prior de 60 com peso de 10 críticas. Só vale com ≥ 10 críticas; senão, o peso é redistribuído.
  - IMDb, filmes: prior de 5,9 (média real dos filmes de terror da base) com peso de 10 mil votos.
  - IMDb, séries: prior de 7,0 com peso de 5 mil votos.
- **Ordenação:** quem passa no corte **Elite** fica sempre acima de quem só passa no corte de **Recomendados**. Dentro de cada faixa, vale o Índice.
- **Categoria:** segue o tipo do IMDb. Exceção: *Carrie* (2026), oficialmente uma minissérie de 8 episódios que o IMDb cataloga como série.
- **Séries com várias temporadas:** usa-se a média de todas as temporadas que o RT exibe (“Avg. Tomatometer”). O Metascore é o da página principal no Metacritic.

### 1.5 Onde assistir
Dados do **JustWatch Brasil** coletados em {SNAPSHOT}.
- “Assinatura” inclui planos com anúncios.
- “Canal no Prime Video” significa assinatura adicional dentro da Amazon.
- Catálogos mudam toda semana: confira antes de assinar.

---

## 2. 🎬 Filmes

{section(filmes, [(1, 'Elite: IMDb ≥ 7,0 e RT ≥ 90%'), (2, 'Também recomendados: IMDb ≥ 6,5 e RT ≥ 85%')])}
<sub>* Metascore com menos de 10 críticas: exibido, mas fora do cálculo.</sub>

#### Por que cada filme está aqui
{notes_block(filmes)}

---

## 3. 📺 Séries

{section(series, [(1, 'Elite: IMDb ≥ 7,5 e RT ≥ 90%'), (2, 'Também recomendadas: IMDb ≥ 7,0 e RT ≥ 80%')])}
<sub>* Metascore com menos de 10 críticas (From tem 63 com apenas 7): exibido, mas fora do cálculo.</sub>

#### Por que cada série está aqui
{notes_block(series)}

---

## 4. 🕯️ Minisséries

{section(minis, [(1, 'Elite: IMDb ≥ 7,5 e RT ≥ 90%'), (2, 'Também recomendadas: IMDb ≥ 7,0 e RT ≥ 80%')])}

#### Por que cada minissérie está aqui
{notes_block(minis)}

> Poucas minisséries de terror lançadas desde 2016 passam nos cortes; a lista curta é resultado do método, não falta de busca.

---

## 5. 📡 Radar: qualidade de elite, pouca audiência

Têm IMDb ≥ 6,8 e Tomatometer ≥ 90% (com ≥ 20 críticas), mas não atingem o volume mínimo de votos ou de críticas. Ficam fora do ranking principal e servem como garimpo.

{HDR}
{chr(10).join(row(x) for x in radar)}

{notes_block(radar)}

---

## 6. ⚖️ Zona cinzenta: fora por regra (transparência)

| Obra | Tipo | Onde ver | Números | Por que ficou fora |
|---|---|---|---|---|
{chr(10).join(f'| {a} | {b} | {c} | {d} | {e} |' for a, b, c, d, e in FRONTEIRA)}

Quase entraram nos filmes (falharam por pouco no Tomatometer ou no IMDb):
- O Telefone Negro (6,9 / 81%)
- Não! Não Olhe! (6,8 / 83%)
- Alien: Romulus (7,1 / 80%)
- Sorria (6,5 / 79%)
- A Noite Passada em Soho (7,0 / 75%)
- Cara-de-Barro (7,6 / 75%)
- Exhuma (6,9 / 93%, mas só 32 mil votos)
- Midsommar (7,1 / 83%)
- Doutor Sono (7,3 / 79%)
- Fragmentado (7,3 / 79%)
- Invocação do Mal 2 (7,3 / 80%)
- O Que Ficou Para Trás / His House (6,4 / 100%)
- Rua do Medo: 1666 e 1978 seguem no ranking; Halloween (2018) ficou fora (6,5 / 79%)

---

## 7. Fontes
- IMDb Non-Commercial Datasets: https://datasets.imdbws.com/ (snapshot de {IMDB_DATA})
- Rotten Tomatoes: páginas de cada título (links em `dados/ranking.json`)
- Metacritic: páginas de cada título; o slug foi obtido via Wikidata (propriedade P1712)
- JustWatch Brasil: API pública do site (país BR, idioma pt-BR)
- Pôsteres: [TMDB](https://www.themoviedb.org/), arte brasileira quando disponível. Este produto usa a API do TMDB, mas não é endossado nem certificado pelo TMDB.
- Fatos citados nas notas:
  - 16 indicações de *Pecadores* ao Oscar; Oscar de Amy Madigan por *A Hora do Mal*: [TheWrap](https://www.thewrap.com/industry-news/awards/oscar-nominations-records-milestones-2026/), [Variety](https://au.variety.com/2026/film/news/amy-madigan-best-supporting-actress-oscar-34250)
  - Bilheteria de *Resident Evil*: [CTV/AP](https://www.ctvnews.ca/entertainment/article/box-office-resident-evil-tops-box-office-with-franchise-best-debut-of-us60-million/)

## 8. Reproduzir
```bash
cd scripts
# 1) baixe a base do IMDb e filtre terror 2016+
mkdir -p <pasta>/data && cd <pasta>/data && curl -O https://datasets.imdbws.com/title.basics.tsv.gz -O https://datasets.imdbws.com/title.ratings.tsv.gz && cd -
python3 filter.py <pasta>
# 2) coleta RT, JustWatch e monta as faixas
python3 rt.py <pasta>; python3 tiers.py <pasta>; python3 jwbr.py <pasta>
# (Metascores: coletados página a página e salvos em <pasta>/data/mc.json)
# 3) gera ranking.json, README.md e index.html
TMDB_TOKEN=<seu token de leitura do TMDB> python3 tmdb.py <pasta>   # pôsteres
python3 build.py <pasta> ..
```
Os dados brutos usados nesta versão estão em `dados/brutos/`.
"""
if not EMBED:
    open(f'{OUT}/README.md', 'w').write(readme)

# ---------------------------------------------------------------- HTML
tpl = open(os.path.join(os.path.dirname(__file__), 'template.html')).read()
payload = json.dumps(dict(gerado_em=SNAPSHOT, filmes=filmes, series=series, minisseries=minis, radar=radar,
                          fronteira=[dict(zip(['obra', 'tipo', 'onde', 'numeros', 'motivo'], f)) for f in FRONTEIRA]),
                     ensure_ascii=False)
HEAD = '<!doctype html>\n<html lang="pt-BR">\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
open(f'{OUT}/index.html', 'w').write(HEAD + tpl.replace('/*__DATA__*/null', payload).replace('__UNIVERSO__', str(N_UNIVERSO)).replace('__NRT__', str(N_RT)))
print('filmes', len(filmes), 'series', len(series), 'minis', len(minis), 'radar', len(radar))
for name, xs in (('FILMES', filmes), ('SERIES', series), ('MINIS', minis), ('RADAR', radar)):
    print(name)
    for x in xs:
        print(' ', x.get('posicao'), x['tier'], x['titulo'], x['indice'], x['componentes'], onde(x))
