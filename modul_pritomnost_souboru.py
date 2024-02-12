"""
Láďa Vávra 
1.ročník MFF UK 

Zápočtový program 
ZS 2023/2024

Programování I 
NPRG030

část programu: modul kontroly přítomnosti souborů 
"""
#potřebné moduly
import os

def ZjistiCestuTady():
    "Zjistí a vypíše cestu k aktuální složce, v které je tato funkce spuštěna"
    return os.getcwd()
    
def ZjistiJePritomnySoubor(_soubor):
    """pokud je zadaný soubor v aktuální složce, vypíše True, jinak False """
    for i in os.listdir():
        if _soubor == i:
            return True 
    return False

def NastavSoubory():
    """zjistí přítomnost souborů v složce, pokud nejsou přítomny, vytvoří je 
    -> zjišťuje
        - soubor s aktuálními úkoly: aktualni.txt
        - soubor s hořícími úkoly: horici.txt
        - soubor s post_due úkoly: post_due.txt 
        """
    print("-   "*20)
    print("Začátek úseku nastavování souborů ")
    aktualni = "aktualni.txt"
    horici = "horici.txt"
    past_due = "past_due.txt"
    hotove = "hotove.txt"
    #zjistění přítomnosti souboru s aktuálními,hořícími,hotovými a včas nesplněnými úkoly 
    for _ in range(2):
        #při prvním načtení zjistí přítomnost a při druhém načtení založí (zjistil jsem při testování -> jen jedno spuštění nestačí, hodí chybu, ovšem při druhém spuštění již funguje jak má )
        try:
            if ZjistiJePritomnySoubor(aktualni) == True:
                pass
            else:
                cesta_k_akt = ZjistiCestuTady() + "/" + aktualni
                with open(cesta_k_akt, "r") as f:
                    s = f.readline
        except:
            print("\tsoubor s aktuálními úkoly nebyl přítomný, zahajuji jeho tvorbu ")
            try:
                cesta_k_akt = ZjistiCestuTady() + "/" + aktualni                
                open(cesta_k_akt, "x")
                print("     \tvytvořen soubor s aktuálními úkoly\n")
            except:
                print("CHYBA - zkuste restartovat soubor")
                #vyjímka, chyba, potřeba restartovat 
    for _ in range(2):
        try:
            if ZjistiJePritomnySoubor(horici) == True:
                pass
            else:
                cesta_k_akt = ZjistiCestuTady() + "/" + horici
                with open(cesta_k_akt, "r") as f:
                    s = f.readline
        except:
            print("\tsoubor s hořícími úkoly nebyl přítomný, zahajuji jeho tvorbu ")
            try:
                cesta_k_akt = ZjistiCestuTady() + "/" + horici
                open(cesta_k_akt, "x")
                print("     \tvytvořen soubor s hořícími úkoly\n")
            except:
                print("CHYBA - zkuste restartovat soubor")
    for _ in range(2):
        try:
            if ZjistiJePritomnySoubor(past_due) == True:
                pass
            else:
                cesta_k_akt = ZjistiCestuTady() + "/" + past_due
                with open(cesta_k_akt, "r") as f:
                    s = f.readline
        except:
            print("\tsoubor s post due úkoly nebyl přítomný, zahajuji jeho tvorbu ")
            try:
                cesta_k_akt = ZjistiCestuTady() + "/" + past_due
                open(cesta_k_akt, "x")
                print("     \tvytvořen soubor s post due úkoly\n")
            except:
                print("CHYBA - zkuste restartovat soubor")
    for _ in range(2):
        try:
            if ZjistiJePritomnySoubor(hotove) == True:
                pass
            else:
                cesta_k_akt = ZjistiCestuTady() + "/" + hotove
                with open(cesta_k_akt, "r") as f:
                    s = f.readline
        except:
            print(" \tsoubor s hotovými úkoly nebyl přítomný, zahajuji jeho tvorbu ")
            try:
                cesta_k_akt = ZjistiCestuTady() + "/" + hotove
                open(cesta_k_akt, "x")
                print("     \tvytvořen soubor s hotovými úkoly\n")
            except:
                print("CHYBA - zkuste restartovat soubor")
                #vyjímka, chyba, potřeba restartovat 
    print("\nKonec úseku nastavování potřebných souborů ")
    print("-   "*20)

def KontrolaPritomnostiModulu():
    """zkontroluje přítomnost potřebných modulů, které program potřebuje pro svůj běh """
    modul_a = "modul_casove_operace.py"
    modul_b =  "modul_prace_s_ukoly.py"
    modul_c =  "modul_pritomnost_souboru.py"
    try:
        if ZjistiJePritomnySoubor(modul_a) == True:
            print("přítomný modul: modul_casove_operace")
            pass
        else:
            cesta_k_akt = ZjistiCestuTady() + "/" + modul_a
            with open(cesta_k_akt, "r") as f:
                s = f.readline 
    except:
        print(f" Modul {modul_a} není přítomný !!")
        return False 
    try:
        if ZjistiJePritomnySoubor(modul_b) == True:
            print("přítomný modul: modul_prace_s_ukoly")
            pass
        else:
            cesta_k_akt = ZjistiCestuTady() + "/" + modul_b
            with open(cesta_k_akt, "r") as f:
                s = f.readline
    except:
        print(f" Modul {modul_b} není přítomný !!")
        return False
    try:
        if ZjistiJePritomnySoubor(modul_c) == True:
            print("přítomný modul: modul_pritomnost_souboru")
            pass
        else:
            cesta_k_akt = ZjistiCestuTady() + "/" + modul_c
            with open(cesta_k_akt, "r") as f:
                s = f.readline
                return True #všechny moduly jsou přítomny 
    except:
        print(f" Modul {modul_c} není přítomný !!")
        return False