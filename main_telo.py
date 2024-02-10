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

motivujici_hlasky = ["Skvělá práce! Máš hotový další úkol!"]
#motivující hlášky při splnění úkolu

#------------------–––––––––––––––––––––––––––––––––––––-

#nastavení programu - vytvoření potřebných souborů, pokud již nejsou přítomny v aktuální složce 

aktualni = "aktualni.txt"
horici = "horici.txt"
past_due = "past_due.txt"
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

print("Nastavení úspěšné")
print("-"*50, end = "\n\n")
#konec nastavení 

#hlavní část - opakující se


"""#varianta 2 - můžu použít funkci ZjistiInterval()
print("Napiš jak často (v minutách) chceš aby se ti opakovalo vypisování a upozorňování na úkoly")
interval = int(ZjistiInterval()) *60
print("Napiš jak kolik času v sekundách chceš, aby program čekal na tvoji odpověď")
timeout = int(ZjistiInterval((30)))#heuristicky si myslím, že 10 sekundový interval na to, abych se rozhodl jestli chci 
                                #dělat nějakou akci je dostačující
print("Napiš kolik sekund chceš vidět úkoly, co jsi dělal - po ukončení tvojich (případných) akcí. Minimálně je 1s a maximum je hodina")
doba_ponechani_terminalu = int(ZjistiInterval(3599,1))
"""
cas_zopakovat = 40
timeout = 10
interval = 50 #ODEBRAT "!!!!!" nastaveno na 3 sekundy
#cekaci_doba_terminalu = 20
doba_ponechani_terminalu = 30 #max hodisna 
while True:
    #tady chci kontrolovat hořící úkoly a kdyžtak vypsat výstrahu, že zbývá 1h / 2h / 3h
    """
    kontrolovat každou hodinu 
    každé ráno v 9 přijde hláška 
    if 24 hodin po
    if 3 hodiny po 
    if 2 hodiny  po 
    if hodina  po
    """
    aktualni_cas = time.time()
    #if (aktualni_cas %)
    cas_opakovani_za_hodinu = aktualni_cas + 3600
    if (ZjistiJestliJeCelaHodina() == True) and (cas_opakovani_za_hodinu < cas_zopakovat):
       # print("pod tímto")
        #print(f"mělo by platit že {cas_opakovani_za_hodinu} < {cas_zopakovat} –> delta {cas_opakovani_za_hodinu - cas_zopakovat} s aktualnim {aktualni_cas}")
        #if True and (cas_opakovani_za_hodinu < cas_zopakovat):  
        #print("aka hodina uplynula ")
        VypisHodinoveUkoly(aktualni_cas,past_due)
        #print("HEEEJ!! JSEM TU ")
        time.sleep(cas_zopakovat-aktualni_cas)
        print("x"*50)
        continue
    #print("ještě nad tímhle")
    #má se spustit co hodinu 
    #cílem aby program běžel nonstop v pozadí 
    #aktualni_cas = time.time()
    cas_zopakovat = aktualni_cas + interval
    #čas nového spuštění 
    #potřebné přesunu z aktuálních do hořících
    PresunPodleCasuZAdoB(aktualni_cas, aktualni, horici, 86_400)#změněno na sekundy 
    #přesun z hořících do past_due 
    PresunPodleCasuZAdoB(aktualni_cas, horici, past_due, 0)
    #vypís úkolů
        #výpis aktuálních úkolů 
    VypisUkoly(aktualni)
        #výpis hořících úkolů 
    ##print(f"hořící úkoly josu v {horici}")
    VypisUkolyKtereHori(horici)
        #výpis úkolů past due 
    VypisUkolyPastDue(past_due)
    typy_atributu_pridavaneho_ukolu = [int,int,str]
    jmena_atributu_pridavaneho_ukolu = ["datum ve formátu *RRRR.MM.DD.HH.MM* kde \n\tR.. roky (například 2024)|\n\tM.. měsíc (například leden..01)|\n\tD.. datum dne v měsíci (druhý -> 02)|\n\tH.. hodina (formát 24 hodin, 01-24)|\n\tM .. minuta (0 až 60) ","NEPSAT","Jméno úkolu: "]
    #otázka, jestli chce něco dělat za akce: 
    #timeout na rozhodnutí 
    print("\nChceš provádět nějaké akce? \nAno ... Napiš cokoliv \nNe ... nereaguj\n")
    pravdivost = ZjistiJestliReaguje(timeout)
    #ze začátku zjistí jestli něco chce dělat, potom už nekontroluji - předpokládám, že uživatel když chce něco dělat, nepřestane odpovídat
    informacni_text = "-----------\nmožnosti, jaké akce můžeš zvolit\n  formát: [jméno akce]......[co napsat pro tíženou akci]\
                \n\tOdškrtnout(splnit) úkol ...... O, S\n\tPřidat úkol ...... P\n\tZobrazit hotové úkoly ...... Z \n---------\
                \n\tpro ukončení napiš: cokoliv jiného\n------------"
    text_input = "Napiš mi tíženou akci:\n "
    ##print(f"{zapoceti} - vstup")
    ##print(f"\nvstupní parametry:\npravdivost {pravdivost}\nzapoceti {zapoceti}\ncčas zopakovat {cas_zopakovat}\n aktuální {time.time()}, rozdíl je {cas_zopakovat - time.time()}\n")
    if pravdivost:
        ##zapoceti = input("Napiš mi") #myslím, že nadbytečné, jelikož jsem už zjistil, že chce dělat akci 
        ##if zapoceti == "A":
            
            print(informacni_text)
            inp = input()
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
                        VypisUkoly(horici,True)
                        try:
                            radka_kterou_odskrtnout_H = input(f"zadej číslo úkolu, který si přeješ odškrtnout ")
                            cislo_odskrtavane_radky_H = int(radka_kterou_odskrtnout_H)
                            if cislo_odskrtavane_radky_H >= 0:
                                z2 = PresunzAdoB(horici,hotove,cislo_odskrtavane_radky_H)
                                #přesunutí řádky s úkolem mezi hotové úkoly
                                indexx_motivujici_hlasky = random.randrange(0,len(motivujici_hlasky))
                                print()
                                print(motivujici_hlasky[indexx_motivujici_hlasky])
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
                        ##print(f"volám funkci vypisukoly")
                        VypisUkoly(aktualni,True)
                        ##print(f"zavolal jsem funkci vypisukoly")
                        try:
                            radka_kterou_odskrtnout_A = input(f"zadej číslo úkolu, který si přeješ odškrtnout ")
                            cislo_odskrtavane_radky_A = int(radka_kterou_odskrtnout_A)
                            if cislo_odskrtavane_radky_A >= 0:
                                z4 = PresunzAdoB(aktualni,hotove,cislo_odskrtavane_radky_A)
                                #přesunutí řádky s úkolem mezi hotové úkoly
                                indexx_motivujici_hlasky = random.randrange(0,len(motivujici_hlasky))
                                print()
                                print(motivujici_hlasky[indexx_motivujici_hlasky])
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
                        VypisUkoly(past_due,True)
                        try:
                            radka_kterou_odskrtnout_P = input(f"zadej číslo úkolu, který si přeješ odškrtnout ")
                            cislo_odskrtavane_radky_P = int(radka_kterou_odskrtnout_P)
                            if cislo_odskrtavane_radky_P >= 0:
                                z6 = PresunzAdoB(past_due,hotove,cislo_odskrtavane_radky_P)
                                #přesunutí řádky s úkolem mezi hotové úkoly
                                indexx_motivujici_hlasky = random.randrange(0,len(motivujici_hlasky))
                                print()
                                print(motivujici_hlasky[indexx_motivujici_hlasky])
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
    pravdivost = False
    print("\tKonec akcí \n")
    print("~"*50)
    time.sleep(doba_ponechani_terminalu)
    #print(f"budu čekat {cas_zopakovat - time.time()} protože čas je {time.time()} a mám zopakovat v {cas_zopakovat} s intervalem {interval} neboli {interval/60} minut")
    ktery_z_casu_zopakovat = min(cas_zopakovat, cas_opakovani_za_hodinu)
    #print(f"jdu čekat {ktery_z_casu_zopakovat-time.time()}")
    time.sleep(max(0, ktery_z_casu_zopakovat - time.time())) #změna, pojistka ať nečekám 
    print('\x1bc')  #vymaže věci napsané v terminálu 
    