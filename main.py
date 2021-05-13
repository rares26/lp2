# BMR = Rata metabolică bazală
def Date_despre_utilizator():
    vârsta = int ( input (' Introduceți vârsta dumneavoastră: '))
    sex = input ( ' Introduceți sexul dumneavoastră : ')
    greutatea = int ( input ( ' Introduceți greutatea dumneavoastră : '))
    înălțimea = int ( input ( ' Introduceți înalțimea dumneavoastră : '))

    if sex == 'Masculin':
        baza = 66.47
        îm = 5.003 * înălțimea
        gm = 13.75 * greutatea
        vm = 6.755 * vârsta
    elif sex == 'Feminin':
        baza = 655
        îm = 1.850 * înălțimea
        gm = 9.563 * greutatea
        vm = 4.676 * vârsta

    #BMR pentru barbați = 66.47 + (13.75 * greutatea [kg]) + (5.003 * înălțimea [cm]) − (6.755 * vârsta [ani])
    #BMR pentru femei = 655 + ( 9.563 × greutatea [kg] ) + ( 1.850 × înălțimea [cm] ) – ( 4.676 × vârsta [ani] )

    rezultatul_bmr = baza + îm + gm - vm
    return ( int ( rezultatul_bmr ) )

def Activitatea_utilizatorului( rezultatul_bmr ):
    Nivelul_de_activitate = input('Nivelul dumneavoastră de activitate ( sedentar , activitatea redusa , activ , foarte activ ):')


    if Nivelul_de_activitate == 'sedentar':
        Nivelul_de_activitate = 1.23 * rezultatul_bmr
    elif Nivelul_de_activitate == 'activitatea redusa':
        Nivelul_de_activitate = 1.4 * brezultatul_bmr
    elif Nivelul_de_activitate == 'activ':
        Nivelul_de_activitate = 1.6 * rezultatul_bmr
    elif Nivelul_de_activitate == 'foarte activ':
        Nivelul_de_activitate = 1.75 * rezultatul_bmr


    return ( int ( Nivelul_de_activitate ) )

def Așteptări(Nivelul_de_activitate):
    Scop = input('slabire , menținere , îngrășare : ')

    if Scop == 'slabire':
        calori = Nivelul_de_activitate - 500
    elif Scop == 'menținere':
        calori = Nivelul_de_activitate
    elif Scop == 'îngrășare':
        target = int ( input ( 'Doriți 1 sau 2 kg pe săptămână ') )
        if target == 1:
            calori = Nivelul_de_activitate + 500
        elif target == 2:
            calori = Nivelul_de_activitate + 1000

    print('Pentru a ', Scop, 'obiectivele calorile ar trebui sa fie ', int(calori), '!')


Așteptări(Activitatea_utilizatorului(Date_despre_utilizator()))
#
