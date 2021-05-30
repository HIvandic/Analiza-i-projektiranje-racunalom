import lab1
import math
import sys
import matplotlib.pyplot as plt


# varijabla odreduje hoce li se ispisivati koraci rjesenja ili samo krajnje rjesenje
koraci = False


# klasa implementira fciju r(t) koja ovisi o vremenu
class r_c:
    # inicijalizacija objekta
    # ulazni parametar jer jedna od 3 moguce fcije
    def __init__(self, zad):
        self.zad = zad

    # fcija racuna r(t)
    # ulazni parametar je vrijeme (t)
    # izlazni parametar jer matrica koja predstavlja r(t)
    def r(self, t):
        if self.zad == 0:
            return lab1.Matrica(2, 1, [[0], [0]])
        elif self.zad == 1:
            return lab1.Matrica(2, 1, [[1], [1]])
        else:
            return lab1.Matrica(2, 1, [[t], [t]])


# fcija provodi trapezni postupak
# ulazni parametri su matrica A, matrica B, vrijednost x u trenutku t = 0, korak integracije, vremenski interval,
# korak za ispis te fcija r(t)
# izlazni parametri su matrica zadnje dobivene vrijednosti i rjecnik u kojem je kljuc vrijeme, a vrijednost
# izracunati x u tom trenutku
def trapezni_postupak(A, B, x0, T, tmax, korak, r_f):
    lista = []
    rj = dict()

    # stvaranje jedinicne matrice
    for i in range(A.redova):
        pom = list()
        for j in range(A.stupaca):
            if i == j:
                pom.append(1)
            else:
                pom.append(0)
        lista.append(pom)

    # omogucavanje eksplicitnog oblika
    U = lab1.Matrica(A.redova, A.stupaca, lista)
    pom = U.oduzmi_matrice(A.mnozenje_skalarom(T/2)).inverz()
    R = pom.pomnozi_matrice(U.zbroji_matrice(A.mnozenje_skalarom(T/2)))
    S = pom.mnozenje_skalarom(T/2).pomnozi_matrice(B)

    xc = x0.pridruzivanje()
    t = T
    iteracija = 0

    while t <= tmax:
        iteracija += 1
        xc = R.pomnozi_matrice(xc).zbroji_matrice(S.pomnozi_matrice(r_f.r(t).zbroji_matrice(r_f.r(t + T))))
        rj[t] = xc.matrica
        if koraci and iteracija % korak == 0:
            print(str(iteracija) + ". iteracija:")
            xc.ispis_ekran()
        t += T
    return xc, rj


# fcija provodi Eulerov postupak
# ulazni parametri su matrica A, matrica B, vrijednost x u trenutku t = 0, korak integracije, vremenski interval,
# korak za ispis te fcija r(t)
# izlazni parametri su matrica zadnje dobivene vrijednosti i rjecnik u kojem je kljuc vrijeme, a vrijednost
# izracunati x u tom trenutku
def eulerov_postupak(A, B, x0, T, tmax, korak, r_f):
    rj = dict()
    xc = x0.pridruzivanje()
    t = T
    iteracija = 0

    while t <= tmax:
        iteracija += 1
        der = A.pomnozi_matrice(xc).zbroji_matrice(B.pomnozi_matrice(r_f.r(t)))
        xc = xc.zbroji_matrice(der.mnozenje_skalarom(T))
        rj[t] = xc.matrica
        if koraci and iteracija % korak == 0:
            print(str(iteracija) + ". iteracija:")
            xc.ispis_ekran()
        t += T
    return xc, rj


# fcija provodi obrnuti Eulerov postupak
# ulazni parametri su matrica A, matrica B, vrijednost x u trenutku t = 0, korak integracije, vremenski interval,
# korak za ispis te fcija r(t)
# izlazni parametri su matrica zadnje dobivene vrijednosti i rjecnik u kojem je kljuc vrijeme, a vrijednost
# izracunati x u tom trenutku
def obrnuti_eulerov_postupak(A, B, x0, T, tmax, korak, r_f):
    lista = []
    rj = dict()

    # stvaranje jedinicne matrice
    for i in range(A.redova):
        pom = list()
        for j in range(A.stupaca):
            if i == j:
                pom.append(1)
            else:
                pom.append(0)
        lista.append(pom)

    # omogucavanje eksplicitnog oblika
    U = lab1.Matrica(A.redova, A.stupaca, lista)
    pom = U.oduzmi_matrice(A.mnozenje_skalarom(T)).inverz()
    P = pom.pridruzivanje()
    Q = pom.mnozenje_skalarom(T).pomnozi_matrice(B)

    xc = x0.pridruzivanje()
    t = T
    iteracija = 0

    while t <= tmax:
        iteracija += 1
        xc = P.pomnozi_matrice(xc).zbroji_matrice(Q.pomnozi_matrice(r_f.r(t + T)))
        rj[t] = xc.matrica
        if koraci and iteracija % korak == 0:
            print(str(iteracija) + ". iteracija:")
            xc.ispis_ekran()
        t += T
    return xc, rj


# fcija provodi Runge-Kutta postupak 4. reda
# ulazni parametri su matrica A, matrica B, vrijednost x u trenutku t = 0, korak integracije, vremenski interval,
# korak za ispis te fcija r(t)
# izlazni parametri su matrica zadnje dobivene vrijednosti i rjecnik u kojem je kljuc vrijeme, a vrijednost
# izracunati x u tom trenutku
def runge_kutta_4(A, B, x0, T, tmax, korak, r_f):
    rj = dict()
    xc = x0.pridruzivanje()
    t = T
    iteracija = 0

    while t <= tmax:
        iteracija += 1
        m1 = A.pomnozi_matrice(xc).zbroji_matrice(B.pomnozi_matrice(r_f.r(t)))
        m2 = A.pomnozi_matrice(xc.zbroji_matrice(m1.mnozenje_skalarom(T/2))).zbroji_matrice(B.pomnozi_matrice(r_f.r(t + T/2)))
        m3 = A.pomnozi_matrice(xc.zbroji_matrice(m2.mnozenje_skalarom(T/2))).zbroji_matrice(B.pomnozi_matrice(r_f.r(t + T/2)))
        m4 = A.pomnozi_matrice(xc.zbroji_matrice(m3.mnozenje_skalarom(T))).zbroji_matrice(B.pomnozi_matrice(r_f.r(t + T)))
        xc = xc.zbroji_matrice((m1.zbroji_matrice(m2.mnozenje_skalarom(2)).zbroji_matrice(m3.mnozenje_skalarom(2))
                                .zbroji_matrice(m4)).mnozenje_skalarom(T/6))
        rj[t] = xc.matrica
        if koraci and iteracija % korak == 0:
            print(str(iteracija) + ". iteracija:")
            xc.ispis_ekran()
        t += T
    return xc, rj


# fcija provodi prediktorsko-korektorski postupak
# ulazni parametri su prediktor (vrijednost koja oznacava hoce li predikor biti Eulerov ili RUnge-Kutta postupak,
# korektor (vrijednost koja oznacava hoce li korektor biti obrnuti Eulerov ili trapezni postupak,
# korektor_iteracija (vrijednost koja oznacava koliko se puta provodi korekcija), matrica A, matrica B,
# vrijednost x u trenutku t = 0, korak integracije, vremenski interval, korak za ispis te fcija r(t)
# izlazni parametri su matrica zadnje dobivene vrijednosti i rjecnik u kojem je kljuc vrijeme, a vrijednost
# izracunati x u tom trenutku
def prediktorsko_korektorski(prediktor, korektor, korektor_iteracija, A, B, x0, T, tmax, korak, r_f):
    rj = dict()
    xc = x0.pridruzivanje()
    t = T
    iteracija = 0

    while t <= tmax:
        iteracija += 1
        # prediktor
        # Eulerov postupak
        if prediktor:
            der = A.pomnozi_matrice(xc).zbroji_matrice(B.pomnozi_matrice(r_f.r(t)))
            xp = xc.zbroji_matrice(der.mnozenje_skalarom(T))

        # Runge-Kutta 4. reda
        else:
            m1 = A.pomnozi_matrice(xc).zbroji_matrice(B.pomnozi_matrice(r_f.r(t)))
            m2 = A.pomnozi_matrice(xc.zbroji_matrice(m1.mnozenje_skalarom(T / 2))).zbroji_matrice(
                B.pomnozi_matrice(r_f.r(t + T / 2)))
            m3 = A.pomnozi_matrice(xc.zbroji_matrice(m2.mnozenje_skalarom(T / 2))).zbroji_matrice(
                B.pomnozi_matrice(r_f.r(t + T / 2)))
            m4 = A.pomnozi_matrice(xc.zbroji_matrice(m3.mnozenje_skalarom(T))).zbroji_matrice(
                B.pomnozi_matrice(r_f.r(t + T)))
            xp = xc.zbroji_matrice((m1.zbroji_matrice(m2.mnozenje_skalarom(2)).zbroji_matrice(m3.mnozenje_skalarom(2))
                                    .zbroji_matrice(m4)).mnozenje_skalarom(T / 6))
        # korektor
        for i in range(korektor_iteracija):
            # obrnuti Eulerov postupak
            if korektor:
                der_2 = A.pomnozi_matrice(xp).zbroji_matrice(B.pomnozi_matrice(r_f.r(t + T)))
                xp = xc.zbroji_matrice(der_2.mnozenje_skalarom(T))

            # trapezni postupak
            else:
                xk = A.pomnozi_matrice(xc).zbroji_matrice(B.pomnozi_matrice(r_f.r(t)))
                xk1 = A.pomnozi_matrice(xp).zbroji_matrice(B.pomnozi_matrice(r_f.r(t + T)))
                der_2 = xk.zbroji_matrice(xk1)
                xp = xc.zbroji_matrice(der_2.mnozenje_skalarom(T/2))

        xc = xp.pridruzivanje()
        rj[t] = xc.matrica
        if koraci and iteracija % korak == 0:
            print(str(iteracija) + ". iteracija:")
            xc.ispis_ekran()
        t += T
    return xc, rj


# fcija poziva prediktorsko-korektorski postupak uz Eulerov postupak kao prediktor i obrnuti Eulerov postupak
# kao korektor koji se poziva dva puta
# ulazni parametri su matrica A, matrica B, vrijednost x u trenutku t = 0, korak integracije, vremenski interval,
# korak za ispis te fcija r(t)
# izlazni parametri su povratne vrijednosti prediktorsko-korektorskog postupka
def pe_ce_2(A, B, x0, T, tmax, korak, r_f):
    # prediktor Euler, korektor obrnuti Euler
    return prediktorsko_korektorski(True, True, 2, A, B, x0, T, tmax, korak, r_f)


# fcija poziva prediktorsko-korektorski postupak uz Eulerov postupak kao prediktor i trapezni postupak
# kao korektor koji se poziva jednom
# ulazni parametri su matrica A, matrica B, vrijednost x u trenutku t = 0, korak integracije, vremenski interval,
# korak za ispis te fcija r(t)
# izlazni parametri su povratne vrijednosti prediktorsko-korektorskog postupka
def pe_ce(A, B, x0, T, tmax, korak, r_f):
    # prediktor Euler, korektor trapezni
    return prediktorsko_korektorski(True, False, 1, A, B, x0, T, tmax, korak, r_f)


# fcija pretvara niz brojeva odvojenih zarezom (,) ili tocka zarezom (;) u matricu
# ulazni parametar je string sastavljen od niza brojeva
# izlazni parametar je matrica nastala iz dobivenog stringa
def uredi(ulaz):
    lista = []
    redovi = ulaz.split(";")
    redova = 0
    stupaca = 0
    first = True
    for one in redovi:
        pom = []
        clanovi = one.split(",")
        for clan in clanovi:
            pom.append(int(clan))
            if first:
                stupaca += 1
        first = False
        redova += 1
        lista.append(pom)
    return lab1.Matrica(redova, stupaca, lista)


if __name__ == '__main__':
    ime = ["./peti/lab5_1.txt", "./peti/lab5_2.txt", "./peti/lab5_3.txt", "./peti/lab5_4.txt"]
    f = open("izlaz5.txt", 'w')
    sys.stdout = f

    # prvi zad
    print("1. zadatak")
    f = open(ime[0], encoding="utf8")
    it = 0
    for line in f:
        line = line.strip()
        pom = line.split("=")
        if it == 0:
            A = uredi(pom[1])
        elif it == 1:
            x0 = uredi(pom[1])
        elif it == 2:
            T = float(pom[1])
        else:
            tmax = float(pom[1])
        it += 1

    r_f = r_c(0)
    korak = 5
    B = lab1.Matrica(2, 2, [[0, 0], [0, 0]])

    # racunanje stvarne vrijednosti
    real = dict()
    t = T
    x1_0 = float(x0.dohvati_el(0, 0))
    x2_0 = float(x0.dohvati_el(1, 0))
    time = []
    while t <= tmax:
        time.append(t)
        x1 = x1_0 * math.cos(t) + x2_0 * math.sin(t)
        x2 = x2_0 * math.cos(t) - x1_0 * math.sin(t)
        real[t] = [x1, x2]
        t += T

    print("Eulerov postupak:")
    xc, rj = eulerov_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    pogreska = [0, 0]
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x_real = real[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
        pogreska[0] += abs(x_calc[0][0] - x_real[0])
        pogreska[1] += abs(x_calc[1][0] - x_real[1])
    print("Pogreska = ", end="")
    print(pogreska)
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("1. zadatak, Eulerov postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\Euler_1.png")'''

    print("\nObrnuti Eulerov postupak:")
    xc, rj = obrnuti_eulerov_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    pogreska = [0, 0]
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x_real = real[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
        pogreska[0] += abs(x_calc[0][0] - x_real[0])
        pogreska[1] += abs(x_calc[1][0] - x_real[1])
    print("Pogreska = ", end="")
    print(pogreska)
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("1. zadatak, obrnuti Eulerov postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\obrnuti_Euler_1.png")'''

    print("\nTrapezni postupak:")
    xc, rj = trapezni_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    pogreska = [0, 0]
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x_real = real[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
        pogreska[0] += abs(x_calc[0][0] - x_real[0])
        pogreska[1] += abs(x_calc[1][0] - x_real[1])
    print("Pogreska = ", end="")
    print(pogreska)
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("1. zadatak, Trapezni postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\trapezni_1.png")'''

    print("\nPostupak Runge-Kutta 4. reda:")
    xc, rj = runge_kutta_4(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    pogreska = [0, 0]
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x_real = real[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
        pogreska[0] += abs(x_calc[0][0] - x_real[0])
        pogreska[1] += abs(x_calc[1][0] - x_real[1])
    print("Pogreska = ", end="")
    print(pogreska)
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("1. zadatak, Postupak Runge-Kutta 4. reda")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\runge_kutta_1.png")'''

    print("\nPrediktorsko-korektorski postupak (pe(ce)^2):")
    xc, rj = pe_ce_2(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    pogreska = [0, 0]
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x_real = real[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
        pogreska[0] += abs(x_calc[0][0] - x_real[0])
        pogreska[1] += abs(x_calc[1][0] - x_real[1])
    print("Pogreska = ", end="")
    print(pogreska)
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("1. zadatak, Prediktorsko-korektorski postupak pe(ce)^2")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\pecece_1.png")'''

    print("\nPrediktorsko-korektorski postupak (pece):")
    xc, rj = pe_ce(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    pogreska = [0, 0]
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x_real = real[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
        pogreska[0] += abs(x_calc[0][0] - x_real[0])
        pogreska[1] += abs(x_calc[1][0] - x_real[1])
    print("Pogreska = ", end="")
    print(pogreska)
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("1. zadatak, Prediktorsko-korektorski postupak (pece)")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\pece_1.png")'''

    # drugi zad
    print("\n2. zadatak")
    f = open(ime[1], encoding="utf8")
    it = 0
    for line in f:
        line = line.strip()
        pom = line.split("=")
        if it == 0:
            A = uredi(pom[1])
        elif it == 1:
            x0 = uredi(pom[1])
        elif it == 2:
            T = float(pom[1])
        else:
            tmax = float(pom[1])
        it += 1

    r_f = r_c(0)
    B = lab1.Matrica(2, 2, [[0, 0], [0, 0]])

    print("Eulerov postupak:")
    xc, rj = eulerov_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    time = []
    x1 = []
    x2 = []
    for key in rj.keys():
        time.append(key)
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("2. zadatak, Eulerov postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\Euler_2.png")'''

    print("\nObrnuti Eulerov postupak:")
    xc, rj = obrnuti_eulerov_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("2. zadatak, Obrnuti Eulerov postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\obrnuti_Euler_2.png")'''


    print("\nTrapezni postupak:")
    xc, rj = trapezni_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("2. zadatak, Trapezni postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\trapezni_2.png")'''

    print("\nPostupak Runge-Kutta 4. reda:")
    xc, rj = runge_kutta_4(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("2. zadatak, Postupak Runge-Kutta 4. reda")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\runge_kutta_2.png")'''

    print("\nPrediktorsko-korektorski postupak (pe(ce)^2):")
    xc, rj = pe_ce_2(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("2. zadatak, Prediktorsko-korektorski postupak (pe(ce)^2)")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\pecece_2.png")'''

    print("\nPrediktorsko-korektorski postupak (pece):")
    xc, rj = pe_ce(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("2. zadatak, Prediktorsko-korektorski postupak (pece)")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\pece_2.png")'''

    # isprobavanje runge-kutta za razlicite korake integracije
    print("\nPostupak Runge-Kutta 4. reda za razlicite korake integracije")
    for i in range(1, 11):
        T = i/100
        print("Za T = " + str(T) + ":")
        xc, rj = runge_kutta_4(A, B, x0, T, tmax, korak, r_f)
        print(xc.matrica)

    # treci zad
    print("\n3. zadatak")
    f = open(ime[2], encoding="utf8")
    it = 0
    for line in f:
        line = line.strip()
        pom = line.split("=")
        if it == 0:
            A = uredi(pom[1])
        elif it == 1:
            B = uredi(pom[1])
        elif it == 2:
            x0 = uredi(pom[1])
        elif it == 3:
            T = float(pom[1])
        else:
            tmax = float(pom[1])
        it += 1

    r_f = r_c(1)

    print("Eulerov postupak:")
    xc, rj = eulerov_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    time = []
    x1 = []
    x2 = []
    for key in rj.keys():
        time.append(key)
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("3. zadatak, Eulerov postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\Euler_3.png")'''

    print("\nObrnuti Eulerov postupak:")
    xc, rj = obrnuti_eulerov_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("3. zadatak, Obrnuti Eulerov postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\obrnuti_Euler_3.png")'''

    print("\nTrapezni postupak:")
    xc, rj = trapezni_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("3. zadatak, Trapezni postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\trapezni_3.png")'''

    print("\nPostupak Runge-Kutta 4. reda:")
    xc, rj = runge_kutta_4(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("3. zadatak, Postupak Runge-Kutta 4. reda")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\runge_kutta_3.png")'''

    print("\nPrediktorsko-korektorski postupak (pe(ce)^2):")
    xc, rj = pe_ce_2(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("3. zadatak, Prediktorsko-korektorski postupak (pe(ce)^2)")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\pecece_3.png")'''

    print("\nPrediktorsko-korektorski postupak (pece):")
    xc, rj = pe_ce(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("3. zadatak, Prediktorsko-korektorski postupak (pece)")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\pece_3.png")'''

    # cetvrti zad
    print("\n4. zadatak")
    f = open(ime[3], encoding="utf8")
    it = 0
    for line in f:
        line = line.strip()
        pom = line.split("=")
        if it == 0:
            A = uredi(pom[1])
        elif it == 1:
            B = uredi(pom[1])
        elif it == 2:
            x0 = uredi(pom[1])
        elif it == 3:
            T = float(pom[1])
        else:
            tmax = float(pom[1])
        it += 1

    r_f = r_c(2)

    print("Eulerov postupak:")
    xc, rj = eulerov_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    time = []
    x1 = []
    x2 = []
    for key in rj.keys():
        time.append(key)
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("4. zadatak, Eulerov postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\Euler_4.png")'''

    print("\nObrnuti Eulerov postupak:")
    xc, rj = obrnuti_eulerov_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("4. zadatak, Obrnuti Eulerov postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\obrnuti_Euler_4.png")'''

    print("\nTrapezni postupak:")
    xc, rj = trapezni_postupak(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("4. zadatak, Trapezni postupak")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\trapezni_4.png")'''

    print("\nPostupak Runge-Kutta 4. reda:")
    xc, rj = runge_kutta_4(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("4. zadatak, Postupak Runge-Kutta 4. reda")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\runge_kutta_4.png")'''

    print("\nPrediktorsko-korektorski postupak (pe(ce)^2):")
    xc, rj = pe_ce_2(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("4. zadatak, Prediktorsko-korektorski postupak (pe(ce)^2)")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\pecece_4.png")'''

    print("\nPrediktorsko-korektorski postupak (pece):")
    xc, rj = pe_ce(A, B, x0, T, tmax, korak, r_f)
    print(xc.matrica)
    x1 = []
    x2 = []
    for key in rj.keys():
        x_calc = rj[key]
        x1.append(x_calc[0][0])
        x2.append(x_calc[1][0])
    '''plt.plot(time, x1, "red")
    plt.plot(time, x2, "blue")
    plt.title("4. zadatak, Prediktorsko-korektorski postupak (pece)")
    plt.savefig("C:\\Users\\Hana\\Desktop\\Faks\\diplomski\\1. godina\\Apr\\5.lab\\pece_4.png")'''
