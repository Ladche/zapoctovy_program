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

motivujici_hlasky = ["Skvělá práce! Máš hotový další úkol!","Moc blahopřeji, že jsi to zvládl.","Super! Zasloužíš si něco, co ti udělá radost.","Dobrá práce.", "Úžasné! Zase jsi o kousek blíž k cíli.","Wow, dobře ty.","Blahopřeji. S kázní přichází svoboda.","Paráda! Malé kroky vedou k velkému úspěchu.","Vedeš si dobře!"]
#motivující hlášky zobrazené při splnění úkolu

#nastavení programu - vytvoření potřebných souborů, pokud již nejsou přítomny v aktuální složce 
aktualni = "aktualni.txt"
horici = "horici.txt"
past_due = "past_due.txt"
hotove = "hotove.txt"
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
#konec nastavení programu 


VypisHodinoveUkoly(time.time(),"aktualni.txt")
VypisHodinoveUkoly(time.time(),"past_due.txt")
VypisHodinoveUkoly(time.time(),"horici.txt")

print("--- tu by se to mělo zipakovat")

#hlavní část 
print("Napiš jak často (v minutách) chceš aby se ti opakovalo vypisování a upozorňování na úkoly")
interval = (int(ZjistiInterval(1439,0.9)) *60) #necelých 24 hodin mi přijde jako smysluplná horní mez vzhledem k cíli programu
print("Napiš jak kolik času v sekundách chceš, aby program čekal na tvoji odpověď")
timeout = int(ZjistiInterval((60))) #horní hranice minuty pro zadání vstupu mi přijde dostačující
print("Napiš kolik sekund chceš vidět úkoly, co jsi dělal - po ukončení tvojich (případných) akcí. Minimálně je 1s a maximum je hodina")
doba_ponechani_terminalu = int((ZjistiInterval(int(interval*60),0.9)))#nemá smysl nechávat terminál déle než je interval mezi připomínáními

cas_zopakovat = 0 #prvotní nastavení pro hodinové kontroly
while True:
    aktualni_cas = time.time()
    cas_opakovani_za_hodinu = aktualni_cas + 3600
    if (ZjistiJestliJeCelaHodina() == True) and (cas_opakovani_za_hodinu < cas_zopakovat):
        #každou hodinu připomenutí úkolů, které již měly být splněné 
        VypisHodinoveUkoly(aktualni_cas,past_due) #po 
        VypisHodinoveUkoly(aktualni_cas,horici)# 2 až 3 hodiny před
        VypisHodinoveUkoly(aktualni_cas,aktualni_cas) #2 dny před 
        time.sleep(cas_zopakovat-aktualni_cas)
        print("x"*50)
        continue

    aktualni_cas = time.time() #aktualizace času, předchozí blok může trvat určitou i když velmi krátkou dobu - lze případně tento řádek zanedbat
    cas_zopakovat = aktualni_cas + interval #vypočítání času nového spuštění

    #potřebné přesunu z aktuálních do hořících
    PresunPodleCasuZAdoB(aktualni_cas, aktualni, horici, 86400, True)
    #přesun z hořících do past_due 
    PresunPodleCasuZAdoB(aktualni_cas, horici, past_due, 0)
    #vypís úkolů
        #výpis aktuálních úkolů 
    VypisUkoly(aktualni)
        #výpis hořících úkolů 
    VypisUkolyKtereHori(horici)
        #výpis úkolů past due 
    VypisUkolyPastDue(past_due)

    typy_atributu_pridavaneho_ukolu = [int,int,str]
        #při přidání úkolu přidávám intové číslo(data splnění úkolu), intové číslo (počtu opakování) a stringový řetězec (názvu úkolu)
    jmena_atributu_pridavaneho_ukolu = ["datum ve formátu *RRRR.MM.DD.HH.MM* kde \n\tR.. roky (například 2024)|\n\tM.. měsíc (například leden..01)|\n\tD.. datum dne v měsíci (druhý -> 02)|\n\tH.. hodina (formát 24 hodin, 01-24)|\n\tM .. minuta (0 až 60) ","NEPSAT","Jméno úkolu: "]

    #možnost pro uživatele interagovat s programem, ovšem s timeoutem, aby případně program nečekal příliš dlouho na nedostavenou reakci
    print("\nChceš provádět nějaké akce? \nAno ... Napiš cokoliv \nNe ... nereaguj\n")
    pravdivost = ZjistiJestliReaguje(timeout)
    #ze začátku zjistí jestli něco chce dělat, potom už nekontroluji - předpokládám, že uživatel když chce něco dělat,a nepřestane odpovídat zničeho nic
    informacni_text = "-----------\nmožnosti, jaké akce můžeš zvolit\n  formát: [jméno akce]......[co napsat pro tíženou akci]\
                \n\tOdškrtnout(splnit) úkol ...... O, S\n\tPřidat úkol ...... P\n\tZobrazit hotové úkoly ...... Z \n---------\
                \n\tpro ukončení napiš: cokoliv jiného\n------------"
    text_input = "Napiš mi tíženou akci:\n "
    if pravdivost:
            print(informacni_text)
            inp = input()
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
                        print()
                        VypisUkoly(horici,True)
                        try:
                            radka_kterou_odskrtnout_H = input(f"zadej číslo úkolu, který si přeješ odškrtnout ") #celý řádek je odškrtávaný úkol
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
                        VypisUkoly(aktualni,True)
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
    ktery_z_casu_zopakovat = min(cas_zopakovat, cas_opakovani_za_hodinu)
    time.sleep(max(0, ktery_z_casu_zopakovat - time.time())) #změna, pojistka ať nečekám 
    #print('\x1bc')  #vymaže věci napsané v terminálu 
    