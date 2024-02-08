"""
Láďa Vávra 
1.ročník MFF UK 

Zápočtový program 
ZS 2023/2024

Programování I 
NPRG030

část programu: kostra programu
"""


import time 
from modul_casove_operace import *
from modul_prace_s_ukoly import *
from modul_pritomnost_souboru import *

#------------------–––––––––––––––––––––––––––––––––––––-

#nastavení programu - vytvoření potřebných souborů, pokud již nejsou přítomny v aktuální složce 

aktualni = "aktualni.txt"
horici = "horici.txt"
past_due = "post_due.txt"
hotove = "hotove.txt"
#nastavovani_souboru_pri_startu = NastavSoubory()
print("Nastavuji program:")
NastavSoubory()

#zjištění přítomnosti potřebných modulů 
if KontrolaPritomnostiModulu == False:
    print("CHYBA\n\t!!zkontrolujte přítomnost potřebných modulů v složce!!")
    assert("CHYBA")
else:
    print("kontrola potřebných modulů proběhla úspěšně ")

print("konec nastavování")
print("-"*50, end = "\n\n")
#konec nastavení 

#začátek main() smyčky
#interval = int(input("Zvol si pevný inverval v minutách, jak často chceš být upozorňován(a)")*60)

#stará se o to funkce ZjistiInterval()
#interval = ZjistiInterval()


#timeout = ZjistiInterval((10/60))#heuristicky si myslím, že 10 sekundový interval na to, abych se rozhodl jestli chci 
                                #dělat nějakou akci je dostačující
timeout = 20
interval = 3 #ODEBRAT "!!!!!" nastaveno na 3 sekundy
cas_pocatecni = time.time()
cas_zopakovat = cas_pocatecni + interval 
while True:
    #cílem aby program běžel nonstop v pozadí 
    
    #další vlákno na čas:
    """aktualni_cas_po_konci = time.time()
    #interval už vím, nemusím se znovu ptát 
    #nastavím nový čas, kdy se má znovu spustit:
    cas_zopakovat = interval + aktualni_cas_po_konci

    print(f"Nyní budu vyčkávat, připomenutí ti přijde znovu za {interval/60} minut, tedy v {cas_zopakovat}")
"""
    while time.time() < cas_zopakovat:
        #print(f"stále čekám {time.time()} < {cas_zopakovat}")
        time.sleep(1)
    aktualni_cas = time.time()
    cas_zopakovat = aktualni_cas + interval
    #čas nadešel, jdeme na to:
    #potřebné přesunu z aktuálních do hořících
    ###print("spouští se hlavní myška")
    ###aktualni_cas = time.time()
    ##print(f"aktuální čas je {aktualni_cas}")
    #chyba v přesouvání podle času 
    #x1 = PresunPodleCasuZAdoB(aktualni_cas, aktualni, horici, 10000)
    #přesun z hořících do past_due 
    ###print("dostal jsem se za x1")
    #x2 = PresunPodleCasuZAdoB(aktualni_cas, horici, past_due, 0)
    ####print("----------------------")
    #vypís úkolů
        #výpis aktuálních úkolů 
    VypisUkoly(aktualni)
        #výpis hořících úkolů 
    
    VypisUkolyKtereHori(aktualni_cas, horici)
        #výpis úkolů past due 
    
    VypisUkolyKtereHori(aktualni_cas, past_due)
    

    typy_atributu_pridavaneho_ukolu = [int,int,str]
    jmena_atributu_pridavaneho_ukolu = ["datum ve formátu RRRR.MM.DD.HH.MM kde R.. roky (například 2024)| M.. měsíc (například leden..01)|  D.. datum dne v měsíci (druhý -> 02)| H.. hodina (formát 24 hodin, 01-24)| M .. minuta (0 až 60) ","NEPSAT","Jméno úkolu: "]

    #otázka, jestli chce něco dělat za akce: 
    #timeout na rozhodnutí 
    print("Chceš provádět nějaké akce? \nAno ... A\nNe... N (či cokoliv jiného)\n")
    pravdivost, zapoceti = ZjistiVstup()
    while pravdivost:
        ##zapoceti = input("")
        if zapoceti == "A":
            informacni_text = "-----------\nmožnosti, jaké akce můžeš zvolit\n  formát: [jméno akce]......[co napsat pro tíženou akci]\
                \n        Odškrtnout(splnit) úkol ...... O, S\n        Přidat úkol ...... P\n        Zobrazit hotové úkoly ...... Z \n---------\
                \n    pro ukončení napiš: K \n------------"
            text_input = "Napiš mi tíženou akci:\n "
            print(informacni_text)
            pravdivost, inp = ZjistiVstup()
            #nastavení timeoutu, ať program nečeká celou dobu na uživatelský input, skončí když mu uživatel nic nedá 
            while inp == "P"  or inp == "S" or inp == "O" or inp == "Z":#jednodušší, než speciální klávesa pro ukončení 
                if inp == "P":
                    #přidání úkolu 
                    x = PridejUkol(typy_atributu_pridavaneho_ukolu, aktualni, jmena_atributu_pridavaneho_ukolu)
                    if x == 1:
                        print("\núkol se neporařilo přidat,zkus to znovu :(\n")
                    if x == 0:
                        print("\núkol úspěšně přidán :D\n")
                    print("\n\n"+ informacni_text)
                    inp = input(text_input)

                if inp == "S" or inp == "O":
                    #odškrtnutí, splnění úkolu 
                    #můžu buď vypsat všechny úkoly a z nich ať si vybere - ovšem mohlo by být jak paměťově a časově náročné, tak i zbytečné, jelikož 
                    #uživatel obvykle ví, jestli mu daný úkol hoří, či nikoliv a spíš by ho to jej zdržovalo hledat chtěný úkol
                    #pokud chce odškrtnou více úkolů, může to udělat postupně. 

                    #chci zjistit v kterém souboru hledat 
                    v_jakem_souboru = input("Z jakých úkolů chceš odškrtnout úkol(úkoly)? \nH.. Hořící \t\tA.. Aktuální \t\tP.. úkoly Po termínu \n")

                    if v_jakem_souboru == "H":
                        #hořící úkoly 
                        #zjistit jaký řádek 
                        print()
                        z1 = VypisUkoly(horici,True)
                        try:
                            radka_kterou_odskrtnout_H = input(f"zadej číslo úkolu, který si přeješ odškrtnout ")
                            cislo_odskrtavane_radky_H = int(radka_kterou_odskrtnout_H)
                            if cislo_odskrtavane_radky_H >= 0:
                                z2 = PresunzAdoB(horici,hotove,cislo_odskrtavane_radky_H)
                                #přesunutí řádky s úkolem mezi hotové úkoly
                                print("úspěšně přesunuto")
                                print("\n\n"+ informacni_text)
                                inp = input(text_input)
                            else:
                                print("chyba, zkus znovu")
                                print("\n\n"+ informacni_text)
                                inp = input(text_input)
                        except:
                            print("Měl jsi zadat číslo řádky, zadal jsi špatně ")
                            print("\n\n"+ informacni_text)
                            inp = input(text_input)
                    if v_jakem_souboru == "A":
                        # aktuální úkoly
                        print()
                        z3 = VypisUkoly(horici,True)
                        try:
                            radka_kterou_odskrtnout_A = input(f"zadej číslo úkolu, který si přeješ odškrtnout ")
                            cislo_odskrtavane_radky_A = int(radka_kterou_odskrtnout_A)
                            if cislo_odskrtavane_radky_A >= 0:
                                z4 = PresunzAdoB(aktualni,hotove,cislo_odskrtavane_radky_A)
                                #přesunutí řádky s úkolem mezi hotové úkoly
                                print("úspěšně přesunuto ")
                                print("\n\n"+ informacni_text)
                                inp = input(text_input)
                            else:
                                print("chyba, zkus znovu")
                                print("\n\n"+ informacni_text)
                                inp = input(text_input)
                        except:
                            print("Měl jsi zadat číslo řádky, zadal jsi špatně ")
                            print("\n\n"+ informacni_text)
                            inp = input(text_input)

                    if v_jakem_souboru == "P":
                        #past due úkoly 
                        print()
                        z5 = VypisUkoly(horici,True)
                        try:
                            radka_kterou_odskrtnout_P = input(f"zadej číslo úkolu, který si přeješ odškrtnout ")
                            cislo_odskrtavane_radky_P = int(radka_kterou_odskrtnout_P)
                            if cislo_odskrtavane_radky_P >= 0:
                                z6 = PresunzAdoB(past_due,hotove,cislo_odskrtavane_radky_P)
                                #přesunutí řádky s úkolem mezi hotové úkoly
                                print("úspěšně přesunuto")
                                print("\n\n"+ informacni_text)
                                inp = input(text_input)
                            else:
                                print("chyba, zkus znovu")
                                print("\n\n"+ informacni_text)
                                inp = input(text_input)
                        except:
                            print("Měl jsi zadat číslo řádky, zadal jsi špatně ")
                            print("\n\n"+ informacni_text)
                            inp = input(text_input)
                    else:
                        print(f"špatně jsi zadal písmeno. Můžeš zkusit znovu či jinou akci ")
                        print("\n\n"+ informacni_text)
                        inp = input(text_input)
                if inp == "Z":
                    #výpis jen hotových, protože aktuální, hořící a past due se mu automaticky zobrazí, tudíž nemá smysl je vypisovat 
                    print("Hotové úkoly:")
                    z7 = VypisUkoly(hotove) 
                    print("%%%%%%")
                    print("\n\n"+ informacni_text)
                    inp = input(text_input)
    print("Konec akcí ")
    


    print("aa")
     


