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
def PresunzAdoB(_soubor_odkud, _soubor_kam,_ktery_radek):
    """přečte celý soubor, přesune zadanou řádku z souboru A -> B a přepíše soubor B tak, že v souboru A už nebude daná řádka """
    aktualni_radka = 0
    meneny_radek = ""
    obsah_s_odkud = ""
    with open(_soubor_odkud, 'r') as soubor1:
        for line in soubor1:
            aktualni_radka += 1
            if aktualni_radka == _ktery_radek:
                #najití měněné řádky 
                meneny_radek += line
            else:
                obsah_s_odkud += line #+ "\n"
                #ostatní neměnené řádky přidávám do proměnné reprezentující soubor s odstraněnou příslušnou řádkou
    with open(_soubor_odkud, 'w') as soubor1: #soubor odkud vezmu
        soubor1.write(str(obsah_s_odkud) )#+ "\n")
    with open(_soubor_kam, 'a') as soubor2:#soubor kam dopisu
        soubor2.write(str(meneny_radek))
def PridejUkol(_typy_atributu_co_maji_byt, _soubor,_jmena_atributu = None):
    """typy atributů -- List, soubor -- 'jmeno_souboru.txt',jména_atributů = list se stringy které uvidí uživatel
    do souboru přidá specifikované typy parametrů (jako stringy),
      zkontroluje že uživatel dává správné typy souborů, jinak vrátí chybu a 1
        ke každému parametru potřeba specifikovat jakého typu má být a název, který se zobrazí uživateli
        tedy např 5 stringů a int  : [str, str, str, str, str, int]
        VÝJIMKY:\n
            - pokud v atributu "NEPSAT" nebude se uživatele ptát na daný atribut a přidá automaticky 0 \n
            - pokud nelze přidat úkol -> chyba uživatele (špatně zadal parametry) .. vrátí 1\n
            - pokud přidá úkol, vrátí 0 \n
        """
    pridavane_atributy = Atributy(_typy_atributu_co_maji_byt,_jmena_atributu)
    if pridavane_atributy == 1:
        print("špatně přidané parametry, zkus to znova :D")
        return 1
    with open(_soubor, 'a') as s:
        #takto automaticky zavře soubor jak se dodělá blok kódu, takže jej nemusím netřeba zavírat metodou close() 
        pridavane = ""
        for atribut in pridavane_atributy:
            x = str(atribut)
            pridavane += x + " "
        s.write(str(pridavane) + "\n")  #přidávaný stringový řetězec(reprezentující úkol) do textového souboru
    return 0

def Atributy(__typy_atributu_na_kontrolu,__nazvy_atributu = ""):
    """vratí daný počet parametrů, kolik je položek v __typy_atributu_na_kontrolu od uživatele daných typů. Uživatele se zeptá na příslušný atribut s názvem atributu 
    (položky v __nazvy_atributu), který i zkontroluje. Pokud dostane v názvu atributu "NEPSAT", tak se nevyžaduje vstup od uživatele a automaticky přidá 0"""
    pocet = len(__typy_atributu_na_kontrolu)
    print(f"zadej mi následujících {pocet-1} atributů na každý řádek zvlášť: ")  
    __atributy = []
    for i in range(pocet):
        if __nazvy_atributu[i] == "NEPSAT":
            __atributy.append(0)
            #pokud je zadané slovo "NEPSAT", program se neptá uživatele na input a pokračuje na další(jestli je ještě další atribut)
        else:
            print(f"zadej mi {__nazvy_atributu[i]}\n\n... typu {__typy_atributu_na_kontrolu[i]}: \n")
            if __typy_atributu_na_kontrolu[i] == int:
                __input_uziv = input()
                try:
                    if len(__input_uziv) == 12:
                        #předem vím, že v programu budu načítat pouze data splnění od uživatele jako intová čísla, a vím předem počet cifer - 12 (RRRRMMDDHHMM)
                        a = int(__input_uziv)
                        #pokud by nebylo zadáno číslo, try blok spadne a program přejde do except bloku
                        __atributy.append(a)
                    else:
                        #nebyla zadána potřebná délka data
                        print(f"chyba, zkus znovu. Atribut měl být {__typy_atributu_na_kontrolu[i]} a dal jsi {type(__input_uziv)} s délky 12")
                        return 1
                except:
                    print(f"chyba, zkus znovu. Atribut měl být {__typy_atributu_na_kontrolu[i]} a dal jsi {type(__input_uziv)}")
                    return 1
            if __typy_atributu_na_kontrolu[i] == str:
                try:
                    input_uziv = input()
                    a = str(input_uziv)
                    __atributy.append(a)
                except:
                    print(f"chyba - špatně zadaný typ, zkus znovu: Atribut měl být {__typy_atributu_na_kontrolu[i]} a dal jsi {type(input_uziv)}")
                    return 1
    return __atributy

"""def Vystraha(_zbyvajici_cas__):
    #hlášky na to, když nesplní úkol - mezi 1h, 2h, 3h po datumu splnění 
    list_motiv1 = ["jdi do toho!"] #hodina až dvě po datu splnění
    list_motiv2 = ["Už jsi po termínu, ale nelámej hlavu "] #dvě až tři hodiny 
    list_motiv3 = ["S kázní přichází svoboda"] #tři až čtyři hodiny po 
    if _zbyvajici_cas__ > -3600:
        #nultá  výstraha, méně než hodina po splnění 
        print(f"Pojď na to! Tento úkol jsi měl před {int(abs(_zbyvajici_cas__)/60)} min, toto je připomenutí")
        return  #nemá smysl zkoumat další podmínky
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
        #86 400 sekund = 24 hodin
        print(f"\tJiž jsi nesplnil tento úkol přes 24 hodin. Zkus se prosím s kvalifikovaným psychologem poradit o chronické prokrastinaci.")
        return """

def VypisUkoly(_soubor_s_aktualnimi_ukoly, __cislovat = False):
    """vypíše úkoly s formátem úkolů //DATUM_OPAKOVANÍ_JMENO-UKOLU// z daného souboru 
    tedy klidně už hotové úkoly, nehotové úkoly,... 
    každý úkol na novou řádku
    \t lze číslovat -> __cislovat = "True" 
    """
    #pozice informací v uložených souborech: datum splnění(prvních 12 znaků), počet opakování(15.znak), název úkolu(od 17.znaku) s mezerami mezi jednotlivými informacemi
    if __cislovat == False:
        with open(_soubor_s_aktualnimi_ukoly, 'r') as zdroj:
            for line in zdroj:
                print(f"Úkol: " + line[15:] )   #počet opakování není nutný #+ "\tpočet opakování: " + line[13])
                print() #pouze pro vizuální účely     
    if __cislovat == True:
        _cislo_radky = 0
        with open(_soubor_s_aktualnimi_ukoly, 'r') as zdroj:
            for line in zdroj:
                _cislo_radky += 1 
                print(f"Úkol číslo {_cislo_radky}: \n\t" + line[15:] ) # zbytečné dávat počet opakování + "\tpočet opakování: " + line[13])
                print()

def VypisUkolyPastDue(_soubor_s_post__due_ukoly):
    """vypíše úkoly, ze souboru a zvětší u nich počet upozornění"""
    aktualizovany_soubor = ""
    with open(_soubor_s_post__due_ukoly, 'r') as zdroj:
        for line in zdroj: 
            if len(line) >12:    #podmínka řeší problém vypsání poslední prázdné řádky
                try:
                    #spustí pro počet opakování od 0 až po 8
                    pocet_vystrah = int(line[13]) 
                    VypisRadku(line, True)
                    if pocet_vystrah <=8:
                        aktualizovana_vystraha = pocet_vystrah + 1
                        aktualizovana_line = line[:13] + str(aktualizovana_vystraha) + line[14:]
                        aktualizovany_soubor += aktualizovana_line
                    else:
                        #ochrana proti přetečení počtu upozornění na pozice názvu úkolu
                        aktualizovana_vystraha = pocet_vystrah + 1
                        aktualizovana_line = line[:13] + str("X") + line[14:]
                        aktualizovany_soubor += aktualizovana_line
                except:
                    #pro počet opakování "X"
                    VypisRadku(line, True)
                    aktualizovany_soubor += line
    with open(_soubor_s_post__due_ukoly, 'w') as akt:
        #zapsání aktualizace počtu opakování
        akt.write(str(aktualizovany_soubor))

def VypisRadku(_radka_s_neco_ukolem,byl = False):
    """Vypíše aktuální řádek, hodnota proměnné byl umožní použít pro vypsání past_due úkolů i hořících úkolů
    - False -> hořící úkoly
    - True -> past due úkoly
    """
    if byl == True:
        _do_kdy_se_mel_splnit_cele_datum = _radka_s_neco_ukolem[:12]
        _jmeno_ukolu_past_due = _radka_s_neco_ukolem[15:]
        _rok_past_due = _do_kdy_se_mel_splnit_cele_datum[0:4]
        _mesic_past_due = _do_kdy_se_mel_splnit_cele_datum[4:6]
        _den_past_due = _do_kdy_se_mel_splnit_cele_datum[6:8]
        _hodina_past_due = _do_kdy_se_mel_splnit_cele_datum[8:10]
        _minuta_past_due = _do_kdy_se_mel_splnit_cele_datum[10:12]
        _pocet_vystrah_due = _radka_s_neco_ukolem[13]
        print(f"Úkol: " + str(_jmeno_ukolu_past_due))
        print(f"\tměl být splněn {_den_past_due}/{_mesic_past_due}/{_rok_past_due} v čase {_hodina_past_due}:{_minuta_past_due}. Byl jsi na něj upozorněn již {_pocet_vystrah_due}")
        print()
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

def PresunPodleCasuZAdoB(_cas, _souborA, _souborB, _Kolik_ma_zbyt,__omezeno_nulou = False):
    """podle zbávajícího času v sekundách přesune mezi soubory\n
    -\t omezeno nulou: True –> pokud má být hodnota ostře větší než 0 a zároveň menší než _kolik_má_zbýt"""

    with open(_souborA, "r") as _aa:
        radky = _aa.readlines()  # Přečte všechny řádky najednou
        _aktualni_r = 0
        if __omezeno_nulou == True:
            while (_aktualni_r) < (len(radky)):
                _radek_omezeno = radky[_aktualni_r]
                _datum_radky_omezeno = int( _radek_omezeno[0:12])
                __porovnavany_cas_datum_radky_omezeno = ZjistiStringNaSekundy(_datum_radky_omezeno)
                _zbyva_casu_omezeno = __porovnavany_cas_datum_radky_omezeno - _cas
                if ((_zbyva_casu_omezeno <= _Kolik_ma_zbyt) and (_zbyva_casu_omezeno > 0)):
                    PresunzAdoB(_souborA, _souborB, _aktualni_r+1)
                    radky.pop(_aktualni_r)  # Odstranění řádku, který byl právě zpracován, nepřidávám _aktualni_r protože jsem odstranil aktuální řádek
                else:
                    _aktualni_r += 1 
        if __omezeno_nulou == False:
            while (_aktualni_r) < (len(radky)):
                _radek = radky[_aktualni_r]
                _datum_radky = int(_radek[0:12])
                __porovnavany_cas_datum_radky = ZjistiStringNaSekundy(_datum_radky)
                _zbyva_casu = __porovnavany_cas_datum_radky - _cas
                if _zbyva_casu <= _Kolik_ma_zbyt:
                    PresunzAdoB(_souborA, _souborB, _aktualni_r+1)
                    radky.pop(_aktualni_r)  
                else:
                    _aktualni_r += 1  

from modul_casove_operace import ZjistiStringNaSekundy
def VypisHodinoveUkoly(_aktualni_cas,__soubor__s_post_ukoly):
    """ z souboru vypíšu úkoly, které mají po  splnění """
    #nechci měnit počet upozornění, jen na ně upozornit
    #######print(f"Jsem v hodinových úkolech")
    with open(__soubor__s_post_ukoly, 'r') as zdroj:
        
        zdroj__ = zdroj.readlines()
        for line in zdroj__: 
            if len(line) >10:#vyřešení problému s koncovou řádkou- mezerou na konci souboru
                __x_termin_ukolu = int(line[0:12])
                __c_termin_ukolu_sekundy = ZjistiStringNaSekundy(__x_termin_ukolu)
                __x_delta_casu = __c_termin_ukolu_sekundy - _aktualni_cas
                __nazev_ukolu_ = line[14:]
                VystrahaPo(__x_delta_casu,__nazev_ukolu_)
                VystrahaPred(__x_delta_casu,__nazev_ukolu_)
        ######print(f"zavření {__soubor__s_post_ukoly}")
def VypisUkolyKtereHori(_soubor_s_horicimi_ukoly):
    #neměním počet upozornění, jelikož zatím ještě zbývá čas na jejich splnění
    with open(_soubor_s_horicimi_ukoly, 'r') as zdroj:
        for line in zdroj: 
            if len(line) >12:#vyřešení problému s koncovou řádkou- mezerou na konci souboru
                VypisRadku(line,False)

def VystrahaPo(_zbyvajici_cas__,__nazev_ukolu_po_co_byl):
    """výstraha na úkoly po datu splnění, píše motivující hlášky s úkoly \n\t-1 až 2 hodiny po \n\t-24 až 26 hodin po """
    list_motiv1 = ["Chybí ti splnit úkol. Pusť se do toho, ať nemáš problém.","Nemáš splněný úkol. Ještě to můžeš dohnat a ušetřit si zbytečné starosti a čas.","Nevzdávej to! Překážky nejsou od toho, aby tě zastavily, ale posílily.","Nestresuj se z toho, že jsi úkol nestihl. Zkus se do něj pustit teď. A případně udělat aspoň kousek, který dokážeš nebo stihneš.",\
                   "Nikdy není pozdě, ještě to zkus.","Ještě není pozdě začít a dokončit to, co je potřeba.","Není důležité, kolikrát padneme, ale kolikrát se zvedneme.","Každý úspěch začíná rozhodnutím to zkusit. Dej se ještě do toho.","Netrap se tím, že jsi úkol nestihl a soustřeď se na něj teď."] #hodina až dvě po datu splnění
    ######print(f"Výstraha PO : zbývajícíc čas je {_zbyvajici_cas__}")
    if (_zbyvajici_cas__ >= -7200) and (_zbyvajici_cas__ <= -3600): 
        #výstraha 1 až 2 po 
        index_1 = random.randrange(0,len(list_motiv1))
        print("\t" + list_motiv1[index_1])
        print(f"\t!! Připomínám úkol: {__nazev_ukolu_po_co_byl}\n\tco jsi měl před {int(abs(_zbyvajici_cas__)/60)}min, vrhni se na něj!")
        print()
        return 
    if (-93600 <= _zbyvajici_cas__ <= -86400):
        #86 400 sekund = 24 hodin
        print(f"\t!! Uplynul den po termínu úkolu: {__nazev_ukolu_po_co_byl}\n\tPokud nejsi nemocný nebo úkol nebyl zrušen, zkus si zjistit informace o prokrastinaci a jak na ni vyzrát. Nebo se poraď s kvalifikovaným psychologem. Může ti to pomoct odhalit překážky, které ti brání v tom zažívat úspěch. Je to běžná věc, se kterou se nemusíš trápit a nemusíš být na ni sám.")
        print()
        return 

def VystrahaPred(_zbyvajici_cas__,__nazev__ukolu__pred):
    """vypíše motivující hlášku \n - 2 až 3 hodiny před splněním \n - 48 až 46 hodin před""" 
    list_motiv_pred_2_3 = ["Připomínám nesplněný úkol, pusť se do toho, ať nemáš problém.","Dívej se na celkový cíl a udělej úkol jako krok, který na cestě k němu potřebuješ.",\
                           "Teď je ideální čas ukázat, co dokážeš pod tlakem. Pusť se do toho hned.","Nyní je nejlepší čas začít, každá minuta se počítá, 3, 2, 1… start.",\
                            "Stále máš čas otočit situaci ve svůj prospěch a úkol odevzdat včas.","Vykašli se na to, co jsi měl udělat dříve a pusť se do toho, co můžeš udělat teď.",\
                            "Uvidíš, jak se budeš báječně cítit, když úkol dokončíš včas. Jdi do toho teď.","Stále máš šanci to zvládnout, udělej první krok teď.","Použij termín úkolu jako motivaci.",\
                            "Nepropadej panice, když začneš hned pracovat, máš šanci.","Každá akce, i ta malá, může teď udělat velký rozdíl. Běž do toho, stojí to za to.",\
                            "Využij zbylý čas k dosažení něčeho skvělého.","Každá minuta, kterou využiješ k plnění úkolu, tě přiblíží k celkovému cíli.","Máš sílu to zvládnout, když začneš teď.","Teď je čas být efektivní, go!"] 
    list_motiv_pred_48 = ["Máš ještě dostatek času na splnění úkolu. Udělej teď první malý krok. Bude bezva stihnout to včas.","Rozděl si úkol na malé části, ale první z nich udělej už teď. Být včas v cíli stojí za to.",\
                          "Zaměř se na malé kroky, každý z nich tě přiblíží k cíli, a ty tam budeš včas.","Nemusíš s úkolem spěchat, ale už nemáš čas s ním otálet. Každá minuta, kterou nad ním trávíš, se počítá. V přestávkách si vymysli, jak si po splnění úkolu udělat radost.",\
                            "Máš dostatek času, abys mohl pracovat efektivně a bez stresu. Využij ho a začni teď. ","Bude příjemné mít včas splněno.","Máš šanci připravit se bez spěchu a tlaku. Využij toho a pracuj na úkolu s klidem, který ti tento čas nabízí. Užij si cestu a hlavně dosažení cíle.",\
                            "Začít může být někdy nejtěžší částí. Udělej ten první krok, ať už je jakkoli malý. Pak už to půjde líp. Být v cíli stojí za to.","Přemýšlej o tom, jak skvěle se budeš cítit, až budeš mít hotovo dobře a včas.","Nech se motivovat časem, který máš. Je fajn mít v klidu hotovo."] 
    
    ########print(f"Výstraha PŘED : zbývajícíc čas je {_zbyvajici_cas__}")
    if (_zbyvajici_cas__ <= 10800) and (_zbyvajici_cas__ >= 7200): 
        #dvě až tři hodiny před  
        index_2_pred_23 = random.randrange(0,len(list_motiv_pred_2_3))
        print(f"\t!! Úkolu {__nazev__ukolu__pred} \n\tzbývá {((_zbyvajici_cas__/60)/60)}h do termínu splnění")
        print("\t" + list_motiv_pred_2_3[index_2_pred_23])
        print()
        return 

    if (165600 <= _zbyvajici_cas__ <= 172800): 
        #48 hodin před (až 46)
        print(f"\t!! Úkolu {__nazev__ukolu__pred}\n\tzbývá {((_zbyvajici_cas__/60)/60)}h do termínu splnění")
        index_2_pred_48 = random.randrange(0,len(list_motiv_pred_48))
        print("\t" + list_motiv_pred_48[index_2_pred_48])
        print()
        return 
    #####print("KONEC Před")
