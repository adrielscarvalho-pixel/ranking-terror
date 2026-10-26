import json,sys
S=sys.argv[1]
d={x['id']:x for x in json.load(open(f'{S}/data/horror_candidates.json'))}
rt=json.load(open(f'{S}/data/rt.json')); wd=json.load(open(f'{S}/data/wd.json'))
BAD={'tt11173328','tt20863294','tt26225038','tt35674970','tt36812904','tt14641098','tt22804760','tt29899652'} # RT match errado
def vmin(kind,y):
    if kind=='film': return {2026:5000,2025:20000}.get(y,50000)
    return {2026:5000,2025:10000}.get(y,20000)
res=[]
for k,e in rt.items():
    if k in BAD: continue
    x=d[k]; c=e.get('critics') or {}
    kind='film' if x['type'] in('movie','tvMovie') else ('mini' if x['type']=='tvMiniSeries' else 'series')
    T=int(c['score']) if c.get('score') else None; n=c.get('reviewCount') or 0
    R=x['rating']; V=x['votes']; vm=vmin(kind,x['year'])
    nmin=40 if kind=='film' else 20
    tier=None
    if T is not None and n>=nmin and V>=vm:
        if kind=='film':
            if R>=7.0 and T>=90: tier=1
            elif R>=6.5 and T>=85: tier=2
        else:
            if R>=7.5 and T>=90: tier=1
            elif R>=7.0 and T>=80: tier=2
    if tier is None and T is not None and T>=90 and n>=20 and R>=6.8 and V>=3000: tier=3
    if tier: res.append(dict(id=k,kind=kind,tier=tier,title=x['title'],year=x['year'],imdb=R,votes=V,tm=T,n=n,genre=e.get('rt_genre'),mc=wd.get(k,{}).get('mc')))
json.dump(res,open(f'{S}/data/tiers.json','w'),indent=1,ensure_ascii=False)
for r in sorted(res,key=lambda r:(r['kind'],r['tier'],-r['imdb'])):
    print(r['kind'],r['tier'],r['year'],r['title'],r['imdb'],r['votes'],r['tm'],r['n'],r['genre'],r['mc'])
