"""
Láďa Vávra 
1.ročník MFF UK 

Zápočtový program 
ZS 2023/2024

Programování I 
NPRG030

část programu: potřebný modul
"""
import random 
#pro náhodný výběr motivujícíc hlášky během výstrah


def PresunzAdoB(_soubor_odkud, _soubor_kam,_ktery_radek):
    """přečte celý soubor, přesune zadanou řádku z souboru A -> B a přepíše soubor B tak, že v souboru A už nebude daná řádka """
    #vždy musí být odsazeno v souboru už před, dá nový řádek pro další řádku 
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
    #print("-------------------")
    #print(f"meneny radek je {meneny_radek}")

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
    print(f"zadej mi následujících {pocet-1} atributů na každý řádek zvlášť v pořadí: {__nazvy_atributu}")
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

def Vystraha(_pocet_opakovani, _zbyvajici_cas__):
    
    print(f"  počet opakování: {_pocet_opakovani} \n      zbyvájící, delta času je {_zbyvajici_cas__}")
    list_motiv1 = ["jdi do toho!"]
    list_motiv2 = ["Už se ti blíží termín, ale ještě máš šanci :D"]
    list_motiv3 = ["S kazni prichazi svoboda. Posledni sance to stihnout bro "]
    if _pocet_opakovani == 0:
        #první výstraha, ještě žádná nebyla předtím 
        print(f"blíží se ti termín! máš ho za {_zbyvajici_cas__}, toto je tvá první výstraha")
        return
    #chci aby mi skončila funkce, když nastane první možnost 
    if _pocet_opakovani == 1: 
        #druhá výstraha
        index_1 = random.randrange(0,len(list_motiv1))
        print(list_motiv1[index_1])
        print(f"zbývá ti ještě: " + str(_zbyvajici_cas__))
        ###print(f"TADY DOPSAT MOTIVUJICI HLASKU NA PRVNI OPAKOVANÍ, jedná se o tvoji druhou výstrahu ") 
        return
    if _pocet_opakovani == 2: 
        #druhá výstraha - vytisknu náhodnou povzbuzující hlášku 
        ##print(f"TADY DOPSAT MOTIVUJICI HLASKU NA DRUHEEE OPAKOVANI, jedná se o tvoji třetí výstrahu ")
        index_2 = random.randrange(0,len(list_motiv2))
        print(list_motiv2[index_2])
        print(f"zbývá ti ještě: " + str(_zbyvajici_cas__))
        return 
    if _pocet_opakovani == 3: 
        ##print(f"KAMO UZ TO MAS FAKT BLIZKO DELEJ NECO S TIM HELE UZ, už máš více než 3 výstrahy ")
        index_3 = random.randrange(0,len(list_motiv3))
        print(list_motiv3[index_3])
        print(f"zbývá ti ještě: " + str(_zbyvajici_cas__))
        return 
    if _pocet_opakovani >3:
        #doporučení psychologa 
        print(f"Již jsi nesplnil úkol více než 3x. Zkus se prosím s kvalifikovaným psychologem poradit o chronické prokrastinaci.")
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
                print(f"ÚKOL: " + line[15:], end = "")
                print("počet opakování: " + (line[13]))
    if __cislovat == True:
        _cislo_radky = 0
        with open(_soubor_s_aktualnimi_ukoly, 'r') as zdroj:
            for line in zdroj:
                _cislo_radky += 1 
                print(f"ÚKOL číslo {_cislo_radky}: " + line[15:], end = "")
                print("počet opakování: " + (line[13]))

def VypisUkolyKtereHori(_aktualni_cas,_soubor_s_horicimi_ukoly):
    """ z sb_s_hořícími_úkoly vypíšu úkoly, které mají do splnění méně než den """
    #print(f"aktuální čas a datum je {_aktualni_cas}", end = '\n \n ')
    aktualizovany_soubor = ""

    with open(_soubor_s_horicimi_ukoly, 'r') as zdroj:
        #print("přivolána funkce vypisukoly které hoří ")
        for line in zdroj: 
            print(f"\n %%%% \n aktuální řádka: {line}")
            pocet_vystrah = int(line[13]) 

            #zjistím datum úkolu a jeslti je menší než 
            termin_ukolu = int(line[0:10])
            #print(f"čas a datum je {_aktualni_cas}")
            delta_casu = termin_ukolu - _aktualni_cas
            print(f"\n ----- \n výpočet delty času: \n delta času .. {delta_casu} = {termin_ukolu} - {_aktualni_cas}\n termín úkolu je {termin_ukolu} \n aktuální čas je {_aktualni_cas}")
            #zjistím zbývající čas do splnění úkolu,
            #jestli méně jak 1 00 00 tak dělám akci
            if delta_casu <= 1_00_00:
                    #delta_casu < 1_00_00:
                    #tu jsou ukoly ktere maji mene než 1 den na splněí 
                    #chci zjistit počet výstrah / opakování 
                    #chci zvětšit počet opakování daného úkolu o 1
                    #než přepisovat celý soubor, tak asi bude jednodušší to dát od dalšího souboru 
                    Vystraha(pocet_vystrah, delta_casu)
                    print(f"\n hořící úkol: {line[15:]}")
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

def VypisRadku(_radka_s_past_due_ukolem):
    #chci speciálně vypsast úkoly, které už jsou po termínu a já mu je chci říct 
    #print("\n\nfunkce VypisRadku")
    _do_kdy_se_mel_splnit_cele_datum = _radka_s_past_due_ukolem[:12]
    ##print(f"pro řádku {_radka_s_past_due_ukolem}\n bylo datum splnění {_do_kdy_se_mel_splnit_cele_datum}")
    ##print(f"KONTORLA : ŘÁDKA JE |{_radka_s_past_due_ukolem}.")
    ##print(f"KONTROLNÍ PRINT. délka řádky |{len(_radka_s_past_due_ukolem)}")
    _jmeno_ukolu_past_due = _radka_s_past_due_ukolem[15:]
    _rok_past_due = _do_kdy_se_mel_splnit_cele_datum[0:4]
    _mesic_past_due = _do_kdy_se_mel_splnit_cele_datum[4:6]
    _den_past_due = _do_kdy_se_mel_splnit_cele_datum[6:8]
    _hodina_past_due = _do_kdy_se_mel_splnit_cele_datum[8:10]
    _minuta_past_due = _do_kdy_se_mel_splnit_cele_datum[10:12]
    _pocet_vystrah_due = _radka_s_past_due_ukolem[13]
    print(f"úkol {_jmeno_ukolu_past_due} měl být splněn {_rok_past_due}/{_mesic_past_due}/{_den_past_due} \
          v čase {_hodina_past_due}:{_minuta_past_due}. Byl jsi na něj upozorněn již {_pocet_vystrah_due}")
    #jméno úkolu, datum kdy mělo být splněno,počet jeho opakování, 
                   
def PresunPodleCasuZAdoB(_cas,_souborA,_souborB,_Kolik_ma_zbyt):
    """pokud je čas do plnění méně nebo kolik-má-zbýt tak přesune úkol ze souboru A do souboru B
        pro 24 hodin -- 1_00_00 -> odpovídá 01(D)24(H)59(M)
        pro 0 hodin -- 0
       """
    #chci zavoalt přesuňZAdoB na potřebné řádky 
    _aktualni_r = 0
    with open(_souborA, "r") as _A:
        _max_radku = sum(1 for _ in _A) 
        while _aktualni_r < _max_radku:
            for _radek in _A:
                _datum_radky = int(_radek[0:10])
                #vyzvedne číslo - datum splnění úkolu 
                #rozdil pod 10000 - šlo by přepočítat na minuty, ale takto ulehčuji a je to obecnější 
                _zbyva_casu = _datum_radky - _cas
                if _zbyva_casu <= _Kolik_ma_zbyt:
                    #budu měnit danou řádku –> přesunu ji do druhého souboru 
                    x = PresunzAdoB(_souborA,_souborB,_aktualni_r)
                    _aktualni_r = 0
                    #začnu prohledávat odznova
                else:
                    _aktualni_r += 1

    
                 

                




"""
soubor_s_ukoly = 'uk_test.txt'
#VypisUkoly(soubor_s_ukoly)

jmena_parametru_ukolu = ["datum splnění Rok_Měsíc_Den_Hodina_Minuta", "počet opakování", "jméno úkolu"]
typy_pyrametru_ukolu = [int, int, str]

#soubor s aktuálními úkoly 
soubor_aktualni_ukoly =     'uk_test.txt'
soubor_s_horicimi_ukoly =   'uk_hori.txt'

pokracovat = True
while pokracovat == True:
    #udělají se funkce 
     #   přečtu aktuální úkoly
      #  zjistím čas
      #  porovnám čas s úkoly
      #  jestli se blíží nějaký úkol, tak ho vypíšu 
      #  jestli je už po nějakém úkolu tak 
      #  zeptám se jestli chce něco dělat 
      #  
  #začátek když se spustí smyčka 
    
    #aktualni_cas_zjisteny = int(ZjistiTedCasVratiString())
    #POZOR ODDĚLAT ZE ZÁVOREK!!
    #
    #aktualni_cas_zjisteny = 1000
    #VypisUkoly(soubor_aktualni_ukoly)
   # VypisUkoly(soubor_aktualni_ukoly)
   # VypisUkolyKtereHori(aktualni_cas_zjisteny, soubor_s_horicimi_ukoly)
    
    #ukolykterepastdue(soubor_s_horicimi_ukoly)
    #chces_odstrknout_horici_ukoly(soubor_s_horicimi_ukoly,soubor_s_hotovymi_ukoly, ??)
    #chces si odskrtnout nehorici ukoly( soubor_s_aktualnimi ukoly, soubor s hotovymi ukoly, )
    #chces pridat ukol() –> hotovy modul 
    # chces si zobrazit hotove ukoly(soubr s hotovymi ukoly )
    #pravidelne ukoly - pridani pravidelnych ukolu ??? 
    #NE ! rozvrh hodin??? - pravidelne ukoly ktere musim pridat a sty splnit - takze zase nějaké opakování 
    # 

    




    
    #PridejUkol(typy_pyrametru_ukolu, soubor_aktualni_ukoly, jmena_parametru_ukolu)
    pokracovat = False
print("funguju ")

"""



