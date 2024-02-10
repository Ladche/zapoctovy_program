"""
Láďa Vávra 
1.ročník MFF UK 

Zápočtový program 
ZS 2023/2024

Programování I 
NPRG030

část programu: potřebný modul práce s úkoly 
"""
import random 
from modul_casove_operace import ZjistiStringNaSekundy

#pro náhodný výběr motivujícíc hlášky během výstrah


def PresunzAdoB(_soubor_odkud, _soubor_kam,_ktery_radek):
    """přečte celý soubor, přesune zadanou řádku z souboru A -> B a přepíše soubor B tak, že v souboru A už nebude daná řádka """
    #vždy musí být odsazeno v souboru už před, dá nový řádek pro další řádku 
    #print(f"zavolána funkce PresunzAdoB na řádku {_ktery_radek} z {_soubor_odkud} -> {_soubor_kam}")
    aktualni_radka = 0
    meneny_radek = ""
    obsah_s_odkud = ""
    with open(_soubor_odkud, 'r') as soubor1:
        for line in soubor1:
            #print(line)    #bere to mega moc radku ktere tam ani nejsou 
            aktualni_radka += 1
            if aktualni_radka == _ktery_radek:
                #print(f"menena radka je {line}, hodnota meneneho radku je {meneny_radek}")
                #meneny_radek += str(line)
                meneny_radek += line
                #našel jsem řádku kterou chci měnit 
                #print(f"měněná řádka PO je {meneny_radek}.")
            else:
                obsah_s_odkud += line #+ "\n"
                #print(f"obsah souboru odkud beru bez řádky je zatím : {obsah_s_odkud}")
                #přidávám řádky origo souboru, ať nemusím pak mazat a vše posunout
                #chtěnou řádku tam nepřidávám, stejně bych ji mazal
    with open(_soubor_odkud, 'w') as soubor1: #soubor odkud vezmu
        soubor1.write(str(obsah_s_odkud) )#+ "\n")
    with open(_soubor_kam, 'a') as soubor2:#soubor kam dopisu
        soubor2.write(str(meneny_radek))
    
    #print("uspesne zmeneno :D")
    #print(f"ZAVOLANO: meneny radek je {meneny_radek}")

def PridejUkol(_typy_atributu_co_maji_byt, _soubor,_jmena_atributu = None):
    """typy atributu -- List, soubor -- 'soubor.txt',jmena_atributu = list se stringy které uvidí uživatel
    do souboru přidá specifikované typy parametrů (jako stringy),
      zkontroluje že uživatel dává správné typy souborů, jinak hodí chybu a vrátí 1
        každý parametr co chci přidat zvlášť specifikovat jaký typ to má být, jede po jednom 
        tedy např 5 stringů a int  : [str, str, str, str, str, int]
        VÝJIMKY:\n
            - pokud v atributu "NEPSAT" nebude se uživatele ptát na daný atribut a přidá 0 \n
            - pokud nelze přidat úkol - chyba uživatele (špatně zadané parametry) .. vrátí 1\n
            - pokud přidá úkol, vrátí 0 \n
        """
    pridavane_atributy = Atributy(_typy_atributu_co_maji_byt,_jmena_atributu)
    if pridavane_atributy == 1:
        print("špatně přidané parametry, zkus to znova :D")
        return 1
    with open(_soubor, 'a') as s:
        #automaticky zavře soubor jak se dodělá blok kódu, takže jej nemusím zavírat sám 
        #s_obsah = s.read() #read pro menší soubory, readlines() pro větší soubory 
        #či přímo s.readline(n) - přečtě to prvních n znaků
        #print(s_obsah)
        pridavane = ""
        for atribut in pridavane_atributy:
            x = str(atribut)
            pridavane += x + " "


        s.write(str(pridavane) + "\n")  #text co se přidává 
        #print(f"přidal jsem atributy {pridavane}, {pridavane_atributy} ")
        #chci přidávat \n na začátek, ať se mi to odsadí 
    return 0

"""
nejde to pro každý atribut zvlášť a musím to rozdělit na případy podle toho, jestli zrovna chci zjistit číslo, string,...
a pak to podle toho zkontrolovat 
"""
#atributy jsou hotové
def Atributy(__typy_atributu_na_kontrolu,__nazvy_atributu = ""):
    """přidá počet atributů co dostane, zkontroluje jestli každý sedí s tím jaký jeho typ
    chceš, pokud nesedí, tak hodí chybu (a vrátí 1 nadprogramu)
    například typy_atributu_na_kontrolu = [int,str]"""
    #netiskne atribut, pokud je atribut "NEPSAT" a dá 0 
    pocet = len(__typy_atributu_na_kontrolu)
    print(f"zadej mi následujících {pocet-1} atributů na každý řádek zvlášť: ")     ##v pořadí: {__nazvy_atributu}") #nadbytečné 
    __atributy = []
    for i in range(pocet):
        if __nazvy_atributu[i] == "NEPSAT":
            __atributy.append(0)
            #pokud je zadané toto slovo, program ignoruje atribut a jede dál 
        else:
            print(f"zadej mi {__nazvy_atributu[i]}\n\n... typu {__typy_atributu_na_kontrolu[i]}: \n")
            #print(f"chci formát: {typy_atributu_na_kontrolu[i]} ať mi zadáš pro atribut {nazvy_atributu[i]}:")
            if __typy_atributu_na_kontrolu[i] == int:
                #jediný přidávaný int je datum,čas,... a ten má mít délku 12
                __input_uziv = input()
                try:
                    if len(__input_uziv) == 12:
                        a = int(__input_uziv)
                        #test jestli je zadáno opravdu číslo
                        ##print(f"FAJN Atribut měl být {typy_atributu_na_kontrolu[i]} a dal jsi {type(input_uziv)}")
                        __atributy.append(a)
                    else:
                        print(f"chyba, zkus znovu. Atribut měl být {__typy_atributu_na_kontrolu[i]} a dal jsi {type(__input_uziv)}")
                        return 1
                except:
                    print(f"chyba, zkus znovu. Atribut měl být {__typy_atributu_na_kontrolu[i]} a dal jsi {type(__input_uziv)}")
                    return 1
            if __typy_atributu_na_kontrolu[i] == str:
                try:
                    input_uziv = input()
                    a = str(input_uziv)
                    #print(f"FAJN Atribut měl být {typy_atributu_na_kontrolu[i]} a dal jsi {type(input_uziv)}")
                    __atributy.append(a)
                except:
                    print(f"chyba - špatně zadaný typ, zkus znovu: Atribut měl být {__typy_atributu_na_kontrolu[i]} a dal jsi {type(input_uziv)}")
                    return 1
    return __atributy

def Vystraha(_zbyvajici_cas__):
    
    ##print(f"\tzbyvájící čas je {_zbyvajici_cas__}")
    #hlášky na to, když nesplní úkol - 1h, 2h, 3h po datumu splnění 
    list_motiv1 = ["jdi do toho!"] #hodina po až dvě 
    list_motiv2 = ["Už jsi po termínu, ale nelámej hlavu "] #dvě až tři hodiny 
    list_motiv3 = ["S kázní přichází svoboda"] #tři až čtyři hodiny po 
    #předělat na kontrolu zbývajícího času 
    if _zbyvajici_cas__ > -3600:
        #nultá  výstraha, ještě žádná nebyla předtím 
        print(f"Pojď na to! Tento úkol jsi měl před {int(abs(_zbyvajici_cas__)/60)} min, toto je připomenutí")
        return
    #chci aby mi skončila funkce, když nastane první možnost 
    if (_zbyvajici_cas__ > -7200) and (_zbyvajici_cas__ < -3600): 
        #první výstraha
        index_1 = random.randrange(0,len(list_motiv1))
        print("\t" + list_motiv1[index_1])
        print(f"\tJe to první připomenutí úkolu, co jsi měl před {int(abs(_zbyvajici_cas__)/60)}min, vrhni se na něj!")
        return
    if (_zbyvajici_cas__ > -10800) and (_zbyvajici_cas__ < -7200): 
        #druhá 
        index_2 = random.randrange(0,len(list_motiv2))
        print("\t" + list_motiv2[index_2])
        print(f"\tDruhé připomenutí úkolu, který jsi chtěl splnit před {int(abs(_zbyvajici_cas__)/60)} min")
        return 
    if (_zbyvajici_cas__ > -14400) and (_zbyvajici_cas__ < -10800): 
       #třetí výstraha 
        index_3 = random.randrange(0,len(list_motiv3))
        print("\t" + list_motiv3[index_3])
        print(f"\tNezapomeň, tento úkol jsi chtěl splnit! Tak na co váháš a pojď na to! Chtěl jsi to udělat už před: {int(abs(_zbyvajici_cas__)/60)}min")
        return 
    if _zbyvajici_cas__ < -86400:
        #24 hodin s
        #doporučení psychologa 
        print(f"\tJiž jsi nesplnil tento úkol přes 24 hodin. Zkus se prosím s kvalifikovaným psychologem poradit o chronické prokrastinaci.")
        return 

def VypisUkoly(_soubor_s_aktualnimi_ukoly, __cislovat = False):
    """vypíše úkoly s formátem úkolů //DATUM_OPAKOVANÍ_JMENO-UKOLU// z daného souboru 
    tedy klidně už hotové úkoly, nehotové úkoly,... 
    každý úkol na novou řádku
    \
    \t lze číslovat -> __cislovat = "True" 
    """
    #datum má 4(rok)+2(mesic)+2(den)+2(hodina)+2(minuta) znaků + mezera = 13 znaků 
    # opakování má 1 znak + mezera
    #chci psát od 13+1+1 znaku celé –>  15 znaků
    if __cislovat == False:
        with open(_soubor_s_aktualnimi_ukoly, 'r') as zdroj:
            for line in zdroj:
                print(f"ÚKOL: " + line[15:] + "\tpočet opakování: " + line[13])
                print() #pro vizuální stránku 
                
    if __cislovat == True:
        _cislo_radky = 0
        
        with open(_soubor_s_aktualnimi_ukoly, 'r') as zdroj:
            for line in zdroj:
                _cislo_radky += 1 
                print(f"ÚKOL číslo {_cislo_radky}: \n\t" + line[15:] + "\tpočet opakování: " + line[13])
                print() #vizuální oddělení
                

def VypisUkolyPastDue(_soubor_s_horicimi_ukoly):
    """ z post_due vypíšu úkoly, které mají do splnění méně než den """
    #print(f"aktuální čas a datum je {_aktualni_cas}", end = '\n \n ')
    aktualizovany_soubor = ""

    with open(_soubor_s_horicimi_ukoly, 'r') as zdroj:
        #print("přivolána funkce vypisukoly které hoří ")
        for line in zdroj: 
            if len(line) >1:#vyřešení problému s koncovou řádkou- mezerou na konci souboru
                ##print(f"aktuální řádka: {line} délky {len(line)} ")
                try:
                    pocet_vystrah = int(line[13]) 
                    VypisRadku(line, True)
                    if pocet_vystrah <=8:
                        aktualizovana_vystraha = pocet_vystrah + 1
                        aktualizovana_line = line[:13] + str(aktualizovana_vystraha) + line[14:]
                        aktualizovany_soubor += aktualizovana_line
                    else:
                        #ochrana proti přetečení při příliš častému opakování 
                        aktualizovana_vystraha = pocet_vystrah + 1
                        aktualizovana_line = line[:13] + str("X") + line[14:]
                        aktualizovany_soubor += aktualizovana_line
                except:
                    VypisRadku(line, True)
                    aktualizovany_soubor += line
    with open(_soubor_s_horicimi_ukoly, 'w') as akt:
        akt.write(str(aktualizovany_soubor))

def VypisUkolyKtereHori__(_aktualni_cas,_soubor_s_horicimi_ukoly):
    """ z sb_s_hořícími_úkoly vypíšu úkoly, které mají do splnění méně než den """
    #print(f"aktuální čas a datum je {_aktualni_cas}", end = '\n \n ')
    aktualizovany_soubor = ""

    with open(_soubor_s_horicimi_ukoly, 'r') as zdroj:
        #print("přivolána funkce vypisukoly které hoří ")
        for line in zdroj: 
            print(f"\n %%%% \n aktuální řádka: {line} délky {len(line)} s počtem výstrah {line[13]}")
            pocet_vystrah = int(line[13]) 

            #zjistím datum úkolu a jeslti je menší než 
            termin_ukolu = int(line[0:10])
            #print(f"čas a datum je {_aktualni_cas}")
            delta_casu = termin_ukolu - _aktualni_cas
            ##print(f"\n ----- \n výpočet delty času: \n delta času .. {delta_casu} = {termin_ukolu} - {_aktualni_cas}\n termín úkolu je {termin_ukolu} \n aktuální čas je {_aktualni_cas}")
            #zjistím zbývající čas do splnění úkolu,
            #jestli méně jak 1 00 00 tak dělám akci
            if delta_casu <= 1_00_00:
                    #delta_casu < 1_00_00:
                    #tu jsou ukoly ktere maji mene než 1 den na splněí 
                    #chci zjistit počet výstrah / opakování 
                    #chci zvětšit počet opakování daného úkolu o 1
                    #než přepisovat celý soubor, tak asi bude jednodušší to dát od dalšího souboru 
                    print(f"\n Hořící úkol: {line[15:]}")
                        #změna pořadí, bylo to opačně
                    Vystraha(pocet_vystrah, delta_casu)
                    
                    #print("if podmínka")
                    aktualizovana_vystraha = pocet_vystrah + 1
                    aktualizovana_line = line[:13] + str(aktualizovana_vystraha) + line[14:]
                    aktualizovany_soubor += aktualizovana_line

                    #vím, že počet podmínek nepřesáhne danou hranici 
                    #print(f"řádka předtím byla {line} \na po aktulizaci {aktualizovana_line}")
                    #TOHLE ASI NEMA SMYSL, KDYŽ MAM SOUBOR S PAST-DUE 
                    if delta_casu <= 0:
                        VypisRadku(aktualizovana_line)
                        #vypíšu jen úkoly, které mají záporný čas do splnění 
                    else:
                        pass
            else:
                aktualizovany_soubor += line
    with open(_soubor_s_horicimi_ukoly, 'w') as akt:
        akt.write(str(aktualizovany_soubor))

def VypisRadku(_radka_s_neco_ukolem,byl = False):
    """pokud False, tak píše hořící se úkoly, pokud True, píše úkoly co již měly být splněné past due
    - False -> hořící úkoly
    - True -> past due úkoly
    """
    #chci speciálně vypsast úkoly, které už jsou po termínu a já mu je chci říct 
    #print("\n\nfunkce VypisRadku")
    if byl == True:
        _do_kdy_se_mel_splnit_cele_datum = _radka_s_neco_ukolem[:12]
        ##print(f"pro řádku {_radka_s_past_due_ukolem}\n bylo datum splnění {_do_kdy_se_mel_splnit_cele_datum}")
        ##print(f"KONTORLA : ŘÁDKA JE |{_radka_s_past_due_ukolem}.")
        ##print(f"KONTROLNÍ PRINT. délka řádky |{len(_radka_s_past_due_ukolem)}")
        _jmeno_ukolu_past_due = _radka_s_neco_ukolem[15:]
        _rok_past_due = _do_kdy_se_mel_splnit_cele_datum[0:4]
        _mesic_past_due = _do_kdy_se_mel_splnit_cele_datum[4:6]
        _den_past_due = _do_kdy_se_mel_splnit_cele_datum[6:8]
        _hodina_past_due = _do_kdy_se_mel_splnit_cele_datum[8:10]
        _minuta_past_due = _do_kdy_se_mel_splnit_cele_datum[10:12]
        _pocet_vystrah_due = _radka_s_neco_ukolem[13]
        print(f"ÚKOL: " + str(_jmeno_ukolu_past_due))
        print(f"\tměl být splněn {_den_past_due}/{_mesic_past_due}/{_rok_past_due} v čase {_hodina_past_due}:{_minuta_past_due}. Byl jsi na něj upozorněn již {_pocet_vystrah_due}")
        print()
        #jméno úkolu, datum kdy mělo být splněno,počet jeho opakování, 
    if byl == False:
        _do_kdy_se_mel_splnit_cele_datum_horici = _radka_s_neco_ukolem[:12]
        _jmeno_ukolu_horici_ = _radka_s_neco_ukolem[15:]
        _rok_horici_ = _do_kdy_se_mel_splnit_cele_datum_horici[0:4]
        _mesic_horici_ = _do_kdy_se_mel_splnit_cele_datum_horici[4:6]
        _den_horici_ = _do_kdy_se_mel_splnit_cele_datum_horici[6:8]
        _hodina_horici_ = _do_kdy_se_mel_splnit_cele_datum_horici[8:10]
        _minuta_horici_ = _do_kdy_se_mel_splnit_cele_datum_horici[10:12]
        print(f"Pozor blíží se úkol: " + str(_jmeno_ukolu_horici_))
        print(f"\t splň ho do {_den_horici_}/{_mesic_horici_}/{_rok_horici_} do {_hodina_horici_}:{_minuta_horici_}")
        print()

#asi odstranit ?? 
def PresunPodleCasuZAdoB_(_cas,_souborA,_souborB,_Kolik_ma_zbyt):
    """pokud je čas do plnění méně nebo kolik-má-zbýt tak přesune úkol ze souboru A do souboru B
        pro 24 hodin -- 1_00_00 –> odpovídá 01(D)24(H)59(M)
        pro 0 hodin -- 0
       """
    #chci zavoalt přesuňZAdoB na potřebné řádky 
    _aktualni_r = 0
    print("spuštěna funkce přesuňpodlečasu")
    with open(_souborA, "r") as _aa:
        print("otevřel jsem soubor A")
        _max_radku = sum(1 for _ in _aa) 
        print(f"našel jsem nejdelší řádek v souboru {_souborA}: {_max_radku}")
        while _aktualni_r < (_max_radku+1):
            print(f"zkoumám řádky\n")
            for _radek in _aa:
                print(f"zkoumám řádek {_radek}")
                _datum_radky = int(_radek[0:10])
                #vyzvedne číslo - datum splnění úkolu 
                #rozdil pod 10000 - šlo by přepočítat na minuty, ale takto ulehčuji a je to obecnější 
                _zbyva_casu = _datum_radky - _cas
                print(f"pro řádek {_radek}\nje: aktuální {_cas}-získáno ze vstupu,zbývá {_zbyva_casu} ")
                if _zbyva_casu <= _Kolik_ma_zbyt:
                    print("tento řádek bych měl přesunout z souoru A do B a znovu hledám ")
                    #budu měnit danou řádku –> přesunu ji do druhého souboru 
                    x = PresunzAdoB(_souborA,_souborB,_aktualni_r)
                    _aktualni_r = 0
                    #začnu prohledávat odznova
                else:
                    print("tento řádek nebylo potřeba přesuout")
                    _aktualni_r += 1
            return 

def PresunPodleCasuZAdoB(_cas, _souborA, _souborB, _Kolik_ma_zbyt):
    """v sekundách, kolik má zbýt času """
    with open(_souborA, "r") as _aa:
        radky = _aa.readlines()  # Přečte všechny řádky najednou

    _aktualni_r = 0
    while (_aktualni_r) < (len(radky)):
        #print(f"tady to padá: aktualni_radek{_aktualni_r},radky josu v rozsahu {len(radky)}")
        _radek = radky[_aktualni_r]
        #print(f"zkousám řádek {_radek}")
        
        # Zde doplňte logiku pro zpracování řádku
        _datum_radky = int(_radek[0:12])
        #print(f"budu volat ZjiSTRnaSEk a dávám mu datum řádky jako {_datum_radky}")
        __porovnavany_cas_datum_radky = ZjistiStringNaSekundy(_datum_radky)
        _zbyva_casu = __porovnavany_cas_datum_radky - _cas
        ##print(f"zkoumám řádek {_radek}, zbývá {_zbyva_casu} <= {_Kolik_ma_zbyt} a datum splnění řádky je {_datum_radky} neboli {__porovnavany_cas_datum_radky}sekund")

        if _zbyva_casu <= _Kolik_ma_zbyt:
            #print(f"\t\tměním řádek {_radek} s číslem _{_aktualni_r}_, jelikož zbývá {_zbyva_casu} a má mít více než {_Kolik_ma_zbyt}")
            # Logika pro přesun řádku z A do B
            PresunzAdoB(_souborA, _souborB, _aktualni_r+1)
            ##print(f"zavolal jsem přesunutí řádky {_radek}")
            radky.pop(_aktualni_r)  # Odstranění řádku, který byl právě zpracován
            # Nezvyšujeme _aktualni_r, protože jsme odstranili aktuální řádek
        else:
            _aktualni_r += 1  # Pokračujeme na další řádek

from modul_casove_operace import ZjistiStringNaSekundy
def VypisHodinoveUkoly(_aktualni_cas,__soubor__s_post_ukoly):
    """ z souboru vypíšu úkoly, které mají po  splnění """
    #nechci měnit počet upozornění 
    aktualizovany_soubor = ""
    with open(__soubor__s_post_ukoly, 'r') as zdroj:
        for line in zdroj: 
            if len(line) >12:#vyřešení problému s koncovou řádkou- mezerou na konci souboru
               ###print(f"aktuální řádka: {line} délky {len(line)} ")
                
        
                __x_termin_ukolu = int(line[0:12])
                ##print(f"termín úkolu je {__x_termin_ukolu}_")
                #print(f"čas a datum je {_aktualni_cas}")
                __c_termin_ukolu_sekundy = ZjistiStringNaSekundy(__x_termin_ukolu)
                __x_delta_casu = __c_termin_ukolu_sekundy - _aktualni_cas
                ##print(f"delta času je {__x_delta_casu} = {__c_termin_ukolu_sekundy} - {_aktualni_cas}")
                ##print(f"\n ----- \n výpočet delty času: \n delta času .. {delta_casu} = {termin_ukolu} - {_aktualni_cas}\n termín úkolu je {termin_ukolu} \n aktuální čas je {_aktualni_cas}")
                #print(f"Hořící úkol: {line[15:]}")
                            #změna pořadí, bylo to opačně
                #Vystraha(pocet_vystrah, delta_casu)
                __nazev_ukolu_ = line[14:]
                print(f"úkol: {__nazev_ukolu_}")
                Vystraha(__x_delta_casu)

def VypisUkolyKtereHori(_soubor_s_horicimi_ukoly):
    with open(_soubor_s_horicimi_ukoly, 'r') as zdroj:
        for line in zdroj: 
            if len(line) >12:#vyřešení problému s koncovou řádkou- mezerou na konci souboru
                ##print(f"aktuální řádka: {line} délky {len(line)} ")
                VypisRadku(line)
