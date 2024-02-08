"""
Láďa Vávra 
1.ročník MFF UK 

Zápočtový program 
ZS 2023/2024

Programování I 
NPRG030

část programu: potřebný modul
"""

from datetime import datetime
import threading #pro více vláken
import queue #pro předávání informací mezi vlákny
import time

def ZjistiDatumNaLinux(rok,mesic,den,hodina,minuta):
    """vrátí linuxový čas v daný okamžik"""
    cas1 = datetime(rok,mesic,den,hodina,minuta)
    linux_cas = int(cas1.timestamp())
    return linux_cas


def ZjistiJePrestupnyRok(rok):
    """vrátí T / F podle toho jestli je daný rok přestupný """
    return (rok % 4 == 0) and ((rok % 100 != 0) or (rok % 400 == 0))

def ZjistiCisloDne( d,m,r ):
    M = [0,  31,28,31,30,31,30,  31,31,  30,31,30,31]
    for i in range(1,13):
        M[i] += M[i-1]
    if ZjistiJePrestupnyRok( r ) and m > 2:
        d += 1      
    return (r-1)*365+(r-1)//4-(r-1)//100+(r-1)//400 + M[m-1] + d

def ZjistiPocetDnuMezi(datum1, datum2):
    """vezme si jen den, měsíc a rok a hodiny a minuty jsou mu jedno,
      zjistí počet dní mezi daty"""
    r1,m1,d1,hodina1,minuta1 = datum1
    r2,m2,d2,hodina2,minuta2 = datum2
    return ZjistiCisloDne( d2,m2,r2 )-ZjistiCisloDne( d1,m1,r1 )


def ZjistiPocetHodinMezi(datum, datum2):
    """převede data - listy na rozdíl času v minutách """
    rok1,mesic1,den1,hodina1,minuta1 = datum
    rok2,mesic2,den2,hodina2,minuta2 = datum2
    prvni = ZjistiDatumNaLinux(rok1,mesic1,den1,hodina1,minuta1)
    druha = ZjistiDatumNaLinux(rok2,mesic2,den2,hodina2,minuta2)
    cas = druha - prvni 
    return cas/60

def ZjistiDatum():
    """načte rok, měsíc, den, hodina, minuta a vrátí to jako list
    když uživatel něco pokazí, vrátí 1"""
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
    """vrátí list ve formátu [ROK, MESIC, DEN, HODINA, MINUTA]"""
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

def ZjistiInterval(maximum = 1440, minimum = 0):
    """kontrola délky intervalu –> nemá smysl dávat větší než 24 hodin (1440 min), menší 0. Automaticky větší než 24 mu tedy nepovolím a zamítnu 
        lze si nastavit vlastní hodnoty, pokud by bylo třeba 

        - pokud by interval byl větší než 24 hodin, nemá moc smysl pravidelně upomínat. 
        - maximum 24 hodin bylo zvoleno, jelikož je to největší možnost, kdy ještě zjistit 
        že je úkol další den 
    """
    
    inter = input("Zadej interval v minutách: ")
    podminka = True
    while podminka:
        try:
            #pokud zadá string, automaticky spadne
            if int(inter)<=  maximum:
                if int(inter) > minimum:
                    return inter
            print("Tvůj interval přesáhl 24 hodin. Zvol si nějaký, který bude smysluplný:")
            inter = input()
        except:
            #pokud zadal string 
            print("Tvůj vstup je špatně zadaný, zadej znovu smysluplnější:")
            inter = input()  

def ZjistiVstup(timeout_ = 5,text_tisk = ""):
    f"""Čeká dobu *timeout* na vstup, automaticky {timeout_} sekund, jinak vrátí False a prázdný string.
    Pokud se zadá vstup, vrátí daný vstup a True
    """
    fronta = queue.Queue()
    def cteni_vstupu_(fronta):
        try:
            vstup = input(text_tisk)
            fronta.put((True, vstup))
        except:
            fronta.put((False, ""))
    vlakno_vstup = threading.Thread(target=cteni_vstupu_, args=(fronta,))#turple pro správnou interpretaci - proto (fronta,)
    vlakno_vstup.start()

    vlakno_vstup.join(timeout=timeout_)

    if vlakno_vstup.is_alive():
        print("Čas vypršel, vstup nebyl zadán.")
        return False, ""
    else:
        return fronta.get()

#zrejmě nepoužívaný 
def ZjistiJestliNadeselCas(_kdy_mam_skoncit_):
    """hlavní vlákno kontrolující čas, jestli už není kdy mám skončit
    pokud není, vrátím False, pokud je, vrátím True
    - zjišťuji pomocí nezávislého vlákna"""
    
    def _Nadesel_cas(_kdy_mam_skoncit_):
        print(f"čas je {time.time()} a mám skončit za {_kdy_mam_skoncit_ - time.time()}")
        while time.time() >= _kdy_mam_skoncit_:
            pass
        return True 
    vlakno_nadesel = threading.Thread(target=_Nadesel_cas, args=(_kdy_mam_skoncit_,))
    vlakno_nadesel.start()
    if vlakno_nadesel.is_alive():
        print(f"Nepřišel ještě ten čas")
        return False
    else:
        return True 


