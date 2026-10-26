# 🩸 Ranking do Terror 2021–2026: filmes, séries e minisséries

> Curadoria baseada em dados, não em achismo. Coleta feita em **25–26/out/2026**.
> As notas mudam com o tempo; os dados brutos e os scripts estão nesta pasta para refazer tudo.

**Versão visual:** abra o [`index.html`](index.html) no navegador (tem filtros e busca).

## Resumo

- **Pódio dos filmes:** Pecadores (85,6), Resident Evil (83,2), Obsessão (83,2)
- **Pódio das séries:** O Segredo de Widow's Bay (84,3), Entrevista com o Vampiro (82,7), Origem (81,9)
- **Pódio das minisséries:** A Queda da Casa de Usher (79,6), Missa da Meia-Noite (77,8), Carrie, a Estranha (77,8)

---

## 1. Método

### 1.1 Universo analisado (sem escolher a dedo)
1. Usei a base **oficial e completa do IMDb** (`title.basics` + `title.ratings`, datasets.imdbws.com, atualizada em 25/10/2026).
2. Filtrei **todo** título com gênero **Horror** e ano de estreia **≥ 2021**, nos tipos filme, série e minissérie: **736 obras** com ao menos 3 mil votos.
3. Para os **169** com nota competitiva (filmes ≥ 6,4 e séries ≥ 6,8), busquei automaticamente a página no **Rotten Tomatoes** (Tomatometer, nº de críticas, média e Popcornmeter) e a disponibilidade no **JustWatch Brasil**.
4. Para os finalistas, coletei o **Metascore** direto no Metacritic.

### 1.2 Portas de entrada (corte obrigatório)

| | **Elite** (corte principal) | **Também recomendados** |
|---|---|---|
| **Filmes** | IMDb ≥ 7,0 **e** Tomatometer ≥ 90% | IMDb ≥ 6,5 **e** Tomatometer ≥ 85% |
| **Séries / minisséries** | IMDb ≥ 7,5 **e** Tomatometer ≥ 90% | IMDb ≥ 7,0 **e** Tomatometer ≥ 80% |

**Relevância mínima** (votos no IMDb, proporcional ao tempo de mercado):

| Ano de estreia | Filmes | Séries/minisséries |
|---|---:|---:|
| 2021–2024 | 50 mil | 20 mil |
| 2025 | 20 mil | 10 mil |
| 2026 | 5 mil | 5 mil |

Também exijo amostra crítica mínima: ≥ 40 críticas no RT para filmes e ≥ 20 para séries.

### 1.3 Só terror de verdade
- **Filtro 1:** gênero Horror no IMDb (requisito obrigatório).
- **Filtro 2:** checagem com a classificação de gênero do Rotten Tomatoes. Se o RT não marca Horror, decide a curadoria, sempre pela premissa central:
  - **excluídos:** Sandman (fantasia), Red Rooms (thriller de tribunal) e Devil in Disguise (true crime);
  - **mantidos, com justificativa:** Yellowjackets e Alien: Earth.

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
Dados do **JustWatch Brasil** coletados em 25–26/out/2026.
- “Assinatura” inclui planos com anúncios.
- “Canal no Prime Video” significa assinatura adicional dentro da Amazon.
- Catálogos mudam toda semana: confira antes de assinar.

---

## 2. 🎬 Filmes

### Elite: IMDb ≥ 7,0 e RT ≥ 90%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 1 | **Pecadores** <br><sub>Sinners</sub> | 2025 | **85,6** | 7,5 (536 mil) | 97% (441) | 84 | 96% | HBO Max, Netflix · aluguel/compra: Amazon, Apple TV |
| 2 | **Resident Evil** | 2026 | **83,2** | 7,6 (115 mil) | 96% (302) | 79 | 90% | em cartaz nos cinemas |
| 3 | **Obsessão** <br><sub>Obsession</sub> | 2025 | **83,2** | 7,8 (410 mil) | 93% (329) | 77 | 94% | em cartaz nos cinemas; aluguel/compra: Amazon, Apple TV |
| 4 | **A Hora do Mal** <br><sub>Weapons</sub> | 2025 | **81,8** | 7,4 (415 mil) | 93% (400) | 81 | 85% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 5 | **Extermínio: O Templo dos Ossos** <br><sub>28 Years Later: The Bone Temple</sub> | 2026 | **81,0** | 7,2 (133 mil) | 91% (351) | 81 | 88% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 6 | **Desconhecidos** <br><sub>Strange Darling</sub> | 2023 | **79,8** | 7,0 (73 mil) | 96% (164) | 80 | 85% | Telecine (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 7 | **Fale Comigo** <br><sub>Talk to Me</sub> | 2022 | **79,6** | 7,1 (229 mil) | 94% (300) | 76 | 83% | Prime Video, HBO Max, Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 8 | **Pearl: Uma História de Origem 'X'** <br><sub>Pearl</sub> | 2022 | **78,8** | 7,0 (167 mil) | 93% (218) | 76 | 83% | aluguel/compra: Amazon, Apple TV |
| 9 | **Entrevista com o Demônio** <br><sub>Late Night with the Devil</sub> | 2023 | **78,6** | 7,0 (154 mil) | 97% (239) | 72 | 82% | HBO Max, Netflix, Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 10 | **A Meia-Irmã Feia** <br><sub>The Ugly Stepsister</sub> | 2025 | **77,8** | 7,0 (50 mil) | 96% (141) | 70 | 85% | MUBI · em cartaz nos cinemas; aluguel/compra: Apple TV |
| 11 | **O Predador: A Caçada** <br><sub>Prey</sub> | 2022 | **77,2** | 7,1 (279 mil) | 94% (289) | 71 | 74% | Disney+ |
| 12 | **Noites Brutais** <br><sub>Barbarian</sub> | 2022 | **77,0** | 7,0 (279 mil) | 92% (212) | 78 | 70% | Paramount+, Telecine (canal no Prime Video), Universal+ (canal no Prime Video) |

### Também recomendados: IMDb ≥ 6,5 e RT ≥ 85%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 13 | **Frankenstein** | 2025 | **80,3** | 7,4 (343 mil) | 85% (383) | 78 | 94% | Netflix |
| 14 | **Acampamento Miasma: Adolescência, Sexo e Morte** <br><sub>Teenage Sex and Death at Camp Miasma</sub> | 2026 | **79,4** | 6,5 (24 mil) | 94% (278) | 89 | 78% | MUBI · aluguel/compra: Amazon, Apple TV |
| 15 | **A Substância** <br><sub>The Substance</sub> | 2024 | **78,2** | 7,2 (472 mil) | 89% (380) | 78 | 76% | MUBI, Netflix · aluguel/compra: Amazon, Apple TV |
| 16 | **Oddity: Objetos Obscuros** <br><sub>Oddity</sub> | 2024 | **78,2** | 6,7 (64 mil) | 96% (133) | 78 | 85% | Telecine (canal no Prime Video) · aluguel/compra: Amazon |
| 17 | **Socorro!** <br><sub>Send Help</sub> | 2026 | **78,1** | 6,7 (161 mil) | 92% (303) | 75 | 86% | Disney+ |
| 18 | **O Mal que Nos Habita** <br><sub>When Evil Lurks</sub> | 2023 | **77,8** | 6,9 (65 mil) | 96% (122) | 75 | 84% | Netflix · aluguel/compra: Apple TV |
| 19 | **Premonição 6: Laços de Sangue** <br><sub>Final Destination: Bloodlines</sub> | 2025 | **77,5** | 6,7 (174 mil) | 92% (235) | 73 | 86% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 20 | **X: A Marca da Morte** <br><sub>X</sub> | 2022 | **77,3** | 6,5 (231 mil) | 94% (229) | 80 | 76% | MGM+ (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 21 | **Faça Ela Voltar** <br><sub>Bring Her Back</sub> | 2025 | **77,2** | 7,1 (144 mil) | 89% (272) | 75 | 79% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 22 | **Hokum: O Pesadelo da Bruxa** <br><sub>Hokum</sub> | 2026 | **76,4** | 6,6 (73 mil) | 90% (209) | 76 | 82% | Prime Video · aluguel/compra: Amazon, Apple TV |
| 23 | **Nosferatu** | 2024 | **76,3** | 7,1 (281 mil) | 85% (385) | 78 | 73% | Netflix · aluguel/compra: Amazon, Apple TV |
| 24 | **Exit 8** | 2025 | **76,0** | 6,5 (37 mil) | 92% (177) | 71 | 86% | Paramount+ · aluguel/compra: Amazon, Apple TV |
| 25 | **O Menu** <br><sub>The Menu</sub> | 2022 | **76,0** | 7,1 (521 mil) | 88% (338) | 71 | 76% | Disney+ |
| 26 | **Herege** <br><sub>Heretic</sub> | 2024 | **75,9** | 7,0 (243 mil) | 89% (295) | 71 | 76% | Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 27 | **A Longa Marcha: Caminhe ou Morra** <br><sub>The Long Walk</sub> | 2025 | **75,6** | 6,6 (154 mil) | 88% (296) | 71 | 85% | Telecine (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 28 | **Juntos** <br><sub>Together</sub> | 2025 | **75,4** | 6,7 (91 mil) | 89% (246) | 75 | 75% | Prime Video · aluguel/compra: Amazon, Apple TV |
| 29 | **Backrooms: Um Não-Lugar** <br><sub>Backrooms</sub> | 2026 | **74,9** | 6,7 (236 mil) | 86% (316) | 76 | 74% | em cartaz nos cinemas; aluguel/compra: Amazon, Apple TV |
| 30 | **Extermínio: A Evolução** <br><sub>28 Years Later</sub> | 2025 | **73,9** | 6,6 (231 mil) | 88% (399) | 77 | 63% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 31 | **Sorria 2** <br><sub>Smile 2</sub> | 2024 | **73,9** | 6,7 (157 mil) | 86% (212) | 67 | 81% | Paramount+ · aluguel/compra: Amazon, Apple TV |
| 32 | **O Monstro do Meu Quarto** <br><sub>Dust Bunny</sub> | 2025 | **73,0** | 6,5 (22 mil) | 85% (117) | 73 | 82% | Sem oferta legal encontrada no Brasil |
| 33 | **Rua do Medo: 1666 – Parte 3** <br><sub>Fear Street: Part Three - 1666</sub> | 2021 | **72,8** | 6,6 (78 mil) | 89% (100) | 68 | 75% | Netflix |
| 34 | **A Morte do Demônio: A Ascensão** <br><sub>Evil Dead Rise</sub> | 2023 | **72,7** | 6,5 (180 mil) | 85% (242) | 69 | 76% | HBO Max · aluguel/compra: Amazon, Apple TV |
| 35 | **Rua do Medo: 1978 - Parte 2** <br><sub>Fear Street: Part Two - 1978</sub> | 2021 | **72,7** | 6,7 (93 mil) | 88% (110) | 61 | 81% | Netflix |
| 36 | **Buddy** | 2026 | **72,6** | 6,7 (18 mil) | 88% (138) | 67 | 76% | Sem oferta legal encontrada no Brasil |
| 37 | **Longlegs - Vínculo Mortal** <br><sub>Longlegs</sub> | 2024 | **72,4** | 6,5 (235 mil) | 85% (323) | 77 | 61% | Diamond Films (canal no Prime Video) · aluguel/compra: Amazon, Apple TV |
| 38 | **Dezesseis Facadas** <br><sub>Totally Killer</sub> | 2023 | **70,8** | 6,5 (71 mil) | 85% (110) | 62 | 76% | Prime Video |

<sub>* Metascore com menos de 10 críticas: exibido, mas fora do cálculo.</sub>

#### Por que cada filme está aqui
- **1. Pecadores** (2025, dir./criação: Ryan Coogler): Gêmeos (Michael B. Jordan, em papel duplo) abrem um juke joint no Mississippi de 1932 e atraem vampiros. Blues, folclore e história americana num só corpo. Recorde histórico de 16 indicações ao Oscar.
- **2. Resident Evil** (2026, dir./criação: Zach Cregger): A franquia recomeça do zero: um entregador de material médico (Austin Abrams) atravessa uma noite de surto em Raccoon City. Teve a melhor estreia da série nos EUA (US$ 60 milhões).
- **3. Obsessão** (2025, dir./criação: Curry Barker): Um rapaz quebra o “Salgueiro dos Desejos” para conquistar a garota que ama, e o desejo cobra um preço. A estreia em longa de Curry Barker virou fenômeno: são mais de 400 mil votos no IMDb.
- **4. A Hora do Mal** (2025, dir./criação: Zach Cregger): Dezessete crianças da mesma turma saem de casa às 2h17 da madrugada e desaparecem. O mistério é contado em capítulos por pontos de vista diferentes. Amy Madigan ganhou o Oscar de atriz coadjuvante como Tia Gladys.
- **5. Extermínio: O Templo dos Ossos** (2026, dir./criação: Nia DaCosta): Continuação direta de Extermínio: A Evolução. Ralph Fiennes (Dr. Kelson) e Jack O’Connell (o culto de Sir Jimmy Crystal) dominam o capítulo mais sombrio da saga.
- **6. Desconhecidos** (2023, dir./criação: JT Mollner): Um encontro casual vira caçada, contado em seis capítulos fora de ordem que brincam com as expectativas do slasher. Rodado em 35 mm, com fotografia de Giovanni Ribisi.
- **7. Fale Comigo** (2022, dir./criação: Danny e Michael Philippou): Adolescentes australianos usam uma mão embalsamada para “receber” espíritos por 90 segundos, até alguém passar do tempo. A estreia que transformou os irmãos Philippou em grife.
- **8. Pearl: Uma História de Origem 'X'** (2022, dir./criação: Ti West): Prelúdio de X, ambientado em 1918: Mia Goth vive uma jovem de fazenda que sonha com o estrelato e explode em violência. O monólogo final é antológico.
- **9. Entrevista com o Demônio** (2023, dir./criação: Cameron e Colin Cairnes): Halloween de 1977: um apresentador de talk show em crise de audiência leva uma garota “possuída” ao vivo. Falso found footage de época, com David Dastmalchian em grande forma.
- **10. A Meia-Irmã Feia** (2025, dir./criação: Emilie Blichfeldt): Cinderela vista pela meia-irmã que se mutila para caber no padrão de beleza. Body horror norueguês, cruel e muito engraçado.
- **11. O Predador: A Caçada** (2022, dir./criação: Dan Trachtenberg): O Predador chega às Grandes Planícies de 1719. Amber Midthunder vive Naru, jovem comanche que quer provar seu valor como caçadora. Simples, físico e tenso.
- **12. Noites Brutais** (2022, dir./criação: Zach Cregger): Uma mulher reserva um Airbnb em Detroit e descobre que ele já está ocupado por um estranho. O porão esconde muito mais, e a virada no meio do filme é das mais comentadas do terror recente.
- **13. Frankenstein** (2025, dir./criação: Guillermo del Toro): O projeto de uma vida de del Toro: Oscar Isaac é Victor e Jacob Elordi é a Criatura. Mais tragédia gótica do que susto, com design de produção suntuoso.
- **14. Acampamento Miasma: Adolescência, Sexo e Morte** (2026, dir./criação: Jane Schoenbrun): Uma jovem diretora (Hannah Einbinder) é contratada para reviver uma franquia slasher e fica obcecada pela final girl original (Gillian Anderson). Metaterror queer.
- **15. A Substância** (2024, dir./criação: Coralie Fargeat): Uma estrela decadente (Demi Moore) usa uma droga que cria uma versão mais jovem de si mesma (Margaret Qualley). Body horror satírico sobre etarismo e Hollywood.
- **16. Oddity: Objetos Obscuros** (2024, dir./criação: Damian McCarthy): Uma vidente cega investiga a morte da irmã gêmea e leva um boneco de madeira assustador para a casa do viúvo. Terror irlandês de casa isolada, de precisão cirúrgica.
- **17. Socorro!** (2026, dir./criação: Sam Raimi): Raimi volta ao terror: uma funcionária maltratada (Rachel McAdams) e o chefe (Dylan O’Brien) sobrevivem a um acidente aéreo numa ilha, e a hierarquia vira de cabeça para baixo.
- **18. O Mal que Nos Habita** (2023, dir./criação: Demián Rugna): No interior da Argentina, dois irmãos tentam se livrar de um “apodrecido” (um possuído) e acabam espalhando o mal. Um dos filmes de possessão mais cruéis do século.
- **19. Premonição 6: Laços de Sangue** (2025, dir./criação: Zach Lipovsky e Adam Stein): Uma universitária tem visões do desastre que a avó evitou em 1968, e a Morte vem cobrar a família inteira. A franquia renasce, com a última aparição de Tony Todd.
- **20. X: A Marca da Morte** (2022, dir./criação: Ti West): Texas, 1979: uma equipe filma um pornô numa fazenda e vira presa do casal de idosos donos do lugar. Mia Goth faz papel duplo.
- **21. Faça Ela Voltar** (2025, dir./criação: Danny e Michael Philippou): Dois irmãos vão morar com uma mãe adotiva acolhedora (Sally Hawkins), cujo luto esconde um ritual. É o filme mais brutal e mais triste dos Philippou.
- **22. Hokum: O Pesadelo da Bruxa** (2026, dir./criação: Damian McCarthy): Um romancista (Adam Scott) vai a uma pousada irlandesa para espalhar as cinzas dos pais. A suíte de lua de mel fica sempre trancada, porque guarda uma bruxa.
- **23. Nosferatu** (2024, dir./criação: Robert Eggers): Releitura do clássico de 1922, com Lily-Rose Depp como Ellen e Bill Skarsgård irreconhecível como o Conde Orlok. Terror gótico de textura impressionante.
- **24. Exit 8** (2025, dir./criação: Genki Kawamura): Adaptação do game japonês: um homem (Kazunari Ninomiya) fica preso num corredor de metrô em looping e precisa detectar anomalias para escapar.
- **25. O Menu** (2022, dir./criação: Mark Mylod): Um casal janta num restaurante exclusivo numa ilha, e o chef (Ralph Fiennes) preparou um menu de vingança. Sátira de terror sobre gastronomia e classe social.
- **26. Herege** (2024, dir./criação: Scott Beck e Bryan Woods): Duas missionárias mórmons batem à porta do Sr. Reed (Hugh Grant), que quer debater religião e não deixa ninguém sair. Hugh Grant num de seus melhores papéis.
- **27. A Longa Marcha: Caminhe ou Morra** (2025, dir./criação: Francis Lawrence): Adaptação de Stephen King (como Richard Bachman): 50 jovens caminham sem parar, e quem fica abaixo da velocidade mínima é executado. Terror de resistência física e moral.
- **28. Juntos** (2025, dir./criação: Michael Shanks): Dave Franco e Alison Brie, casados na vida real, vivem um casal cujos corpos começam a se fundir literalmente. Body horror sobre codependência.
- **29. Backrooms: Um Não-Lugar** (2026, dir./criação: Kane Parsons): O criador da websérie viral estreia pela A24 como o diretor mais jovem da história do estúdio. O dono de uma loja de móveis (Chiwetel Ejiofor) encontra uma passagem para um labirinto infinito de salas amarelas.
- **30. Extermínio: A Evolução** (2025, dir./criação: Danny Boyle): Boyle e Alex Garland retornam: um garoto (Alfie Williams) deixa pela primeira vez a ilha isolada rumo ao continente infestado. É ousado, estranho e emotivo.
- **31. Sorria 2** (2024, dir./criação: Parker Finn): A maldição do sorriso contamina uma pop star (Naomi Scott) às vésperas da turnê de retorno. É maior, mais estilosa e mais cruel que o original.
- **32. O Monstro do Meu Quarto** (2025, dir./criação: Bryan Fuller): Estreia de Bryan Fuller (Hannibal) na direção de longas: uma menina contrata o vizinho matador de aluguel (Mads Mikkelsen) para eliminar o monstro debaixo da cama.
- **33. Rua do Medo: 1666 – Parte 3** (2021, dir./criação: Leigh Janiak): Fecho da trilogia: a origem da maldição de Sarah Fier na colônia de 1666 e o acerto de contas em 1994.
- **34. A Morte do Demônio: A Ascensão** (2023, dir./criação: Lee Cronin): Os deadites invadem um prédio de apartamentos em Los Angeles: uma mãe possuída contra os próprios filhos. Um banho de sangue fiel à franquia.
- **35. Rua do Medo: 1978 - Parte 2** (2021, dir./criação: Leigh Janiak): Segunda parte da trilogia Rua do Medo: um massacre no acampamento Nightwing, em homenagem declarada ao slasher de acampamento.
- **36. Buddy** (2026, dir./criação: Casper Kelly): Do criador de “Too Many Cooks”: crianças ficam presas num programa infantil ao estilo anos 90, com um unicórnio apresentador nada amigável. Elenco com Cristin Milioti e Michael Shannon.
- **37. Longlegs - Vínculo Mortal** (2024, dir./criação: Osgood Perkins): Uma agente do FBI (Maika Monroe) caça um assassino satânico (Nicolas Cage). A atmosfera é sufocante, e o marketing virou fenômeno à parte.
- **38. Dezesseis Facadas** (2023, dir./criação: Nahnatchka Khan): Uma adolescente volta no tempo até 1987 para impedir o primeiro crime de um serial killer. Comédia de terror no espírito de “De Volta para o Futuro” encontra “Pânico”.

---

## 3. 📺 Séries

### Elite: IMDb ≥ 7,5 e RT ≥ 90%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 1 | **O Segredo de Widow's Bay** <br><sub>Widow's Bay</sub> | 2026 | **84,3** | 8,1 (99 mil) | 98% (109) | 78 | 92% | Apple TV |
| 2 | **Entrevista com o Vampiro** <br><sub>Interview with the Vampire</sub> | 2022 | **82,7** | 7,6 (46 mil) | 99% (105) | 83 | 79% | Prime Video, Netflix |
| 3 | **Origem** <br><sub>From</sub> | 2022 | **81,9** | 7,7 (212 mil) | 96% (67) | 63* | 76% | Globoplay |
| 4 | **Yellowjackets** | 2021 | **77,9** | 7,7 (118 mil) | 92% (202) | 74 | 65% | Paramount+ |

### Também recomendadas: IMDb ≥ 7,0 e RT ≥ 80%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 5 | **Alien: Earth** | 2025 | **78,2** | 7,1 (111 mil) | 94% (122) | 85 | 65% | Disney+ |
| 6 | **Chucky** | 2021 | **77,1** | 7,2 (34 mil) | 95% (64) | 70 | 82% | Disney+, Prime Video, Universal+ (canal no Prime Video) |
| 7 | **O Gabinete de Curiosidades de Guillermo del Toro** <br><sub>Guillermo del Toro's Cabinet of Curiosities</sub> | 2022 | **74,9** | 7,0 (66 mil) | 93% (56) | 72 | 72% | Netflix |
| 8 | **IT: Bem-Vindos a Derry** <br><sub>It: Welcome to Derry</sub> | 2025 | **74,8** | 7,9 (122 mil) | 81% (98) | 61 | 82% | HBO Max · aluguel/compra: Amazon |
| 9 | **Arquivo 81** <br><sub>Archive 81</sub> | 2022 | **74,5** | 7,3 (70 mil) | 87% (39) | 73 | 75% | Netflix |

<sub>* Metascore com menos de 10 críticas (From tem 63 com apenas 7): exibido, mas fora do cálculo.</sub>

#### Por que cada série está aqui
- **1. O Segredo de Widow's Bay** (2026, dir./criação: Katie Dippold): O prefeito (Matthew Rhys) de uma ilha amaldiçoada da Nova Inglaterra quer transformá-la em destino turístico. Terror-comédia que não economiza nos sustos de verdade.
- **2. Entrevista com o Vampiro** (2022, dir./criação: Rolin Jones): Louis (Jacob Anderson) conta sua vida ao lado de Lestat (Sam Reid) a um jornalista. A adaptação mais aclamada do universo de Anne Rice.
- **3. Origem** (2022, dir./criação: John Griffin): Uma cidadezinha de onde ninguém consegue sair. À noite, criaturas com rosto humano batem à porta pedindo para entrar. Harold Perrineau lidera o elenco.
- **4. Yellowjackets** (2021, dir./criação: Ashley Lyle e Bart Nickerson): Um time feminino de futebol cai nos ermos do Canadá em 1996. Vinte e cinco anos depois, as sobreviventes escondem o que fizeram para viver. Sobrevivência, canibalismo e algo sobrenatural. _Nota de curadoria: O RT classifica como Drama/Suspense, mas há canibalismo, sobrevivência e uma entidade sobrenatural no centro: mantida._
- **5. Alien: Earth** (2025, dir./criação: Noah Hawley): O xenomorfo chega à Terra de 2120: híbridos sintéticos com mentes de crianças enfrentam a carga de uma nave que caiu. Ficção científica de terror ambiciosa. _Nota de curadoria: O RT classifica como Drama/Ficção científica, mas é o xenomorfo de Alien, cânone do sci-fi horror: mantida._
- **6. Chucky** (2021, dir./criação: Don Mancini): O criador do Brinquedo Assassino leva Chucky para a TV, com Jennifer Tilly e Brad Dourif. É mais ousada e mais queer do que os filmes.
- **7. O Gabinete de Curiosidades de Guillermo del Toro** (2022, dir./criação: Guillermo del Toro (curador)): Antologia de oito contos escolhidos por del Toro, com direção de nomes como Panos Cosmatos, Jennifer Kent e Ana Lily Amirpour.
- **8. IT: Bem-Vindos a Derry** (2025, dir./criação: Andy e Barbara Muschietti): Prelúdio de IT ambientado em 1962: a Derry dos anos 60 e a origem de Pennywise (Bill Skarsgård).
- **9. Arquivo 81** (2022, dir./criação: Rebecca Sonnenshine): Um arquivista (Mamoudou Athie) restaura fitas de uma documentarista desaparecida em 1994 e descobre um culto. Foi cancelada após uma temporada, mas está completa como história.

---

## 4. 🕯️ Minisséries

### Elite: IMDb ≥ 7,5 e RT ≥ 90%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 1 | **A Queda da Casa de Usher** <br><sub>The Fall of the House of Usher</sub> | 2023 | **79,6** | 7,9 (140 mil) | 91% (114) | 73 | 81% | Netflix |

### Também recomendadas: IMDb ≥ 7,0 e RT ≥ 80%

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
| 2 | **Missa da Meia-Noite** <br><sub>Midnight Mass</sub> | 2021 | **77,8** | 7,7 (177 mil) | 87% (102) | 75 | 79% | Netflix |
| 3 | **Carrie, a Estranha** <br><sub>Carrie</sub> | 2026 | **77,8** | 7,9 (47 mil) | 85% (133) | 71 | 82% | Prime Video |
| 4 | **The Walking Dead: The Ones Who Live** | 2024 | **73,7** | 7,7 (52 mil) | 88% (30) | 61 | 76% | Prime Video |


#### Por que cada minissérie está aqui
- **1. A Queda da Casa de Usher** (2023, dir./criação: Mike Flanagan): Flanagan funde vários contos de Poe numa dinastia farmacêutica: os herdeiros de Roderick Usher morrem um a um. Elegante, venenosa e muito divertida.
- **2. Missa da Meia-Noite** (2021, dir./criação: Mike Flanagan): Um padre carismático chega a uma ilha pesqueira decadente, e milagres começam a acontecer. Terror religioso sobre fé, vício e culpa. Para muitos, é a obra-prima de Flanagan.
- **3. Carrie, a Estranha** (2026, dir./criação: Mike Flanagan): Flanagan reimagina Stephen King em 8 episódios: Summer H. Howell é Carrie White e Samantha Sloyan é a mãe fanática. Stephen King chamou a série de “brilhante”.
- **4. The Walking Dead: The Ones Who Live** (2024, dir./criação: Scott M. Gimple): Seis episódios para reunir Rick Grimes (Andrew Lincoln) e Michonne (Danai Gurira). É o fecho emocional do arco do casal no universo The Walking Dead.

> Poucas minisséries de terror lançadas desde 2021 passam nos cortes; a lista curta é resultado do método, não falta de busca.

---

## 5. 📡 Radar: qualidade de elite, pouca audiência

Têm IMDb ≥ 6,8 e Tomatometer ≥ 90% (com ≥ 20 críticas), mas não atingem o volume mínimo de votos ou de críticas. Ficam fora do ranking principal e servem como garimpo.

| # | Título | Ano | Índice | IMDb (votos) | Tomatometer (críticas) | Metascore | Popcornmeter | Onde ver no Brasil |
|---:|---|---:|---:|---|---|---:|---:|---|
|  | **Exhuma** | 2024 | **80,5** | 6,9 (32 mil) | 93% (46) | 80* | 97% | Sem oferta legal encontrada no Brasil |
|  | **Calls** | 2021 | **79,8** | 7,7 (9 mil) | 95% (20) | 65* | 85% | Apple TV |
|  | **Hysteria!** | 2024 | **78,0** | 7,0 (7 mil) | 92% (24) | — | 86% | HBO Max |
|  | **Os Inocentes** <br><sub>The Innocents</sub> | 2021 | **77,3** | 7,0 (31 mil) | 97% (121) | 79 | 72% | aluguel/compra: Amazon, Apple TV |
|  | **The Creep Tapes** | 2024 | **75,2** | 6,8 (4 mil) | 90% (26) | — | — | Reserva Imovision (canal no Prime Video) |
|  | **Mad God** | 2021 | **74,2** | 6,8 (22 mil) | 92% (91) | 80 | 69% | Reserva Imovision · aluguel/compra: Reserva Imovision |
|  | **Sociedade dos Talentos Mortos** <br><sub>Dead Talents Society</sub> | 2024 | **73,9** | 7,0 (4 mil) | 95% (20) | — | 80% | Netflix · aluguel/compra: Amazon, Apple TV |

- **•. Exhuma** (2024, dir./criação: Jang Jae-hyun): Dois xamãs, um geomante e um agente funerário exumam um túmulo amaldiçoado. Fenômeno de bilheteria na Coreia do Sul.
- **•. Calls** (2021, dir./criação: Fede Álvarez): Série experimental da Apple TV+: cada episódio é contado apenas pelo áudio de ligações telefônicas e por grafismos abstratos. Baseada na série francesa de Timothée Hochet.
- **•. Hysteria!** (2024, dir./criação: Matthew Scott Kane): Pânico satânico nos anos 80: adolescentes fingem ser uma banda satanista para ganhar fama, e a cidade surta. Bruce Campbell está no elenco.
- **•. Os Inocentes** (2021, dir./criação: Eskil Vogt): Num conjunto habitacional norueguês, crianças descobrem poderes durante as férias de verão, e a crueldade infantil vira terror puro.
- **•. The Creep Tapes** (2024, dir./criação: Mark Duplass e Patrick Brice): Derivada dos filmes Creep: Mark Duplass volta como o serial killer que contrata cinegrafistas desavisados.
- **•. Mad God** (2021, dir./criação: Phil Tippett): Pesadelo em stop-motion que o mago dos efeitos de Star Wars e Jurassic Park levou cerca de 30 anos para concluir. Sem diálogos e sem concessões.
- **•. Sociedade dos Talentos Mortos** (2024, dir./criação: John Hsu): Comédia de terror taiwanesa: uma fantasma novata precisa ficar “famosa” assustando os vivos para não desaparecer.

---

## 6. ⚖️ Zona cinzenta: fora por regra (transparência)

| Obra | Tipo | Onde ver | Números | Por que ficou fora |
|---|---|---|---|---|
| The Last of Us | série, 2023 | HBO Max | IMDb 8,4 (755 mil votos) · RT 94% (média das temporadas) | O IMDb não marca como Horror (Ação/Aventura/Drama). Entraria no topo das séries se a regra fosse “Horror no IMDb ou no RT”. |
| All of Us Are Dead | série, 2022 | Netflix | IMDb 7,6 (96 mil) · RT 89% | O IMDb não marca como Horror, e o RT fica abaixo de 90%. Zumbis num colégio coreano: é terror, mas falha nos dois critérios. |
| Acompanhante Perfeita (Companion) | filme, 2025 | HBO Max, Netflix | IMDb 6,9 (195 mil) · RT 93% | O IMDb classifica como Ficção científica/Suspense, sem Horror. |
| Stranger Things | série, 2016–2025 | Netflix | RT 90% | Estreou antes de 2021. A regra vale pela data de estreia da obra, não da temporada. |
| Sandman | série, 2022 | Netflix | IMDb 7,6 · RT 81% | Excluída na curadoria de gênero: é fantasia sombria, e o RT não a classifica como terror. |
| Red Rooms | filme, 2023 | Telecine (canal no Prime Video) | IMDb 7,1 · RT 96% | Excluído na curadoria de gênero: thriller psicológico de tribunal. Excelente, mas não é terror. |
| Devil in Disguise: John Wayne Gacy | minissérie, 2025 | Prime Video | IMDb 7,4 · RT 96% | Excluída na curadoria de gênero: drama de true crime. |

Quase entraram nos filmes (falharam por pouco no Tomatometer ou no IMDb):
- O Telefone Negro (6,9 / 81%)
- Não! Não Olhe! (6,8 / 83%)
- Alien: Romulus (7,1 / 80%)
- Sorria (6,5 / 79%)
- A Noite Passada em Soho (7,0 / 75%)
- Cara-de-Barro (7,6 / 75%)
- Exhuma (6,9 / 93%, mas só 32 mil votos; está no Radar)

---

## 7. Fontes
- IMDb Non-Commercial Datasets: https://datasets.imdbws.com/ (snapshot de 25/10/2026)
- Rotten Tomatoes: páginas de cada título (links em `dados/ranking.json`)
- Metacritic: páginas de cada título; o slug foi obtido via Wikidata (propriedade P1712)
- JustWatch Brasil: API pública do site (país BR, idioma pt-BR)
- Fatos citados nas notas:
  - 16 indicações de *Pecadores* ao Oscar; Oscar de Amy Madigan por *A Hora do Mal*: [TheWrap](https://www.thewrap.com/industry-news/awards/oscar-nominations-records-milestones-2026/), [Variety](https://au.variety.com/2026/film/news/amy-madigan-best-supporting-actress-oscar-34250)
  - Bilheteria de *Resident Evil*: [CTV/AP](https://www.ctvnews.ca/entertainment/article/box-office-resident-evil-tops-box-office-with-franchise-best-debut-of-us60-million/)

## 8. Reproduzir
```bash
cd ranking-terror/scripts
# 1) baixe a base do IMDb e filtre terror 2021+
mkdir -p <pasta>/data && cd <pasta>/data && curl -O https://datasets.imdbws.com/title.basics.tsv.gz -O https://datasets.imdbws.com/title.ratings.tsv.gz && cd -
python3 filter.py <pasta>
# 2) coleta RT, JustWatch e monta as faixas
python3 rt.py <pasta>; python3 tiers.py <pasta>; python3 jwbr.py <pasta>
# (Metascores: coletados página a página e salvos em <pasta>/data/mc.json)
# 3) gera ranking.json, README.md e index.html
python3 build.py <pasta> ..
```
Os dados brutos usados nesta versão estão em `dados/brutos/`.
