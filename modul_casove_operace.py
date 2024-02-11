"""
Láďa Vávra 
1.ročník MFF UK 

Zápočtový program 
ZS 2023/2024

Programování I 
NPRG030

část programu: potřebný modul časových operací 
"""
#potřebné moduly
from datetime import datetime
import subprocess

def ZjistiJestliJeCelaHodina():
    """pokud je v daný moment celá hodina, vrátí True"""
    _akt_zk_casik = datetime.now()
    return _akt_zk_casik.minute == 00 and _akt_zk_casik.second == 00

def ZjistiStringNaSekundy(__vstup__t_):
    """vrátí počet sekund spočítaný ze stringového vstupu """
    __s_cim_delam = str(__vstup__t_)
    __rok_ = __s_cim_delam[0:4]
    __mesicek_ = __s_cim_delam[4:6]
    __den__str_ = __s_cim_delam[6:8]
    __hodina_str_ = __s_cim_delam[8:10]
    __minuta_str_ = __s_cim_delam[10:12]
    #python automaticky oddělá leading zeros při převodu z stringu na int, jinak by šlo použít (0o...)
    ___casik = datetime(int(__rok_),int(__mesicek_),int(__den__str_),int(__hodina_str_),int(__minuta_str_))
    __sekundovy_cas = int(___casik.timestamp())
    return __sekundovy_cas


def ZjistiInterval(maximum = 1440, minimum = 0):
    """kontrola délky intervalu -> u minut nemá smysl dávat větší než 24 hodin (1440), menší 0. Automaticky větší než 24 zamítnu 
        lze si nastavit vlastní hodnoty
    """
    inter = input("Zadej interval: ")
    while True:
        try:
            #pokud zadán stringový řetězec místo číselné hodnoty, spadne
            if int(inter)<=  maximum:
                if int(inter) > minimum:
                    return inter
            print(f"Tvůj interval nedává s danými požadavky smysl. Vyber si nějaký v rozmezí {minimum} <-> {maximum}\nZvol si nějaký, který bude smysluplný:")
            inter = input()
        except:
            #pokud nezadal číselnou hodnotu
            print("Tvůj vstup je špatně zadaný, zadej znovu smysluplnější:")
            inter = input()  

def ZjistiJestliReaguje(__doba_cekani_na_uzivatelsky_vstup___):
    """Zadej dobu, jak dlouho má čekat, než uživatel napíše vstup"""
    x = subprocess.call(f'read -t {__doba_cekani_na_uzivatelsky_vstup___}', shell=True)
    return not x

#v budoucnu implementovatelné:
"""
def ZjistiJePrestupnyRok(rok):
    #vrátí T / F podle toho jestli je daný rok přestupný
    return (rok % 4 == 0) and ((rok % 100 != 0) or (rok % 400 == 0))

def ZjistiCisloDne( d,m,r ):
    M = [0,  31,28,31,30,31,30,  31,31,  30,31,30,31]
    for i in range(1,13):
        M[i] += M[i-1]
    if ZjistiJePrestupnyRok( r ) and m > 2:
        d += 1      
    return (r-1)*365+(r-1)//4-(r-1)//100+(r-1)//400 + M[m-1] + d

def ZjistiPocetDnuMezi(datum1, datum2):
    #zjistí počet dní mezi daty, včetně přestupných roků 
    r1,m1,d1,hodina1,minuta1 = datum1
    r2,m2,d2,hodina2,minuta2 = datum2
    return ZjistiCisloDne( d2,m2,r2 )-ZjistiCisloDne( d1,m1,r1 )

#šlo by použít, pro lepší přehlednost 
def ZjistiDatum():
    #načte rok, měsíc, den, hodina, minuta a vrátí to jako list
    #když uživatel něco pokazí, vrátí 1
    datum = []
    co_chci = ["rok","měsíc","den","hodina","minuta"]
    for i in range(5):
        try:
            print(f"Napiš mi {co_chci[i]}")
            inp = int(input())
            datum.append(inp)
        except:
            print("zadal jsi to špatně")
            return 1
    return datum

def ZjistiTedCasVratiList():
    #vrátí list ve formátu [ROK, MESIC, DEN, HODINA, MINUTA]
    rok = datetime.now().year
    mesic = datetime.now().month
    den = datetime.now().day
    hodina = datetime.now().hour
    minuta = datetime.now().minute
    vraceni_list = []
    vraceni_list.append(rok)
    vraceni_list.append(mesic)
    vraceni_list.append(den)
    vraceni_list.append(hodina)
    vraceni_list.append(minuta)
    return  vraceni_list

def ZjistiTedCasVratiString():
    "vrátí string ve formátu ROK-MESIC-DEN-HODINA-SEKUNDA"
    rok = datetime.now().year
    mesic = datetime.now().month
    den = datetime.now().day
    hodina = datetime.now().hour
    minuta = datetime.now().minute
    vratim = ""
    vratim += str(rok)
    vratim += str(mesic)
    vratim += str(den)
    vratim += str(hodina)
    vratim += str(minuta)
    return vratim
"""