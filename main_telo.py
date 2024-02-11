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
if KontrolaPritomnostiModulu() == False:
    print("CHYBA\n\t!!zkontrolujte přítomnost potřebných modulů v složce!!")
    assert KontrolaPritomnostiModulu() == False, f"chyba, chybí modul(y)"
else:
    print("kontrola potřebných modulů proběhla úspěšně ")
print("Nastavení úspěšné")
print("-"*50, end = "\n\n")
#konec nastavení programu 

#dodatečné upozornění na začátku programu
VypisHodinoveUkoly(time.time(),"aktualni.txt")
VypisHodinoveUkoly(time.time(),"past_due.txt")
VypisHodinoveUkoly(time.time(),"horici.txt")


#hlavní část 
print("Napiš jak často (v minutách) chceš aby se ti opakovalo vypisování a upozorňování na úkoly")
interval = (int(ZjistiInterval(1439,0.9)) *60) #necelých 24 hodin mi přijde jako smysluplná horní mez vzhledem k cíli programu
print("Napiš jak kolik času v sekundách chceš, aby program čekal na tvoji odpověď")
timeout = int(ZjistiInterval((60))) #horní hranice minuty pro zadání vstupu mi přijde dostačující
cas_zopakovat = 0 #prvotní nastavení pro hodinové kontroly
print("Vše proběhlo v pořádku ")
time.sleep(3) #kvůli možnosti nechat přečíst úkoly, ihned se totiž pak smažou v "print('\x1bc')"
while True:
    print('\x1bc')  #vymaže věci napsané v terminálu 
    print(f"nastaveno na: doba mezi upozorněními: {interval}min, doba na reakci uživatele: {timeout}s")
    aktualni_cas = time.time()
    if (ZjistiJestliJeCelaHodina() == True):
        #každou hodinu připomenutí úkolů, které již měly být splněné 
        VypisHodinoveUkoly(aktualni_cas,past_due) #po 
        VypisHodinoveUkoly(aktualni_cas,horici)# 2 až 3 hodiny před
        VypisHodinoveUkoly(aktualni_cas,aktualni) #2 dny před 
        print("x"*50)
        cas_opakovani_za_hodinu_sekundy_x_ = ZjistiSekundyDoDalsiHodiny()
        kolik_sekund_pockat_x_ = min((cas_zopakovat-time.time()), cas_opakovani_za_hodinu_sekundy_x_)
        time.sleep(kolik_sekund_pockat_x_)
        continue
    aktualni_cas = time.time() #aktualizace času, předchozí blok může trvat určitou i když velmi krátkou dobu - lze případně tento řádek zanedbat
    cas_zopakovat = aktualni_cas + interval #vypočítání času nového spuštění

    #potřebné přesunu z aktuálních do hořících
    PresunPodleCasuZAdoB(aktualni_cas, aktualni, horici, 86400, True)
    #přesun z hořících do past_due 
    PresunPodleCasuZAdoB(aktualni_cas, horici, past_due, 0)
    
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
    text_input = "Napiš mi požadovanou akci:\n "
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
                            radka_kterou_odskrtnout_H = input(f"zadej číslo úkolu, který si přeješ odškrtnout: (pokud nechceš odškrtnout tak zadej text)") #celý řádek je odškrtávaný úkol
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
                    print("%"*40)
                    print("\n\n"+ informacni_text)
                    inp = input(text_input)
    pravdivost = False
    print("\tKonec akcí \n")
    print("="*50)
    cas_opakovani_za_hodinu_sekundy = ZjistiSekundyDoDalsiHodiny()
    kolik_sekund_pockat = min((cas_zopakovat-time.time()), cas_opakovani_za_hodinu_sekundy)
    print(f"další opakování proběhne za {kolik_sekund_pockat}s od {datetime.now()}")
    #print(f"zopakuju za {kolik_sekund_pockat} s -> {kolik_sekund_pockat/60} min  jelikož je to minimum z \ncasu kdy by se ukazal uzivateli{(cas_zopakovat-time.time())/60}min \tza hodinu{cas_opakovani_za_hodinu_sekundy/60}min")
    time.sleep(max(0, kolik_sekund_pockat)) #změna - nahrazení místo subprocesu hlídajícího čas 
