# 🩸 Ranking do Terror 2016–2026: filmes, séries e minisséries

> Curadoria baseada em dados, não em achismo. Coleta feita em **26–28/out/2026**.
> As notas mudam com o tempo; os dados brutos e os scripts estão nesta pasta para refazer tudo.

**Site:** https://adrielscarvalho-pixel.github.io/ranking-terror/ (pôsteres, filtros por streaming e busca).

## Resumo

- **Pódio dos filmes:** Pecadores (85,6), Corra! (85,4), Resident Evil (83,2)
- **Pódio das séries:** Kingdom (85,9), O Segredo de Widow's Bay (84,3), Stranger Things (83,2)
- **Pódio das minisséries:** A Maldição da Residência Hill (83,9), The Outsider (81,0), A Queda da Casa de Usher (79,6)

---

## 1. Método

### 1.1 Universo analisado (sem escolher a dedo)
1. Usei a base **oficial e completa do IMDb** (`title.basics` + `title.ratings`, datasets.imdbws.com, atualizada em 27/10/2026).
2. Filtrei **todo** título com gênero **Horror** e ano de estreia **≥ 2016**, nos tipos filme, série e minissérie: **1474 obras** com ao menos 3 mil votos.
3. Para os **325** com nota competitiva (filmes ≥ 6,4 e séries ≥ 6,8), busquei automaticamente a página no **Rotten Tomatoes** (Tomatometer, nº de críticas, média e Popcornmeter) e a disponibilidade no **JustWatch Brasil**.
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
Dados do **JustWatch Brasil** coletados em 26–28/out/2026.
- “Assinatura” inclui planos com anúncios.
- “Canal no Prime Video” significa assinatura adicional dentro da Amazon.
- Catálogos mudam toda semana: confira antes de assinar.

---

## 2. 🎬 Filmes

### Elite: IMDb ≥ 7,0 e RT ≥ 90%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 1 | <img src="https://image.tmdb.org/t/p/w342/v0Ljeti537c6cNKweuEN0iaU3x4.jpg" width="46" alt=""> **Pecadores** <br><sub>Sinners</sub> | 2025 | **85,6** | 7,5 (537 mil) | 97% (441) | 84 | 96% | HBO Max, Netflix · aluguel/compra: Amazon, Apple TV |
| 2 | <img src="https://image.tmdb.org/t/p/w342/A0RoSZh8PEYJgDMgM2EV7Ycz3dR.jpg" width="46" alt=""> **Corra!** <br><sub>Get Out</sub> | 2017 | **85,4** | 7,8 (844 mil) | 98% (403) | 85 | 86% | Prime Video, Disney+, Telecine (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 3 | <img src="https://image.tmdb.org/t/p/w342/gQ76UL64RQe3oHwiwHwODTC23g4.jpg" width="46" alt=""> **Resident Evil** | 2026 | **83,2** | 7,6 (117 mil) | 96% (302) | 79 | 90% | em cartaz nos cinemas |
| 4 | <img src="https://image.tmdb.org/t/p/w342/wUc6IDf5ChjM1UyQye21qFBeJY0.jpg" width="46" alt=""> **Obsessão** <br><sub>Obsession</sub> | 2025 | **83,2** | 7,8 (412 mil) | 93% (329) | 77 | 94% | em cartaz nos cinemas; aluguel/compra: Amazon, Apple TV |
| 5 | <img src="https://image.tmdb.org/t/p/w342/jk1LYcbiuUr0tv37cVcmp4u9KcN.jpg" width="46" alt=""> **Um Lugar Silencioso** <br><sub>A Quiet Place</sub> | 2018 | **82,9** | 7,5 (673 mil) | 96% (386) | 82 | 83% | Netflix, Paramount+ · aluguel/compra: Amazon, Apple TV |
| 6 | <img src="https://image.tmdb.org/t/p/w342/psEJSjQr6I9GSJTdW28CKC4Kffs.jpg" width="46" alt=""> **A Hora do Mal** <br><sub>Weapons</sub> | 2025 | **81,8** | 7,4 (417 mil) | 93% (400) | 81 | 85% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 7 | <img src="https://image.tmdb.org/t/p/w342/olQPqv8AA6Wen8cufp0KCcQpLek.jpg" width="46" alt=""> **Extermínio: O Templo dos Ossos** <br><sub>28 Years Later: The Bone Temple</sub> | 2026 | **81,0** | 7,2 (133 mil) | 91% (351) | 81 | 88% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 8 | <img src="https://image.tmdb.org/t/p/w342/QqHtwk0oHYed26zra9WGQGyBSm.jpg" width="46" alt=""> **Invasão Zumbi** <br><sub>Train to Busan</sub> | 2016 | **80,7** | 7,6 (318 mil) | 95% (130) | 73 | 90% | Prime Video, Netflix, Telecine (canal no Prime Video) · aluguel/compra: Apple TV |
| 9 | <img src="https://image.tmdb.org/t/p/w342/eoFvdVzVqkf7G9RwaT2yFAFjGKr.jpg" width="46" alt=""> **O Lamento** <br><sub>The Wailing</sub> | 2016 | **80,5** | 7,4 (104 mil) | 99% (87) | 81 | 81% | Adrenalina Pura (canal no Prime Video) · aluguel/compra: Apple TV |
| 10 | <img src="https://image.tmdb.org/t/p/w342/x9tUYQj6WrdVwoKimSdoMzkDABS.jpg" width="46" alt=""> **Hereditário** <br><sub>Hereditary</sub> | 2018 | **79,9** | 7,3 (475 mil) | 90% (385) | 87 | 72% | Prime Video, Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 11 | <img src="https://image.tmdb.org/t/p/w342/qN0attJyVKppNgftg7NCozwrmAP.jpg" width="46" alt=""> **Desconhecidos** <br><sub>Strange Darling</sub> | 2023 | **79,8** | 7,0 (73 mil) | 96% (164) | 80 | 85% | Telecine (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 12 | <img src="https://image.tmdb.org/t/p/w342/7U3lC4YnHD8zpeoxbY6Hsj9jyeu.jpg" width="46" alt=""> **Fale Comigo** <br><sub>Talk to Me</sub> | 2022 | **79,6** | 7,1 (229 mil) | 94% (300) | 76 | 83% | Prime Video, HBO Max, Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 13 | <img src="https://image.tmdb.org/t/p/w342/bqWvndlCAcBteUaHOL5HHEN5uHn.jpg" width="46" alt=""> **Um Lugar Silencioso - Parte II** <br><sub>A Quiet Place Part II</sub> | 2020 | **79,6** | 7,2 (331 mil) | 91% (366) | 71 | 92% | Netflix, Paramount+, Universal+ (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 14 | <img src="https://image.tmdb.org/t/p/w342/zdowK9GrOxK0YddhXuMPyxnTA02.jpg" width="46" alt=""> **O Farol** <br><sub>The Lighthouse</sub> | 2019 | **79,1** | 7,3 (312 mil) | 90% (398) | 83 | 72% | aluguel/compra: Amazon, Apple TV |
| 15 | <img src="https://image.tmdb.org/t/p/w342/67gVCA33yHpFkFyqhDJrt21MvYI.jpg" width="46" alt=""> **O Homem Invisível** <br><sub>The Invisible Man</sub> | 2020 | **79,0** | 7,1 (293 mil) | 91% (422) | 72 | 88% | Prime Video, Telecine (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 16 | <img src="https://image.tmdb.org/t/p/w342/cTgLkhIMmzwH1NAaq7NDbFN20zi.jpg" width="46" alt=""> **Pearl: Uma História de Origem 'X'** <br><sub>Pearl</sub> | 2022 | **78,8** | 7,0 (167 mil) | 93% (218) | 76 | 83% | aluguel/compra: Amazon, Apple TV |
| 17 | <img src="https://image.tmdb.org/t/p/w342/blckaGzdEJ4PdG5RxZPcb77VYFV.jpg" width="46" alt=""> **Entrevista com o Demônio** <br><sub>Late Night with the Devil</sub> | 2023 | **78,6** | 7,0 (155 mil) | 97% (239) | 72 | 82% | HBO Max, Netflix, Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 18 | <img src="https://image.tmdb.org/t/p/w342/2dEoQ2eWk3evQQBNUxPnZsPDq1N.jpg" width="46" alt=""> **A Meia-Irmã Feia** <br><sub>The Ugly Stepsister</sub> | 2025 | **77,8** | 7,0 (50 mil) | 96% (141) | 70 | 85% | MUBI · em cartaz nos cinemas; aluguel/compra: Apple TV |
| 19 | <img src="https://image.tmdb.org/t/p/w342/n2hyhBPIYbwvCSipcawcc8iEAsH.jpg" width="46" alt=""> **O Predador: A Caçada** <br><sub>Prey</sub> | 2022 | **77,2** | 7,1 (279 mil) | 94% (289) | 71 | 74% | Disney+ |
| 20 | <img src="https://image.tmdb.org/t/p/w342/mXsvEjsWLvco0hLfhe5FgwmY3qg.jpg" width="46" alt=""> **Noites Brutais** <br><sub>Barbarian</sub> | 2022 | **77,0** | 7,0 (279 mil) | 92% (212) | 78 | 70% | Paramount+, Telecine (canal no Prime Video), Universal+ (canal no Prime Video) |

### Também recomendados: IMDb ≥ 6,5 e RT ≥ 85%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 21 | <img src="https://image.tmdb.org/t/p/w342/rB0tZwNImTT8febX5qVycZ5YVeF.jpg" width="46" alt=""> **Frankenstein** | 2025 | **80,3** | 7,4 (344 mil) | 85% (383) | 78 | 94% | Netflix |
| 22 | <img src="https://image.tmdb.org/t/p/w342/mAwGTx2EOdiY6AiWauGICPUrELg.jpg" width="46" alt=""> **Acampamento Miasma: Adolescência, Sexo e Morte** <br><sub>Teenage Sex and Death at Camp Miasma</sub> | 2026 | **79,4** | 6,5 (24 mil) | 94% (278) | 89 | 78% | MUBI · aluguel/compra: Amazon, Apple TV |
| 23 | <img src="https://image.tmdb.org/t/p/w342/vWeOgzlhnP1sS23H3rzctGHB9Nb.jpg" width="46" alt=""> **A Substância** <br><sub>The Substance</sub> | 2024 | **78,2** | 7,2 (472 mil) | 89% (380) | 78 | 76% | MUBI, Netflix · aluguel/compra: Amazon, Apple TV |
| 24 | <img src="https://image.tmdb.org/t/p/w342/zwphX6D0pFzb6SI95wwVkIQzxZJ.jpg" width="46" alt=""> **Oddity: Objetos Obscuros** <br><sub>Oddity</sub> | 2024 | **78,2** | 6,7 (64 mil) | 96% (133) | 78 | 85% | Telecine (canal no Prime Video) · aluguel/compra: Amazon |
| 25 | <img src="https://image.tmdb.org/t/p/w342/aU0X5Ano994f3vhWdD5wnpkfcjV.jpg" width="46" alt=""> **Raw** | 2016 | **78,2** | 6,9 (98 mil) | 93% (201) | 81 | 76% | Sem oferta legal encontrada no Brasil |
| 26 | <img src="https://image.tmdb.org/t/p/w342/rpU5DGrTVdqcygZBB9npt1WMFch.jpg" width="46" alt=""> **Socorro!** <br><sub>Send Help</sub> | 2026 | **78,1** | 6,7 (161 mil) | 92% (303) | 75 | 86% | Disney+ |
| 27 | <img src="https://image.tmdb.org/t/p/w342/t6cWfm0o5TzCa3nHtHhXpzjBc8V.jpg" width="46" alt=""> **O Mal que Nos Habita** <br><sub>When Evil Lurks</sub> | 2023 | **77,8** | 6,9 (65 mil) | 96% (122) | 75 | 84% | Netflix · aluguel/compra: Apple TV |
| 28 | <img src="https://image.tmdb.org/t/p/w342/x3J781PsdMrjenzQKM5eJXqK5Nd.jpg" width="46" alt=""> **Premonição 6: Laços de Sangue** <br><sub>Final Destination: Bloodlines</sub> | 2025 | **77,5** | 6,7 (174 mil) | 92% (235) | 73 | 86% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 29 | <img src="https://image.tmdb.org/t/p/w342/4BarWJRYFB5fN7LsJI9U2ul79hB.jpg" width="46" alt=""> **X: A Marca da Morte** <br><sub>X</sub> | 2022 | **77,3** | 6,5 (231 mil) | 94% (229) | 80 | 76% | MGM+ (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 30 | <img src="https://image.tmdb.org/t/p/w342/xfmnUz6C5WRboIMQZD0j3SNDT7v.jpg" width="46" alt=""> **Faça Ela Voltar** <br><sub>Bring Her Back</sub> | 2025 | **77,2** | 7,1 (145 mil) | 89% (272) | 75 | 79% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 31 | <img src="https://image.tmdb.org/t/p/w342/qt2UTzGsFCHF729kKdJOvh8YT4g.jpg" width="46" alt=""> **Cuidado com Quem Chama** <br><sub>Host</sub> | 2020 | **76,9** | 6,5 (54 mil) | 98% (98) | 73* | 70% | Prime Video, Pluto TV (grátis) · aluguel/compra: Apple TV |
| 32 | <img src="https://image.tmdb.org/t/p/w342/ioceyCFcOC9LfUCkOGZNMbsuc2o.jpg" width="46" alt=""> **Nós** <br><sub>Us</sub> | 2019 | **76,7** | 6,8 (402 mil) | 93% (551) | 81 | 62% | Prime Video, Telecine (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 33 | <img src="https://image.tmdb.org/t/p/w342/uYxz0lIiNgErrPhQbSjUdwYxtFc.jpg" width="46" alt=""> **It: A Coisa** <br><sub>It</sub> | 2017 | **76,6** | 7,3 (714 mil) | 85% (391) | 69 | 84% | HBO Max, Universal+ (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 34 | <img src="https://image.tmdb.org/t/p/w342/fn5QNtG3LLXC3e7ZTQDYP92kFYc.jpg" width="46" alt=""> **Hokum: O Pesadelo da Bruxa** <br><sub>Hokum</sub> | 2026 | **76,4** | 6,6 (74 mil) | 90% (209) | 76 | 82% | Prime Video · aluguel/compra: Amazon, Apple TV |
| 35 | <img src="https://image.tmdb.org/t/p/w342/fbkUfzmVzEBFSt6p7VigknREIJT.jpg" width="46" alt=""> **Nosferatu** | 2024 | **76,3** | 7,1 (281 mil) | 85% (385) | 78 | 73% | Netflix · aluguel/compra: Amazon, Apple TV |
| 36 | <img src="https://image.tmdb.org/t/p/w342/tBtjyqf8oIdeFkis41bdaJzewBh.jpg" width="46" alt=""> **O Homem nas Trevas** <br><sub>Don't Breathe</sub> | 2016 | **76,2** | 7,1 (337 mil) | 88% (244) | 71 | 79% | Sony One (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 37 | <img src="https://image.tmdb.org/t/p/w342/naszJRWpzgbrR9vdifVoQ9IpNqW.jpg" width="46" alt=""> **Exit 8** | 2025 | **76,0** | 6,5 (38 mil) | 92% (177) | 71 | 86% | Paramount+ · aluguel/compra: Amazon, Apple TV |
| 38 | <img src="https://image.tmdb.org/t/p/w342/rxNelQvAjOmNGUUHRujmsHiPEIh.jpg" width="46" alt=""> **O Menu** <br><sub>The Menu</sub> | 2022 | **76,0** | 7,1 (521 mil) | 88% (338) | 71 | 76% | Disney+ |
| 39 | <img src="https://image.tmdb.org/t/p/w342/w2J7sk5ZFP1yFHLKCbe3YGnXPYA.jpg" width="46" alt=""> **Santa Maud** <br><sub>Saint Maud</sub> | 2019 | **76,0** | 6,6 (57 mil) | 92% (195) | 83 | 67% | aluguel/compra: Amazon, Apple TV |
| 40 | <img src="https://image.tmdb.org/t/p/w342/j5e2YS1PRUVC1YgSool0JJyNLxJ.jpg" width="46" alt=""> **Herege** <br><sub>Heretic</sub> | 2024 | **75,9** | 7,0 (243 mil) | 89% (295) | 71 | 76% | Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 41 | <img src="https://image.tmdb.org/t/p/w342/fSruOTrU6rnEZbAutI7iBNry39y.jpg" width="46" alt=""> **Mandy: Sede de Vingança** <br><sub>Mandy</sub> | 2018 | **75,7** | 6,5 (100 mil) | 91% (253) | 83 | 68% | aluguel/compra: Amazon, Apple TV |
| 42 | <img src="https://image.tmdb.org/t/p/w342/qE0XKOHZvXtiM4aBLlTPUVZiIc5.jpg" width="46" alt=""> **A Longa Marcha: Caminhe ou Morra** <br><sub>The Long Walk</sub> | 2025 | **75,6** | 6,6 (155 mil) | 88% (296) | 71 | 85% | Telecine (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 43 | <img src="https://image.tmdb.org/t/p/w342/m9jfOWLuyYejyJX17wRFUQGtUji.jpg" width="46" alt=""> **Juntos** <br><sub>Together</sub> | 2025 | **75,4** | 6,7 (91 mil) | 89% (246) | 75 | 75% | Prime Video · aluguel/compra: Amazon, Apple TV |
| 44 | <img src="https://image.tmdb.org/t/p/w342/nuRDoKqbly63XbNQNbsCo2JWvlM.jpg" width="46" alt=""> **Aniquilação** <br><sub>Annihilation</sub> | 2018 | **75,4** | 6,8 (400 mil) | 88% (332) | 79 | 67% | Universal+ (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 45 | <img src="https://image.tmdb.org/t/p/w342/t1G9OlLHGTPRpnFnB6NHAlOqmHI.jpg" width="46" alt=""> **Hush: A Morte Ouve** <br><sub>Hush</sub> | 2016 | **75,1** | 6,6 (173 mil) | 92% (48) | 67* | 73% | Plex (grátis) |
| 46 | <img src="https://image.tmdb.org/t/p/w342/a1pgQeEge47xrS4jGlDwIHiieVK.jpg" width="46" alt=""> **Backrooms: Um Não-Lugar** <br><sub>Backrooms</sub> | 2026 | **74,9** | 6,7 (238 mil) | 86% (316) | 76 | 74% | em cartaz nos cinemas; aluguel/compra: Amazon, Apple TV |
| 47 | <img src="https://image.tmdb.org/t/p/w342/k5dJuAdjv1wCq2Vzj1GZfwGmLoU.jpg" width="46" alt=""> **Casamento Sangrento** <br><sub>Ready or Not</sub> | 2019 | **74,5** | 6,9 (270 mil) | 89% (324) | 64 | 78% | Disney+ |
| 48 | <img src="https://image.tmdb.org/t/p/w342/2D0lOSwNAq1jUmeJgrdgPbBY9dK.jpg" width="46" alt=""> **O Culto** <br><sub>The Endless</sub> | 2017 | **74,2** | 6,5 (59 mil) | 91% (127) | 80 | 67% | aluguel/compra: Apple TV |
| 49 | <img src="https://image.tmdb.org/t/p/w342/2K5LCXOqlbzRu7mWHbDnLdDQj6I.jpg" width="46" alt=""> **Extermínio: A Evolução** <br><sub>28 Years Later</sub> | 2025 | **73,9** | 6,6 (231 mil) | 88% (399) | 77 | 63% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 50 | <img src="https://image.tmdb.org/t/p/w342/ypHiYvSJmHIyRDRiosZuE595uir.jpg" width="46" alt=""> **Sorria 2** <br><sub>Smile 2</sub> | 2024 | **73,9** | 6,7 (157 mil) | 86% (212) | 67 | 81% | Paramount+ · aluguel/compra: Amazon, Apple TV |
| 51 | <img src="https://image.tmdb.org/t/p/w342/kYFyeWz6AfKq9e3PEY2GREZ39Ay.jpg" width="46" alt=""> **Jogo Perigoso** <br><sub>Gerald's Game</sub> | 2017 | **73,1** | 6,5 (145 mil) | 91% (81) | 77 | 69% | Netflix |
| 52 | <img src="https://image.tmdb.org/t/p/w342/cvdCMFP0pNYXtWXVuRD5Hqp6vuT.jpg" width="46" alt=""> **O Monstro do Meu Quarto** <br><sub>Dust Bunny</sub> | 2025 | **73,0** | 6,5 (22 mil) | 85% (117) | 73 | 82% | Sem oferta legal encontrada no Brasil |
| 53 | <img src="https://image.tmdb.org/t/p/w342/xC9GZeJZ3NagdkGg9nLQx0aPG6J.jpg" width="46" alt=""> **Possessor** | 2020 | **72,9** | 6,5 (55 mil) | 94% (226) | 72 | 59% | HBO Max |
| 54 | <img src="https://image.tmdb.org/t/p/w342/hsX1vt168fNSMSYwTVi8M9O0hLu.jpg" width="46" alt=""> **Rua do Medo: 1666 – Parte 3** <br><sub>Fear Street: Part Three - 1666</sub> | 2021 | **72,8** | 6,6 (78 mil) | 89% (100) | 68 | 75% | Netflix |
| 55 | <img src="https://image.tmdb.org/t/p/w342/pYHypEGMKtFTSQqfWC6IJFeaz1J.jpg" width="46" alt=""> **A Morte do Demônio: A Ascensão** <br><sub>Evil Dead Rise</sub> | 2023 | **72,7** | 6,5 (180 mil) | 85% (242) | 69 | 76% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 56 | <img src="https://image.tmdb.org/t/p/w342/uicSprflqrrhWykOuJjHQ9lSLJ1.jpg" width="46" alt=""> **Rua do Medo: 1978 - Parte 2** <br><sub>Fear Street: Part Two - 1978</sub> | 2021 | **72,7** | 6,7 (93 mil) | 88% (110) | 61 | 81% | Netflix |
| 57 | <img src="https://image.tmdb.org/t/p/w342/29QY0eScq4chCvZNBx3BIxNdbml.jpg" width="46" alt=""> **Buddy** | 2026 | **72,6** | 6,7 (19 mil) | 88% (138) | 67 | 76% | Sem oferta legal encontrada no Brasil |
| 58 | <img src="https://image.tmdb.org/t/p/w342/uURBOrqLFyU8iKODcI3t2Xkbhqs.jpg" width="46" alt=""> **Longlegs - Vínculo Mortal** <br><sub>Longlegs</sub> | 2024 | **72,4** | 6,5 (236 mil) | 85% (323) | 77 | 61% | Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 59 | <img src="https://image.tmdb.org/t/p/w342/9hY2AVLqdklon41dr9PSQ4KdW8K.jpg" width="46" alt=""> **A Autópsia** <br><sub>The Autopsy of Jane Doe</sub> | 2016 | **71,9** | 6,8 (171 mil) | 86% (108) | 65 | 72% | Prime Video, Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 60 | <img src="https://image.tmdb.org/t/p/w342/o5tWAiHfxEvu2z1qkJKU4gW1uPY.jpg" width="46" alt=""> **Dezesseis Facadas** <br><sub>Totally Killer</sub> | 2023 | **70,8** | 6,5 (71 mil) | 85% (110) | 62 | 76% | Prime Video |
| 61 | <img src="https://image.tmdb.org/t/p/w342/sfRJ6xtfaT1uUWA4YsxU3hGFJbQ.jpg" width="46" alt=""> **Perigo Próximo** <br><sub>Better Watch Out</sub> | 2016 | **70,0** | 6,5 (54 mil) | 89% (66) | 67 | 63% | aluguel/compra: Amazon, Apple TV |

<sub>* Metascore com menos de 10 críticas: exibido, mas fora do cálculo.</sub>

#### Por que cada filme está aqui
- **1. Pecadores** (2025, dir./criação: Ryan Coogler): Gêmeos (Michael B. Jordan, em papel duplo) abrem um juke joint no Mississippi de 1932 e atraem vampiros. Blues, folclore e história americana num só corpo. Recorde histórico de 16 indicações ao Oscar.
- **2. Corra!** (2017, dir./criação: Jordan Peele): Um jovem negro (Daniel Kaluuya) passa o fim de semana na casa de campo da família da namorada branca, e a hospitalidade esconde algo monstruoso. Peele ganhou o Oscar de roteiro original.
- **3. Resident Evil** (2026, dir./criação: Zach Cregger): A franquia recomeça do zero: um entregador de material médico (Austin Abrams) atravessa uma noite de surto em Raccoon City. Teve a melhor estreia da série nos EUA (US$ 60 milhões).
- **4. Obsessão** (2025, dir./criação: Curry Barker): Um rapaz quebra o “Salgueiro dos Desejos” para conquistar a garota que ama, e o desejo cobra um preço. A estreia em longa de Curry Barker virou fenômeno: são mais de 400 mil votos no IMDb.
- **5. Um Lugar Silencioso** (2018, dir./criação: John Krasinski): Uma família sobrevive em silêncio absoluto num mundo dominado por criaturas que caçam pelo som. Emily Blunt e Millicent Simmonds, atriz surda, carregam o filme.
- **6. A Hora do Mal** (2025, dir./criação: Zach Cregger): Dezessete crianças da mesma turma saem de casa às 2h17 da madrugada e desaparecem. O mistério é contado em capítulos por pontos de vista diferentes. Amy Madigan ganhou o Oscar de atriz coadjuvante como Tia Gladys.
- **7. Extermínio: O Templo dos Ossos** (2026, dir./criação: Nia DaCosta): Continuação direta de Extermínio: A Evolução. Ralph Fiennes (Dr. Kelson) e Jack O’Connell (o culto de Sir Jimmy Crystal) dominam o capítulo mais sombrio da saga.
- **8. Invasão Zumbi** (2016, dir./criação: Yeon Sang-ho): Um pai workaholic (Gong Yoo) e a filha embarcam no trem Seul–Busan no dia em que estoura um surto zumbi. Ação claustrofóbica e um dos finais mais tristes do gênero.
- **9. O Lamento** (2016, dir./criação: Na Hong-jin): Num vilarejo coreano, mortes violentas coincidem com a chegada de um estrangeiro japonês, e um policial atrapalhado mergulha em xamanismo e possessão. Duas horas e meia de pavor crescente.
- **10. Hereditário** (2018, dir./criação: Ari Aster): Depois da morte da avó, uma família desmorona entre luto, culpa e algo que foi herdado. Toni Collette tem uma atuação histórica na estreia de Ari Aster.
- **11. Desconhecidos** (2023, dir./criação: JT Mollner): Um encontro casual vira caçada, contado em seis capítulos fora de ordem que brincam com as expectativas do slasher. Rodado em 35 mm, com fotografia de Giovanni Ribisi.
- **12. Fale Comigo** (2022, dir./criação: Danny e Michael Philippou): Adolescentes australianos usam uma mão embalsamada para “receber” espíritos por 90 segundos, até alguém passar do tempo. A estreia que transformou os irmãos Philippou em grife.
- **13. Um Lugar Silencioso - Parte II** (2020, dir./criação: John Krasinski): Continuação imediata: a família Abbott deixa a fazenda e descobre que outros sobreviventes podem ser tão perigosos quanto as criaturas.
- **14. O Farol** (2019, dir./criação: Robert Eggers): Dois faroleiros (Robert Pattinson e Willem Dafoe), isolados numa ilha da Nova Inglaterra nos anos 1890, afundam na loucura. Preto e branco, imagem quase quadrada e um pesadelo marítimo. _Nota de curadoria: O RT classifica como Suspense/Drama, mas é terror psicológico e folclórico de Robert Eggers: mantido._
- **15. O Homem Invisível** (2020, dir./criação: Leigh Whannell): Uma mulher (Elisabeth Moss) foge de um namorado abusivo, que aparentemente se mata, e passa a ser perseguida por alguém que ninguém vê. O clássico relido como terror sobre violência doméstica.
- **16. Pearl: Uma História de Origem 'X'** (2022, dir./criação: Ti West): Prelúdio de X, ambientado em 1918: Mia Goth vive uma jovem de fazenda que sonha com o estrelato e explode em violência. O monólogo final é antológico.
- **17. Entrevista com o Demônio** (2023, dir./criação: Cameron e Colin Cairnes): Halloween de 1977: um apresentador de talk show em crise de audiência leva uma garota “possuída” ao vivo. Falso found footage de época, com David Dastmalchian em grande forma.
- **18. A Meia-Irmã Feia** (2025, dir./criação: Emilie Blichfeldt): Cinderela vista pela meia-irmã que se mutila para caber no padrão de beleza. Body horror norueguês, cruel e muito engraçado.
- **19. O Predador: A Caçada** (2022, dir./criação: Dan Trachtenberg): O Predador chega às Grandes Planícies de 1719. Amber Midthunder vive Naru, jovem comanche que quer provar seu valor como caçadora. Simples, físico e tenso.
- **20. Noites Brutais** (2022, dir./criação: Zach Cregger): Uma mulher reserva um Airbnb em Detroit e descobre que ele já está ocupado por um estranho. O porão esconde muito mais, e a virada no meio do filme é das mais comentadas do terror recente.
- **21. Frankenstein** (2025, dir./criação: Guillermo del Toro): O projeto de uma vida de del Toro: Oscar Isaac é Victor e Jacob Elordi é a Criatura. Mais tragédia gótica do que susto, com design de produção suntuoso.
- **22. Acampamento Miasma: Adolescência, Sexo e Morte** (2026, dir./criação: Jane Schoenbrun): Uma jovem diretora (Hannah Einbinder) é contratada para reviver uma franquia slasher e fica obcecada pela final girl original (Gillian Anderson). Metaterror queer.
- **23. A Substância** (2024, dir./criação: Coralie Fargeat): Uma estrela decadente (Demi Moore) usa uma droga que cria uma versão mais jovem de si mesma (Margaret Qualley). Body horror satírico sobre etarismo e Hollywood.
- **24. Oddity: Objetos Obscuros** (2024, dir./criação: Damian McCarthy): Uma vidente cega investiga a morte da irmã gêmea e leva um boneco de madeira assustador para a casa do viúvo. Terror irlandês de casa isolada, de precisão cirúrgica.
- **25. Raw** (2016, dir./criação: Julia Ducournau): Uma caloura vegetariana de veterinária é obrigada a comer carne crua num trote e desperta um apetite canibal. Estreia de Ducournau, que depois ganharia a Palma de Ouro com Titane.
- **26. Socorro!** (2026, dir./criação: Sam Raimi): Raimi volta ao terror: uma funcionária maltratada (Rachel McAdams) e o chefe (Dylan O’Brien) sobrevivem a um acidente aéreo numa ilha, e a hierarquia vira de cabeça para baixo.
- **27. O Mal que Nos Habita** (2023, dir./criação: Demián Rugna): No interior da Argentina, dois irmãos tentam se livrar de um “apodrecido” (um possuído) e acabam espalhando o mal. Um dos filmes de possessão mais cruéis do século.
- **28. Premonição 6: Laços de Sangue** (2025, dir./criação: Zach Lipovsky e Adam Stein): Uma universitária tem visões do desastre que a avó evitou em 1968, e a Morte vem cobrar a família inteira. A franquia renasce, com a última aparição de Tony Todd.
- **29. X: A Marca da Morte** (2022, dir./criação: Ti West): Texas, 1979: uma equipe filma um pornô numa fazenda e vira presa do casal de idosos donos do lugar. Mia Goth faz papel duplo.
- **30. Faça Ela Voltar** (2025, dir./criação: Danny e Michael Philippou): Dois irmãos vão morar com uma mãe adotiva acolhedora (Sally Hawkins), cujo luto esconde um ritual. É o filme mais brutal e mais triste dos Philippou.
- **31. Cuidado com Quem Chama** (2020, dir./criação: Rob Savage): Seis amigas fazem uma sessão espírita por Zoom no lockdown de 2020. Filmado inteiramente como videochamada, com menos de uma hora de duração.
- **32. Nós** (2019, dir./criação: Jordan Peele): Numa viagem à praia, uma família é atacada por sósias de si mesma. Lupita Nyong’o em papel duplo, numa das atuações mais assustadoras do gênero.
- **33. It: A Coisa** (2017, dir./criação: Andy Muschietti): O Clube dos Perdedores enfrenta Pennywise (Bill Skarsgård) em Derry, 1989. Uma das maiores bilheterias de terror da história.
- **34. Hokum: O Pesadelo da Bruxa** (2026, dir./criação: Damian McCarthy): Um romancista (Adam Scott) vai a uma pousada irlandesa para espalhar as cinzas dos pais. A suíte de lua de mel fica sempre trancada, porque guarda uma bruxa.
- **35. Nosferatu** (2024, dir./criação: Robert Eggers): Releitura do clássico de 1922, com Lily-Rose Depp como Ellen e Bill Skarsgård irreconhecível como o Conde Orlok. Terror gótico de textura impressionante.
- **36. O Homem nas Trevas** (2016, dir./criação: Fede Álvarez): Três jovens assaltam a casa de um veterano de guerra cego, achando que vai ser fácil. Não é: Stephen Lang está aterrorizante.
- **37. Exit 8** (2025, dir./criação: Genki Kawamura): Adaptação do game japonês: um homem (Kazunari Ninomiya) fica preso num corredor de metrô em looping e precisa detectar anomalias para escapar.
- **38. O Menu** (2022, dir./criação: Mark Mylod): Um casal janta num restaurante exclusivo numa ilha, e o chef (Ralph Fiennes) preparou um menu de vingança. Sátira de terror sobre gastronomia e classe social.
- **39. Santa Maud** (2019, dir./criação: Rose Glass): Uma enfermeira recém-convertida (Morfydd Clark) se convence de que precisa salvar a alma da paciente terminal de quem cuida. Terror religioso britânico, curto e devastador.
- **40. Herege** (2024, dir./criação: Scott Beck e Bryan Woods): Duas missionárias mórmons batem à porta do Sr. Reed (Hugh Grant), que quer debater religião e não deixa ninguém sair. Hugh Grant num de seus melhores papéis.
- **41. Mandy: Sede de Vingança** (2018, dir./criação: Panos Cosmatos): Em 1983, um lenhador (Nicolas Cage) caça a seita que destruiu sua vida. Pesadelo psicodélico com trilha de Jóhann Jóhannsson.
- **42. A Longa Marcha: Caminhe ou Morra** (2025, dir./criação: Francis Lawrence): Adaptação de Stephen King (como Richard Bachman): 50 jovens caminham sem parar, e quem fica abaixo da velocidade mínima é executado. Terror de resistência física e moral.
- **43. Juntos** (2025, dir./criação: Michael Shanks): Dave Franco e Alison Brie, casados na vida real, vivem um casal cujos corpos começam a se fundir literalmente. Body horror sobre codependência.
- **44. Aniquilação** (2018, dir./criação: Alex Garland): Uma bióloga (Natalie Portman) entra no “Brilho”, uma zona que faz sofrer mutação tudo o que vive. Ficção científica que vira terror cósmico; a cena do urso é puro pavor. _Nota de curadoria: O RT classifica como Ficção científica/Aventura, mas o centro é terror cósmico e de mutação: mantido._
- **45. Hush: A Morte Ouve** (2016, dir./criação: Mike Flanagan): Uma escritora surda que vive isolada no mato é cercada por um assassino mascarado. Flanagan antes da fama, com tensão do início ao fim em pouco mais de 80 minutos.
- **46. Backrooms: Um Não-Lugar** (2026, dir./criação: Kane Parsons): O criador da websérie viral estreia pela A24 como o diretor mais jovem da história do estúdio. O dono de uma loja de móveis (Chiwetel Ejiofor) encontra uma passagem para um labirinto infinito de salas amarelas.
- **47. Casamento Sangrento** (2019, dir./criação: Matt Bettinelli-Olpin e Tyler Gillett): Na noite de núpcias, a noiva (Samara Weaving) descobre que a família rica do marido vai caçá-la num esconde-esconde mortal. Terror-comédia sangrento.
- **48. O Culto** (2017, dir./criação: Justin Benson e Aaron Moorhead): Dois irmãos voltam ao culto de onde fugiram anos antes e encontram fenômenos que desafiam o tempo. Terror cósmico de baixo orçamento e muita imaginação.
- **49. Extermínio: A Evolução** (2025, dir./criação: Danny Boyle): Boyle e Alex Garland retornam: um garoto (Alfie Williams) deixa pela primeira vez a ilha isolada rumo ao continente infestado. É ousado, estranho e emotivo.
- **50. Sorria 2** (2024, dir./criação: Parker Finn): A maldição do sorriso contamina uma pop star (Naomi Scott) às vésperas da turnê de retorno. É maior, mais estilosa e mais cruel que o original.
- **51. Jogo Perigoso** (2017, dir./criação: Mike Flanagan): Um fim de semana do casal numa casa isolada dá errado: o marido morre e a mulher (Carla Gugino) fica algemada à cama. Adaptação de um Stephen King que muitos consideravam infilmável.
- **52. O Monstro do Meu Quarto** (2025, dir./criação: Bryan Fuller): Estreia de Bryan Fuller (Hannibal) na direção de longas: uma menina contrata o vizinho matador de aluguel (Mads Mikkelsen) para eliminar o monstro debaixo da cama.
- **53. Possessor** (2020, dir./criação: Brandon Cronenberg): Uma assassina (Andrea Riseborough) usa implantes para possuir o corpo de outras pessoas e matar por encomenda, até perder o controle de quem é. Body horror violentíssimo.
- **54. Rua do Medo: 1666 – Parte 3** (2021, dir./criação: Leigh Janiak): Fecho da trilogia: a origem da maldição de Sarah Fier na colônia de 1666 e o acerto de contas em 1994.
- **55. A Morte do Demônio: A Ascensão** (2023, dir./criação: Lee Cronin): Os deadites invadem um prédio de apartamentos em Los Angeles: uma mãe possuída contra os próprios filhos. Um banho de sangue fiel à franquia.
- **56. Rua do Medo: 1978 - Parte 2** (2021, dir./criação: Leigh Janiak): Segunda parte da trilogia Rua do Medo: um massacre no acampamento Nightwing, em homenagem declarada ao slasher de acampamento.
- **57. Buddy** (2026, dir./criação: Casper Kelly): Do criador de “Too Many Cooks”: crianças ficam presas num programa infantil ao estilo anos 90, com um unicórnio apresentador nada amigável. Elenco com Cristin Milioti e Michael Shannon.
- **58. Longlegs - Vínculo Mortal** (2024, dir./criação: Osgood Perkins): Uma agente do FBI (Maika Monroe) caça um assassino satânico (Nicolas Cage). A atmosfera é sufocante, e o marketing virou fenômeno à parte.
- **59. A Autópsia** (2016, dir./criação: André Øvredal): Pai e filho legistas (Brian Cox e Emile Hirsch) examinam numa noite de tempestade o corpo intacto de uma desconhecida. Cada incisão revela algo pior.
- **60. Dezesseis Facadas** (2023, dir./criação: Nahnatchka Khan): Uma adolescente volta no tempo até 1987 para impedir o primeiro crime de um serial killer. Comédia de terror no espírito de “De Volta para o Futuro” encontra “Pânico”.
- **61. Perigo Próximo** (2016, dir./criação: Chris Peckham): Uma babá cuida de um garoto de 12 anos na véspera de Natal quando a casa parece estar sendo invadida. Terror natalino com uma virada cruel.

---

## 3. 📺 Séries

### Elite: IMDb ≥ 7,5 e RT ≥ 90%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 1 | <img src="https://image.tmdb.org/t/p/w342/zXfQcdTx0jxbH5Atpwjvb5z5VjE.jpg" width="46" alt=""> **Kingdom** | 2019 | **85,9** | 8,3 (66 mil) | 98% (32) | — | 91% | Netflix |
| 2 | <img src="https://image.tmdb.org/t/p/w342/hazWZ75ml5Er3MQsFetIzoeWs99.jpg" width="46" alt=""> **O Segredo de Widow's Bay** <br><sub>Widow's Bay</sub> | 2026 | **84,3** | 8,1 (100 mil) | 98% (109) | 78 | 92% | Apple TV |
| 3 | <img src="https://image.tmdb.org/t/p/w342/twfKp60THrcOIep9sjHODOOfO8d.jpg" width="46" alt=""> **Stranger Things** | 2016 | **83,2** | 8,6 (1750 mil) | 90% (663) | 74 | 82% | Netflix |
| 4 | <img src="https://image.tmdb.org/t/p/w342/2gyQRudrRU276fvkXMq4JNq3hzB.jpg" width="46" alt=""> **Evil: Contatos Sobrenaturais** <br><sub>Evil</sub> | 2019 | **82,8** | 7,7 (54 mil) | 96% (105) | 83 | 85% | Globoplay, Paramount+, Universal+ (canal no Prime Video) |
| 5 | <img src="https://image.tmdb.org/t/p/w342/IXwje9xtS8fvXhS4DkKN6RuxTa.jpg" width="46" alt=""> **Entrevista com o Vampiro** <br><sub>Interview with the Vampire</sub> | 2022 | **82,7** | 7,6 (46 mil) | 99% (105) | 83 | 79% | Prime Video, Netflix |
| 6 | <img src="https://image.tmdb.org/t/p/w342/eK9ZDIq7gPFRJ0GGaWvgrXLZgXX.jpg" width="46" alt=""> **Origem** <br><sub>From</sub> | 2022 | **81,9** | 7,7 (212 mil) | 96% (67) | 63* | 76% | Globoplay |
| 7 | <img src="https://image.tmdb.org/t/p/w342/xRnGrn7Z7SC0KIBodocoU1QgDZF.jpg" width="46" alt=""> **Yellowjackets** | 2021 | **77,9** | 7,7 (118 mil) | 92% (202) | 74 | 65% | Paramount+ |

### Também recomendadas: IMDb ≥ 7,0 e RT ≥ 80%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 8 | <img src="https://image.tmdb.org/t/p/w342/8qrRkFh1zhoGxnlRcqNPDzkXuHd.jpg" width="46" alt=""> **Alien: Earth** | 2025 | **78,2** | 7,1 (111 mil) | 94% (122) | 85 | 65% | Disney+ |
| 9 | <img src="https://image.tmdb.org/t/p/w342/fUVn5mScv83FfwrRUUR694yA7bd.jpg" width="46" alt=""> **Terror** <br><sub>The Terror</sub> | 2018 | **78,0** | 7,8 (64 mil) | 87% (115) | 74 | 77% | aluguel/compra: Amazon |
| 10 | <img src="https://image.tmdb.org/t/p/w342/ArSVoiEq2ljNIplabxRgJtamhnB.jpg" width="46" alt=""> **O Exorcista** <br><sub>The Exorcist</sub> | 2016 | **77,6** | 7,9 (34 mil) | 89% (64) | 62 | 90% | Sem oferta legal encontrada no Brasil |
| 11 | <img src="https://image.tmdb.org/t/p/w342/sdCJbGkvnIsIKLxaFQrviriODVq.jpg" width="46" alt=""> **Chucky** | 2021 | **77,1** | 7,2 (34 mil) | 95% (64) | 70 | 82% | Disney+, Prime Video (grátis), Universal+ (canal no Prime Video) |
| 12 | <img src="https://image.tmdb.org/t/p/w342/aMLUWhLtpSo45ibaWvE7ws3iyy7.jpg" width="46" alt=""> **Servant** | 2019 | **76,9** | 7,4 (54 mil) | 90% (116) | 70 | 78% | Apple TV |
| 13 | <img src="https://image.tmdb.org/t/p/w342/6dnUpv9ghx84pgxlMOb4uuJrWDs.jpg" width="46" alt=""> **Castle Rock** | 2018 | **75,9** | 7,5 (59 mil) | 88% (111) | 67 | 77% | Sem oferta legal encontrada no Brasil |
| 14 | <img src="https://image.tmdb.org/t/p/w342/fz7bdjxPColvEWCGr5Kiclzc86d.jpg" width="46" alt=""> **Lovecraft Country** | 2020 | **75,4** | 7,1 (52 mil) | 88% (142) | 79 | 64% | HBO Max |
| 15 | <img src="https://image.tmdb.org/t/p/w342/8hSvf5pHue3UzqBWTO9xMLPMOGn.jpg" width="46" alt=""> **O Mundo Sombrio de Sabrina** <br><sub>Chilling Adventures of Sabrina</sub> | 2018 | **75,0** | 7,4 (121 mil) | 82% (237) | 74 | 72% | Netflix |
| 16 | <img src="https://image.tmdb.org/t/p/w342/sxMMOIuV99LOwcJICx1Wy4O8fgi.jpg" width="46" alt=""> **O Gabinete de Curiosidades de Guillermo del Toro** <br><sub>Guillermo del Toro's Cabinet of Curiosities</sub> | 2022 | **74,9** | 7,0 (66 mil) | 93% (56) | 72 | 72% | Netflix |
| 17 | <img src="https://image.tmdb.org/t/p/w342/gMTfrLvrDaD0zrhpLZ7zXIIpKfJ.jpg" width="46" alt=""> **IT: Bem-Vindos a Derry** <br><sub>It: Welcome to Derry</sub> | 2025 | **74,8** | 7,9 (123 mil) | 81% (98) | 61 | 82% | HBO Max · aluguel/compra: Amazon |
| 18 | <img src="https://image.tmdb.org/t/p/w342/as0QIRSbRCOE1nr6CZyOJmqQ1z3.jpg" width="46" alt=""> **Arquivo 81** <br><sub>Archive 81</sub> | 2022 | **74,5** | 7,3 (70 mil) | 87% (39) | 73 | 75% | Netflix |

<sub>* Metascore com menos de 10 críticas (From tem 63 com apenas 7): exibido, mas fora do cálculo.</sub>

#### Por que cada série está aqui
- **1. Kingdom** (2019, dir./criação: Kim Eun-hee (roteiro)): Coreia da dinastia Joseon: o príncipe herdeiro investiga uma praga que transforma mortos em monstros famintos. Zumbis de época com intriga palaciana.
- **2. O Segredo de Widow's Bay** (2026, dir./criação: Katie Dippold): O prefeito (Matthew Rhys) de uma ilha amaldiçoada da Nova Inglaterra quer transformá-la em destino turístico. Terror-comédia que não economiza nos sustos de verdade.
- **3. Stranger Things** (2016, dir./criação: Irmãos Duffer): Hawkins, 1983: um garoto desaparece e os amigos descobrem experimentos secretos e o Mundo Invertido. A série que virou símbolo da Netflix, encerrada em 2025.
- **4. Evil: Contatos Sobrenaturais** (2019, dir./criação: Robert e Michelle King): Uma psicóloga cética (Katja Herbers), um padre em formação (Mike Colter) e um técnico investigam supostas possessões para a Igreja Católica.
- **5. Entrevista com o Vampiro** (2022, dir./criação: Rolin Jones): Louis (Jacob Anderson) conta sua vida ao lado de Lestat (Sam Reid) a um jornalista. A adaptação mais aclamada do universo de Anne Rice.
- **6. Origem** (2022, dir./criação: John Griffin): Uma cidadezinha de onde ninguém consegue sair. À noite, criaturas com rosto humano batem à porta pedindo para entrar. Harold Perrineau lidera o elenco.
- **7. Yellowjackets** (2021, dir./criação: Ashley Lyle e Bart Nickerson): Um time feminino de futebol cai nos ermos do Canadá em 1996. Vinte e cinco anos depois, as sobreviventes escondem o que fizeram para viver. Sobrevivência, canibalismo e algo sobrenatural. _Nota de curadoria: O RT classifica como Drama/Suspense, mas há canibalismo, sobrevivência e uma entidade sobrenatural no centro: mantida._
- **8. Alien: Earth** (2025, dir./criação: Noah Hawley): O xenomorfo chega à Terra de 2120: híbridos sintéticos com mentes de crianças enfrentam a carga de uma nave que caiu. Ficção científica de terror ambiciosa. _Nota de curadoria: O RT classifica como Drama/Ficção científica, mas é o xenomorfo de Alien, cânone do sci-fi horror: mantida._
- **9. Terror** (2018, dir./criação: David Kajganich (1ª temporada)): Antologia: a 1ª temporada segue a expedição Franklin presa no gelo do Ártico em 1847 e caçada por algo; a 2ª, nipo-americanos em campos de internamento.
- **10. O Exorcista** (2016, dir./criação: Jeremy Slater): Continuação do filme de 1973: dois padres enfrentam uma possessão numa família de Chicago. Foi cancelada após duas temporadas e virou cult.
- **11. Chucky** (2021, dir./criação: Don Mancini): O criador do Brinquedo Assassino leva Chucky para a TV, com Jennifer Tilly e Brad Dourif. É mais ousada e mais queer do que os filmes.
- **12. Servant** (2019, dir./criação: Tony Basgallop (criação) e M. Night Shyamalan): Um casal da Filadélfia trata um boneco reborn como filho, até a babá chegar e o boneco virar um bebê de verdade. _Nota de curadoria: O RT classifica como Drama/Suspense, mas é terror psicológico com ocultismo: mantida._
- **13. Castle Rock** (2018, dir./criação: Sam Shaw e Dustin Thomason): Antologia no universo de Stephen King, na cidadezinha do Maine que aparece em vários livros dele. Sissy Spacek e Lizzy Caplan brilham.
- **14. Lovecraft Country** (2020, dir./criação: Misha Green): Anos 50: um veterano negro cruza os EUA da segregação atrás do pai desaparecido e encontra monstros de Lovecraft e racistas igualmente mortais. _Nota de curadoria: O RT classifica só como Drama, mas os monstros de Lovecraft estão no centro: mantida._
- **15. O Mundo Sombrio de Sabrina** (2018, dir./criação: Roberto Aguirre-Sacasa): Sabrina (Kiernan Shipka), meio bruxa e meio mortal, precisa escolher entre a Igreja da Noite e a vida comum. Bem mais sombria que a versão dos anos 90.
- **16. O Gabinete de Curiosidades de Guillermo del Toro** (2022, dir./criação: Guillermo del Toro (curador)): Antologia de oito contos escolhidos por del Toro, com direção de nomes como Panos Cosmatos, Jennifer Kent e Ana Lily Amirpour.
- **17. IT: Bem-Vindos a Derry** (2025, dir./criação: Andy e Barbara Muschietti): Prelúdio de IT ambientado em 1962: a Derry dos anos 60 e a origem de Pennywise (Bill Skarsgård).
- **18. Arquivo 81** (2022, dir./criação: Rebecca Sonnenshine): Um arquivista (Mamoudou Athie) restaura fitas de uma documentarista desaparecida em 1994 e descobre um culto. Foi cancelada após uma temporada, mas está completa como história.

---

## 4. 🕯️ Minisséries

### Elite: IMDb ≥ 7,5 e RT ≥ 90%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 1 | <img src="https://image.tmdb.org/t/p/w342/mQQGdDgn4WpUL9PXssHecWkjfi1.jpg" width="46" alt=""> **A Maldição da Residência Hill** <br><sub>The Haunting of Hill House</sub> | 2018 | **83,9** | 8,5 (340 mil) | 93% (103) | 79 | 91% | Netflix |
| 2 | <img src="https://image.tmdb.org/t/p/w342/sDT2ZU9Xd2dt0svfO4qYYtziVP5.jpg" width="46" alt=""> **The Outsider** | 2020 | **81,0** | 7,6 (121 mil) | 91% (70) | — | 81% | HBO Max |
| 3 | <img src="https://image.tmdb.org/t/p/w342/b5MzNAgs1baKi32ln3yQoaKIsgZ.jpg" width="46" alt=""> **A Queda da Casa de Usher** <br><sub>The Fall of the House of Usher</sub> | 2023 | **79,6** | 7,9 (140 mil) | 91% (114) | 73 | 81% | Netflix |

### Também recomendadas: IMDb ≥ 7,0 e RT ≥ 80%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 4 | <img src="https://image.tmdb.org/t/p/w342/rka8ibtD6HayiEJmb6rns47lyAL.jpg" width="46" alt=""> **Missa da Meia-Noite** <br><sub>Midnight Mass</sub> | 2021 | **77,8** | 7,7 (177 mil) | 87% (102) | 75 | 79% | Netflix |
| 5 | <img src="https://image.tmdb.org/t/p/w342/fvJ08aPvfuPjQtpUDGWa3d3Dk9h.jpg" width="46" alt=""> **Carrie, a Estranha** <br><sub>Carrie</sub> | 2026 | **77,8** | 7,9 (50 mil) | 85% (133) | 71 | 82% | Prime Video |
| 6 | <img src="https://image.tmdb.org/t/p/w342/95pv9daC8yFm1BfaUyCTx7MfOs.jpg" width="46" alt=""> **The Walking Dead: The Ones Who Live** | 2024 | **73,7** | 7,7 (52 mil) | 88% (30) | 61 | 76% | Prime Video |
| 7 | <img src="https://image.tmdb.org/t/p/w342/V6Zy46oHLDSvL3ITh94NbL4OEo.jpg" width="46" alt=""> **A Maldição da Mansão Bly** <br><sub>The Haunting of Bly Manor</sub> | 2020 | **73,5** | 7,4 (149 mil) | 88% (105) | 63 | 69% | Netflix |


#### Por que cada minissérie está aqui
- **1. A Maldição da Residência Hill** (2018, dir./criação: Mike Flanagan): Os irmãos Crain cresceram na casa mais assombrada dos EUA e, adultos, ainda não escaparam dela. O episódio 6, em longos planos-sequência, virou referência.
- **2. The Outsider** (2020, dir./criação: Richard Price): Um treinador de beisebol infantil é preso por um crime brutal, mas estava em outra cidade na hora. Adaptação de Stephen King pela HBO, com Ben Mendelsohn e Cynthia Erivo. _Nota de curadoria: O RT classifica como Crime/Drama, mas a entidade sobrenatural de Stephen King está no centro: mantida._
- **3. A Queda da Casa de Usher** (2023, dir./criação: Mike Flanagan): Flanagan funde vários contos de Poe numa dinastia farmacêutica: os herdeiros de Roderick Usher morrem um a um. Elegante, venenosa e muito divertida.
- **4. Missa da Meia-Noite** (2021, dir./criação: Mike Flanagan): Um padre carismático chega a uma ilha pesqueira decadente, e milagres começam a acontecer. Terror religioso sobre fé, vício e culpa. Para muitos, é a obra-prima de Flanagan.
- **5. Carrie, a Estranha** (2026, dir./criação: Mike Flanagan): Flanagan reimagina Stephen King em 8 episódios: Summer H. Howell é Carrie White e Samantha Sloyan é a mãe fanática. Stephen King chamou a série de “brilhante”.
- **6. The Walking Dead: The Ones Who Live** (2024, dir./criação: Scott M. Gimple): Seis episódios para reunir Rick Grimes (Andrew Lincoln) e Michonne (Danai Gurira). É o fecho emocional do arco do casal no universo The Walking Dead.
- **7. A Maldição da Mansão Bly** (2020, dir./criação: Mike Flanagan): Uma governanta americana vai cuidar de duas crianças órfãs numa mansão inglesa. Releitura de Henry James, mais romance gótico do que susto.

> Poucas minisséries de terror lançadas desde 2016 passam nos cortes; a lista curta é resultado do método, não falta de busca.

---

## 5. 📡 Radar: qualidade de elite, pouca audiência

Têm IMDb ≥ 6,8 e Tomatometer ≥ 90% (com ≥ 20 críticas), mas não atingem o volume mínimo de votos ou de críticas. Ficam fora do ranking principal e servem como garimpo.

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
|  | <img src="https://image.tmdb.org/t/p/w342/wFbAxK10CiJA1XxgJaEc16UeHTb.jpg" width="46" alt=""> **Plano-Sequência dos Mortos** <br><sub>One Cut of the Dead</sub> | 2017 | **81,4** | 7,6 (37 mil) | 100% (99) | 86 | 83% | Sem oferta legal encontrada no Brasil |
|  | <img src="https://image.tmdb.org/t/p/w342/tw0i3kkmOTjDjGFZTLHKhoeXVvA.jpg" width="46" alt=""> **Exhuma** | 2024 | **80,5** | 6,9 (32 mil) | 93% (46) | 80* | 97% | Sem oferta legal encontrada no Brasil |
|  | <img src="https://image.tmdb.org/t/p/w342/mvp8wW6wm6LulWRtjjeBQcVXMBt.jpg" width="46" alt=""> **Calls** | 2021 | **79,8** | 7,7 (9 mil) | 95% (20) | 65* | 85% | Apple TV |
|  | <img src="https://image.tmdb.org/t/p/w342/rG3mGUouuSACs2KLdJWjEHpuG8L.jpg" width="46" alt=""> **Hysteria!** | 2024 | **78,0** | 7,0 (7 mil) | 92% (24) | — | 86% | HBO Max |
|  | <img src="https://image.tmdb.org/t/p/w342/wFzATr4s8totOxU8iZXXLvnhVzr.jpg" width="46" alt=""> **Sob a Sombra** <br><sub>Under the Shadow</sub> | 2016 | **77,5** | 6,8 (33 mil) | 99% (93) | 83 | 70% | Netflix · aluguel/compra: Apple TV |
|  | <img src="https://image.tmdb.org/t/p/w342/egTvGCHWMUKm9Krjb9zqnNQwSWO.jpg" width="46" alt=""> **Os Inocentes** <br><sub>The Innocents</sub> | 2021 | **77,3** | 7,0 (31 mil) | 97% (121) | 79 | 72% | aluguel/compra: Amazon, Apple TV |
|  | <img src="https://image.tmdb.org/t/p/w342/oCutmhFznao1Pzy6wM1C32kxAEu.jpg" width="46" alt=""> **Channel Zero** | 2016 | **77,3** | 7,1 (14 mil) | 93% (54) | 76 | 85% | Sem oferta legal encontrada no Brasil |
|  | <img src="https://image.tmdb.org/t/p/w342/nh4vd3KIVt2PTavs5Nj1gurnMjs.jpg" width="46" alt=""> **The Creep Tapes** | 2024 | **75,2** | 6,8 (4 mil) | 90% (26) | — | — | Reserva Imovision (canal no Prime Video) |
|  | <img src="https://image.tmdb.org/t/p/w342/105stT9GkiENXiYqvWYKoAuHKQL.jpg" width="46" alt=""> **Mad God** | 2021 | **74,2** | 6,8 (22 mil) | 92% (91) | 80 | 69% | Reserva Imovision · aluguel/compra: Reserva Imovision |
|  | <img src="https://image.tmdb.org/t/p/w342/6DU4UZTNgt77z4IJtjYv34u8Yjq.jpg" width="46" alt=""> **Sociedade dos Talentos Mortos** <br><sub>Dead Talents Society</sub> | 2024 | **73,9** | 7,0 (4 mil) | 95% (20) | — | 80% | Netflix · aluguel/compra: Amazon, Apple TV |
|  | <img src="https://image.tmdb.org/t/p/w342/5gmQ6k4NWQQ0vlZ5KXtN3iLIPT9.jpg" width="46" alt=""> **Novembro** <br><sub>November</sub> | 2017 | **73,8** | 7,1 (8 mil) | 93% (28) | 79 | 81% | Sem oferta legal encontrada no Brasil |

- **•. Plano-Sequência dos Mortos** (2017, dir./criação: Shinichiro Ueda): Uma equipe grava um terror de zumbi barato num galpão abandonado até zumbis de verdade aparecerem. Os primeiros 37 minutos são um único plano-sequência; o resto muda tudo.
- **•. Exhuma** (2024, dir./criação: Jang Jae-hyun): Dois xamãs, um geomante e um agente funerário exumam um túmulo amaldiçoado. Fenômeno de bilheteria na Coreia do Sul.
- **•. Calls** (2021, dir./criação: Fede Álvarez): Série experimental da Apple TV+: cada episódio é contado apenas pelo áudio de ligações telefônicas e por grafismos abstratos. Baseada na série francesa de Timothée Hochet.
- **•. Hysteria!** (2024, dir./criação: Matthew Scott Kane): Pânico satânico nos anos 80: adolescentes fingem ser uma banda satanista para ganhar fama, e a cidade surta. Bruce Campbell está no elenco.
- **•. Sob a Sombra** (2016, dir./criação: Babak Anvari): Teerã, anos 80, guerra Irã–Iraque: mãe e filha presas num prédio bombardeado passam a ser assombradas por um djinn.
- **•. Os Inocentes** (2021, dir./criação: Eskil Vogt): Num conjunto habitacional norueguês, crianças descobrem poderes durante as férias de verão, e a crueldade infantil vira terror puro.
- **•. Channel Zero** (2016, dir./criação: Nick Antosca): Antologia baseada em creepypastas da internet: cada temporada conta uma história fechada, com terror lento e imagens perturbadoras.
- **•. The Creep Tapes** (2024, dir./criação: Mark Duplass e Patrick Brice): Derivada dos filmes Creep: Mark Duplass volta como o serial killer que contrata cinegrafistas desavisados.
- **•. Mad God** (2021, dir./criação: Phil Tippett): Pesadelo em stop-motion que o mago dos efeitos de Star Wars e Jurassic Park levou cerca de 30 anos para concluir. Sem diálogos e sem concessões.
- **•. Sociedade dos Talentos Mortos** (2024, dir./criação: John Hsu): Comédia de terror taiwanesa: uma fantasma novata precisa ficar “famosa” assustando os vivos para não desaparecer.
- **•. Novembro** (2017, dir./criação: Rainer Sarnet): Fábula estoniana em preto e branco sobre camponeses, espíritos e criaturas feitas de sucata. Folk horror poético e estranhíssimo.

---

## 6. ⚖️ Zona cinzenta: fora por regra (transparência)

| Obra | Tipo | Onde ver | Números | Por que ficou fora |
|---|---|---|---|---|
| The Last of Us | série, 2023 | HBO Max | IMDb 8,4 (755 mil votos) · RT 94% (média das temporadas) | O IMDb não marca como Horror (Ação/Aventura/Drama). Entraria no topo das séries se a regra fosse “Horror no IMDb ou no RT”. |
| All of Us Are Dead | série, 2022 | Netflix | IMDb 7,6 (96 mil) · RT 89% | O IMDb não marca como Horror, e o RT fica abaixo de 90%. Zumbis num colégio coreano: é terror, mas falha nos dois critérios. |
| Acompanhante Perfeita (Companion) | filme, 2025 | HBO Max, Netflix | IMDb 6,9 (195 mil) · RT 93% | O IMDb classifica como Ficção científica/Suspense, sem Horror. |
| Sandman | série, 2022 | Netflix | IMDb 7,6 · RT 81% | Excluída na curadoria de gênero: é fantasia sombria, e o RT não a classifica como terror. |
| Red Rooms | filme, 2023 | Telecine (canal no Prime Video) | IMDb 7,1 · RT 96% | Excluído na curadoria de gênero: thriller psicológico de tribunal. Excelente, mas não é terror. |
| Devil in Disguise: John Wayne Gacy | minissérie, 2025 | Prime Video | IMDb 7,4 · RT 96% | Excluída na curadoria de gênero: drama de true crime. |
| O Que Fazemos nas Sombras | série, 2019–2024 | Disney+ | IMDb 8,5 · RT 96% | Excluída na curadoria de gênero: é uma sitcom com vampiros. Ótima, mas o objetivo é fazer rir, não dar medo. |
| Santa Clarita Diet | série, 2017–2019 | Netflix | IMDb 7,8 · RT 89% | Excluída na curadoria de gênero: sitcom gore com uma morta-viva, mais comédia do que terror. |
| Twin Peaks: O Retorno | série, 2017 | MUBI | IMDb 8,5 · RT 94% | Excluída na curadoria de gênero: mistério surreal de David Lynch, com momentos de terror, mas sem ser uma obra de terror. |
| Rua Cloverfield, 10 | filme, 2016 | aluguel/compra | IMDb 7,2 · RT 91% | Excluído na curadoria de gênero: thriller de confinamento; o RT não o classifica como terror. |
| Fuja (Run) | filme, 2020 | Netflix | IMDb 6,7 · RT 88% | Excluído na curadoria de gênero: thriller psicológico. |
| Tumbbad | filme, 2018 | — | IMDb 8,2 (78 mil) · RT 87% (30 críticas) | Falha no Tomatometer (abaixo de 90% para o Radar e de 85% com amostra de 40 críticas para o ranking). Clássico indiano de folk horror, vale a busca. |

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
- IMDb Non-Commercial Datasets: https://datasets.imdbws.com/ (snapshot de 27/10/2026)
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
