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
from datetime import datetime,timedelta
import subprocess

def ZjistiSekundyDoDalsiHodiny():
    """vrátí počet sekund do nejbližší hodiny"""
    _aktualni_cas = datetime.now()
    __dalsi_hodina = _aktualni_cas.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    return (__dalsi_hodina - _aktualni_cas).seconds

def ZjistiJestliJeCelaHodina():
    """pokud je v daný moment celá hodina, vrátí True"""
    _akt_zk_casik = datetime.now()
    return _akt_zk_casik.minute == 00 ##and _akt_zk_casik.second == 00 #můžu si dovolit díky limitu intervalu minimálně 1 minuty 

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


def ZjistiInterval(maximum = 1439, minimum = 1):
    """kontrola délky intervalu -> u minut nemá smysl dávat větší než 24 hodin (1440) –> max = 1439, menší 1. Automaticky větší než 24 zamítnu 
        lze si nastavit vlastní hodnoty
    """
    inter = input("Zadej interval: ")
    while True:
        try:
            #pokud zadán stringový řetězec místo číselné hodnoty, spadne
            if int(inter)<=  maximum:
                if int(inter) >= minimum:
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
