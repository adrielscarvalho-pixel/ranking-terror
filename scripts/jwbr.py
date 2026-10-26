import json, sys, time, subprocess
S=sys.argv[1]
d=json.load(open(f'{S}/data/horror_candidates.json'))
ids={r['id'] for r in json.load(open(f'{S}/data/tiers.json'))}|{'tt3581920','tt14169960','tt26584495'}; cands=[x for x in d if x['id'] in ids]+[dict(id='tt3581920',title='The Last of Us',orig='The Last of Us'),dict(id='tt14169960',title='All of Us Are Dead',orig='All of Us Are Dead'),dict(id='tt26584495',title='Companion',orig='Companion')]
Q="query S($f: TitleFilter!, $c: Country!, $l: Language!) { popularTitles(country: $c, filter: $f, first: 8) { edges { node { objectType content(country: $c, language: $l) { title originalReleaseYear fullPath externalIds { imdbId } } offers(country: $c, platform: WEB) { monetizationType package { clearName } } } } } }"
try: cache=json.load(open(f'{S}/data/jwbr.json'))
except: cache={}
def post(q):
    body=json.dumps({"query":Q,"variables":{"f":{"searchQuery":q},"c":"BR","l":"pt-BR"}})
    r=subprocess.run(['curl','-s','--max-time','30','-X','POST','https://apis.justwatch.com/graphql','-H','Content-Type: application/json','-A','Mozilla/5.0','--data',body],capture_output=True).stdout
    try: return json.loads(r)
    except: return {}
for x in cands:
    if x['id'] in cache: continue
    found=None
    for q in dict.fromkeys([x['title'],x['orig']]):
        r=post(q)
        for e in (((r.get('data') or {}).get('popularTitles') or {}).get('edges') or []):
            n=e['node']
            if (n['content']['externalIds'] or {}).get('imdbId')==x['id']:
                found=n; break
        if found: break
        time.sleep(0.4)
    if found:
        offs={}
        for o in found['offers'] or []:
            offs.setdefault(o['monetizationType'],set()).add(o['package']['clearName'])
        cache[x['id']]={'pt_title':found['content']['title'],'path':found['content']['fullPath'],'offers':{k:sorted(v) for k,v in offs.items()}}
    else:
        cache[x['id']]={'pt_title':None}
    json.dump(cache,open(f'{S}/data/jwbr.json','w'),ensure_ascii=False,indent=1)
    print(x['title'],'->',cache[x['id']].get('pt_title'),cache[x['id']].get('offers',{}).get('FLATRATE'),file=sys.stderr)
    time.sleep(0.4)
