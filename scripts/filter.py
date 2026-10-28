import gzip, csv, sys, json
S=sys.argv[1]
ratings={}
with gzip.open(f'{S}/data/title.ratings.tsv.gz','rt') as f:
    next(f)
    for line in f:
        t,r,v=line.rstrip('\n').split('\t')
        ratings[t]=(float(r),int(v))
out=[]
with gzip.open(f'{S}/data/title.basics.tsv.gz','rt',encoding='utf-8') as f:
    next(f)
    for line in f:
        p=line.rstrip('\n').split('\t')
        tconst,ttype,ptitle,otitle,adult,sy,ey,rt,genres=p
        if ttype not in ('movie','tvSeries','tvMiniSeries','tvMovie'): continue
        if 'Horror' not in genres: continue
        if sy=='\\N' or int(sy)<2016: continue
        if tconst not in ratings: continue
        r,v=ratings[tconst]
        if v<3000: continue
        out.append(dict(id=tconst,type=ttype,title=ptitle,orig=otitle,year=int(sy),end=ey,runtime=rt,genres=genres,rating=r,votes=v))
json.dump(out,open(f'{S}/data/horror_candidates.json','w'),ensure_ascii=False,indent=1)
print(len(out))
