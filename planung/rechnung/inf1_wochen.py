import json, datetime as dt
from collections import defaultdict, Counter
u=json.load(open("/home/neo/projects/schuljahr-2026-27/daten/webuntis-stundenplan-2026-27.json"))
def dd(p):
    s=str(p["date"]); return dt.date(int(s[:4]),int(s[4:6]),int(s[6:]))
def rng(a,b):
    a=dt.date.fromisoformat(a); b=dt.date.fromisoformat(b)
    return {a+dt.timedelta(d) for d in range((b-a).days+1)}
FREI=set()
for a,b in [("2026-10-26","2026-10-30"),("2026-12-23","2027-01-08"),("2027-02-04","2027-02-09"),
            ("2027-03-22","2027-04-02"),("2027-05-18","2027-05-28"),("2027-07-29","2027-09-11")]:
    FREI|=rng(a,b)
FREI|={dt.date(2027,5,6)}
BLOCK={dt.date(2026,11,18)}  # Studieninformationstag J1
WD=["Mo","Di","Mi","Do","Fr"]
inf=[p for p in u if any(s["name"]=="INF1" for s in p.get("su",[]))]
print("INF1-Slots gesamt (roh):", len(inf))
pat=Counter((WD[dd(p).weekday()], p["startTime"], p["endTime"], "/".join(r["name"] for r in p.get("ro",[]))) for p in inf)
print("Slotmuster (Tag, Beginn, Ende, Raum) -> Anzahl Termine im Jahr:")
for k,v in sorted(pat.items(), key=lambda x:(WD.index(x[0][0]),x[0][1])): print("  ",k,v)
weeks=defaultdict(list)
for p in inf:
    d=dd(p); kw=d.isocalendar()[1]; y=d.isocalendar()[0]
    st= "FERIEN" if d in FREI else ("BLOCK" if d in BLOCK else "ok")
    weeks[(y,kw)].append((d,WD[d.weekday()],p["startTime"],st))
tot=0; rows=[]
for (y,kw),lst in sorted(weeks.items()):
    mon=min(d for d,_,_,_ in lst) - dt.timedelta(days=min(d for d,_,_,_ in lst).weekday())
    n=sum(1 for x in lst if x[3]=="ok"); tot+=n
    days=" ".join(f"{w}{'' if s=='ok' else '('+s[0]+')'}" for d,w,st_,s in sorted(lst))
    hj=1 if mon<dt.date(2027,2,1) else 2
    rows.append((y,kw,mon,hj,n,days))
for y,kw,mon,hj,n,days in rows:
    print(f"HJ{hj} KW{kw:02d} {mon.strftime('%d.%m.%Y')}  {n} Std   {days}")
print("NETTO gesamt:", tot, " HJ1:", sum(r[4] for r in rows if r[3]==1), " HJ2:", sum(r[4] for r in rows if r[3]==2))
