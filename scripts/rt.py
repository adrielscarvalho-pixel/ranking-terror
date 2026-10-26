import json, re, sys, time, subprocess, urllib.parse, html
S=sys.argv[1]
d=json.load(open(f'{S}/data/horror_candidates.json'))
cands=[x for x in d if (x['type'] in('movie','tvMovie') and x['rating']>=6.4 and x['votes']>=4000) or (x['type'] in('tvSeries','tvMiniSeries') and x['rating']>=6.8 and x['votes']>=3000)]
print(len(cands),file=sys.stderr)
try: cache=json.load(open(f'{S}/data/rt.json'))
except: cache={}
def get(url):
    return subprocess.run(['curl','-s','-L','--max-time','30','-A','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36',url],capture_output=True).stdout.decode('utf-8','ignore')
def norm(s): return re.sub(r'[^a-z0-9]','',html.unescape(s).lower())
for x in cands:
    if x['id'] in cache: continue
    tv = x['type'] in ('tvSeries','tvMiniSeries')
    res=None
    for q in dict.fromkeys([x['title'], x['orig']]):
        h=get('https://www.rottentomatoes.com/search?search='+urllib.parse.quote(q))
        sec_type='tvSeries' if tv else 'movie'
        m=re.search(r'<search-page-result[^>]*type="%s"(.*?)</search-page-result>'%sec_type,h,re.S)
        if not m: continue
        rows=re.findall(r'<search-page-media-row(.*?)</search-page-media-row>',m.group(1),re.S)
        best=None
        for r in rows:
            attr=lambda k: (re.search(k+r'="([^"]*)"',r) or [None,''])[1]
            yr=(attr('start-year') or attr('startyear')) if tv else (attr('release-year') or attr('releaseyear'))
            um=re.search(r'href="(https://www.rottentomatoes.com/[^"]+)"',r)
            nm=re.search(r'slot="title">\s*(.*?)\s*</a>',r,re.S)
            if not um or not nm: continue
            url=um.group(1); name=nm.group(1)
            try: yr=int(yr)
            except: yr=None
            ok_year = yr is not None and abs(yr-x['year'])<=1
            ok_name = norm(name)==norm(q)
            score=(ok_name*2+ok_year*3)
            if ok_year and (best is None or score>best[0]): best=(score,url,name,yr)
        if best and best[0]>=3: res=best; break
        time.sleep(0.5)
    entry={'query':x['title']}
    if res:
        entry.update(url=res[1],rt_name=html.unescape(res[2]),rt_year=res[3],exact=res[0]>=5)
        p=get(res[1])
        cs=re.search(r'"criticsScore":(\{[^}]*"title":"(?:Avg\. )?Tomatometer"\})',p)
        au=re.search(r'"audienceScore":(\{[^}]*"title":"(?:Avg\. )?Popcornmeter"\})',p)
        if cs: entry['critics']=json.loads(cs.group(1))
        if au: entry['audience']=json.loads(au.group(1))
        ms=re.search(r'"genre":\s*(\[[^\]]*\]|"[^"]*")',p)
        if ms: entry['rt_genre']=ms.group(1)
    cache[x['id']]=entry
    json.dump(cache,open(f'{S}/data/rt.json','w'),ensure_ascii=False,indent=1)
    print(x['title'],x['year'],'->',entry.get('url'),(entry.get('critics') or {}).get('score'),file=sys.stderr)
    time.sleep(0.5)
