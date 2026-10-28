"""Busca no Wikidata o slug do Metacritic (P1712) de cada título coletado no RT."""
import json, subprocess, sys
S = sys.argv[1]
rt = json.load(open(f'{S}/data/rt.json'))
ids = ' '.join(f'"{k}"' for k in rt)
q = ('SELECT ?imdb ?mc WHERE { VALUES ?imdb { %s } ?item wdt:P345 ?imdb . '
     'OPTIONAL { ?item wdt:P1712 ?mc } }' % ids)
r = subprocess.run(['curl', '-s', '-G', 'https://query.wikidata.org/sparql', '--data-urlencode', 'query=' + q,
                    '-H', 'Accept: application/sparql-results+json', '-A', 'RankingTerror/1.0 (pesquisa pessoal)'],
                   capture_output=True).stdout
out = {}
for b in json.loads(r)['results']['bindings']:
    o = out.setdefault(b['imdb']['value'], {})
    if 'mc' in b:
        o['mc'] = b['mc']['value']
json.dump(out, open(f'{S}/data/wd.json', 'w'), indent=1)
print(len(out), sum('mc' in v for v in out.values()))
