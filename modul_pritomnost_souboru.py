"""
Láďa Vávra 
1.ročník MFF UK 

Zápočtový program 
ZS 2023/2024

Programování I 
NPRG030

část programu: modul kontroly přítomnosti soouborů 
"""

import os
#cesta do složky, kde je tento soubor 
#JeSouborPřitomnyVe aktuální složce kde je to spuštěné
#cesta k spuštěněému souobru –> složka 
#print("\n")

def ZjistiCestuTady():
    "Zjistí a vypíše cestu k aktuální složce, v které je tato funkce spuštěna"
    return os.getcwd()
    
def ZjistiJePritomnySoubor(_soubor):
    """pokud je zadaný soubor v aktuální složce, vypíše True, jinak False """
    for i in os.listdir():
        #pro každou složku 
        #print(f"soubor {i} je typu {type(i)}")
        if i == _soubor:
            #print(f"SOoubor {_soubor} je přítmncý ")
            #print(f"soubro {i} je v aktuální složce {os.getcwd()}")

            return True 
    return False

def NastavSoubory():
    """zjistí přítomnost souborů v složce, pokud nejsou přítomny, vytvoří je 
    zjišťuje
        - soubor s aktuálními úkoly: aktualni.txt
        - soubor s hořícími úkoly: horici.txt
        - soubor s post_due úkoly: post_due.txt 
        """
    print("-   "*20)
    print("začátek úseku nastavování souborů ")
    aktualni = "aktualni.txt"
    horici = "horici.txt"
    past_due = "past_due.txt"
    hotove = "hotove.txt"
    #zjistění přítomnosti souboru s aktuálními úkoly 
    for _ in range(2):
        #při prvním načtení zjistí přítomnost a při druhém načtení založí 
        #zjistil jsem při testování - jen jedno spuštění nestačí, hodí chybu, ovšem při druhém spuštění již funguje bezchybně 
        try:
            if ZjistiJePritomnySoubor(aktualni) == True:
                pass
            else:
                cesta_k_akt = ZjistiCestuTady() + "/" + aktualni
                with open(cesta_k_akt, "r") as f:
                    s = f.readline
        except:
            print(" \tsoubor s aktuálními úkoly nebyl přítomný, zahajuji  jeho tvorbu ")
            try:
                cesta_k_akt = ZjistiCestuTady() + "/" + aktualni
                #print(f"cesta je {cesta_k_akt}")
                
                open(cesta_k_akt, "x")
                print("     \tvytvořen soubor s aktuálními úkoly\n")
            except:
                print("CHYBA - zkuste restartovat soubor")
                #vyjímka, chyba, potřeba restartovat 

    for _ in range(2):
        #při prvním načtení zjistí přítomnost a při druhém načtení založí 
        #zjistil jsem při testování - jen jedno spuštění nestačí, hodí chybu, ovšem při druhém spuštění již funguje bezchybně 
        try:
            if ZjistiJePritomnySoubor(horici) == True:
                pass
            else:
                cesta_k_akt = ZjistiCestuTady() + "/" + horici
                with open(cesta_k_akt, "r") as f:
                    s = f.readline
        except:
            print(" \tsoubor s hořícími úkoly nebyl přítomný, zahajuji  jeho tvorbu ")
            try:
                cesta_k_akt = ZjistiCestuTady() + "/" + horici
                #print(f"cesta je {cesta_k_akt}")
                
                open(cesta_k_akt, "x")
                print("     \tvytvořen soubor s hořícími úkoly\n")
            except:
                print("CHYBA - zkuste restartovat soubor")

    for _ in range(2):
        #při prvním načtení zjistí přítomnost a při druhém načtení založí 
        #zjistil jsem při testování - jen jedno spuštění nestačí, hodí chybu, ovšem při druhém spuštění již funguje bezchybně 
        try:
            if ZjistiJePritomnySoubor(past_due) == True:
                pass
            else:
                cesta_k_akt = ZjistiCestuTady() + "/" + past_due
                with open(cesta_k_akt, "r") as f:
                    s = f.readline
        except:
            print(" \tsoubor s post due úkoly nebyl přítomný, zahajuji  jeho tvorbu ")
            try:
                cesta_k_akt = ZjistiCestuTady() + "/" + past_due
                #print(f"cesta je {cesta_k_akt}")
                
                open(cesta_k_akt, "x")
                print("     \tvytvořen soubor s post due úkoly\n")
            except:
                print("CHYBA - zkuste restartovat soubor")
    for _ in range(2):
        #při prvním načtení zjistí přítomnost a při druhém načtení založí 
        #zjistil jsem při testování - jen jedno spuštění nestačí, hodí chybu, ovšem při druhém spuštění již funguje bezchybně 
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
                #print(f"cesta je {cesta_k_akt}")
                
                open(cesta_k_akt, "x")
                print("     \tvytvořen soubor s hotovými úkoly\n")
            except:
                print("CHYBA - zkuste restartovat soubor")
                #vyjímka, chyba, potřeba restartovat 

    print("\nkonec úseku nastavování potřebných souborů ")
    print("-   "*20)

def KontrolaPritomnostiModulu():
    """zkontroluje přítomnost potřebných modulů, které program potřebuje pro svůj běh """
    modul_a = "modul_casove_operace.py"
    modul_b =  "modul_prace_s_ukoly.py"
    modul_c =  "modul_pritomnost_souboru.py"
    try:
        if ZjistiJePritomnySoubor(modul_a) == True:
            pass
        else:
            cesta_k_akt = ZjistiCestuTady() + "/" + modul_a
            with open(cesta_k_akt, "r") as f:
                s = f.readline 
    except:
        print(f" modul {modul_a} není přítomný")
        return False 
    try:
        if ZjistiJePritomnySoubor(modul_b) == True:
            pass
        else:
            cesta_k_akt = ZjistiCestuTady() + "/" + modul_b
            with open(cesta_k_akt, "r") as f:
                s = f.readline
    except:
        print(f" modul {modul_b} není přítomný")
        return False
    try:
        if ZjistiJePritomnySoubor(modul_c) == True:
            pass
        else:
            cesta_k_akt = ZjistiCestuTady() + "/" + modul_c
            with open(cesta_k_akt, "r") as f:
                s = f.readline
                return True #všechny moduly jsou přítomny 
    except:
        print(f" modul {modul_c} není přítomný")
        return False
    
