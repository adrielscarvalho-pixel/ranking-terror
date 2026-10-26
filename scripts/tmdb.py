"""Busca pôster (preferindo a arte brasileira) no TMDB para cada obra do ranking.
Uso: TMDB_TOKEN=<token v4 de leitura> python3 tmdb.py <pasta>
Salva <pasta>/data/tmdb.json (só caminhos de imagem; o token não é gravado)."""
import json, os, sys, subprocess, time
S = sys.argv[1]
TOKEN = os.environ['TMDB_TOKEN']
r = json.load(open(f'{S}/data/tiers.json'))
def get(path):
    out = subprocess.run(['curl', '-s', '--max-time', '30', '-H', f'Authorization: Bearer {TOKEN}',
                          f'https://api.themoviedb.org/3/{path}'], capture_output=True).stdout
    return json.loads(out or b'{}')
res = {}
for x in r:
    f = get(f"find/{x['id']}?external_source=imdb_id&language=pt-BR")
    hit, kind = None, None
    for k, t in (('movie_results', 'movie'), ('tv_results', 'tv')):
        if f.get(k):
            hit, kind = f[k][0], t
            break
    if not hit:
        print('SEM TMDB', x['title'], file=sys.stderr); continue
    d = get(f"{kind}/{hit['id']}?language=pt-BR")
    imgs = get(f"{kind}/{hit['id']}/images?include_image_language=pt,en,null")
    posters = imgs.get('posters') or []
    br = [p for p in posters if p.get('iso_639_1') == 'pt' and p.get('iso_3166_1') in ('BR', None)]
    poster = d.get('poster_path') or hit.get('poster_path')
    if br:
        poster = max(br, key=lambda p: (p.get('iso_3166_1') == 'BR', p.get('vote_average', 0)))['file_path']
    res[x['id']] = dict(tmdb_id=hit['id'], tipo=kind, poster=poster, backdrop=d.get('backdrop_path'),
                        sinopse=d.get('overview'))
    print(x['title'], kind, poster, 'BR' if br else '', file=sys.stderr)
    time.sleep(0.1)
json.dump(res, open(f'{S}/data/tmdb.json', 'w'), ensure_ascii=False, indent=1)
