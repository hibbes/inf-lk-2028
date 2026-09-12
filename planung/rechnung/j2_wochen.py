import datetime as dt
def rng(a,b):
    a=dt.date.fromisoformat(a); b=dt.date.fromisoformat(b)
    return {a+dt.timedelta(d) for d in range((b-a).days+1)}
FREI=set()
for a,b in [("2027-11-02","2027-11-06"),("2027-12-23","2028-01-08"),("2028-02-24","2028-02-29"),  # Fastnacht: ANNAHME wie 2027 (Do-Di)
            ("2028-04-13","2028-04-22"),("2028-06-06","2028-06-17")]:
    FREI|=rng(a,b)
FREI|={dt.date(2027,11,1), dt.date(2028,5,1), dt.date(2028,5,18), dt.date(2028,5,29), dt.date(2028,6,15)}  # Allerheiligen, 1. Mai, Himmelfahrt, Pfingstmontag, Fronleichnam
ABI=rng("2028-04-25","2028-05-12")  # schriftl. Prüfung (J2 unterrichtsfrei), Wiederbeginn 15.05.
# Slotmuster wie 2026/27 (ANNAHME): Di 2, Do 2, Mi 2 in ungeraden KW
def slots(mon):
    kw=mon.isocalendar()[1]
    s=[(mon+dt.timedelta(1),2),(mon+dt.timedelta(3),2)]
    if kw%2==1: s.append((mon+dt.timedelta(2),2))
    return s
start=dt.date(2027,9,13); end=dt.date(2028,6,23)   # bis Notenschluss-Phase vor mdl. Prüfung (Annahme)
mon=start; tot=0; rows=[]
while mon<=end:
    n=sum(h for d,h in slots(mon) if d not in FREI and d not in ABI)
    phase = "J2.1" if mon<dt.date(2028,1,31) else ("J2.2" if mon<dt.date(2028,4,25) else "nach Abi")
    tot+=n; rows.append((mon,n,phase))
    mon+=dt.timedelta(7)
for mon,n,ph in rows:
    print(f"{ph:8s} KW{mon.isocalendar()[1]:02d} {mon.strftime('%d.%m.%Y')}  {n} Std")
for ph in ("J2.1","J2.2","nach Abi"):
    print(ph, sum(n for m,n,p in rows if p==ph), "Std,", sum(1 for m,n,p in rows if p==ph and n>0), "Wochen mit Unterricht")
print("GESAMT", tot)
