import lab1
import numpy as np
import math
import sys
import random

k = 1 / 2 * (pow(5, 1 / 2) - 1)
koraci = 0  # ako koraci = 0 nema ispisa po koracima, inace ispis za svaki korak
h = 1  # korak za unimodalni interval


class fcija:
    def __init__(self, zadatak):
        self.broj_poziva = 0
        self.zadatak = zadatak

    # fcije jedne varijable
    def f(self, x):
        self.broj_poziva = self.broj_poziva + 1
        return pow(x - i_fcija_3, 2)

    # fcije vise varijabli
    def F(self, x):
        self.broj_poziva = self.broj_poziva + 1
        if self.zadatak == 1:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(0, 1)
            return 100 * pow(x2 - pow(x1, 2), 2) + pow(1 - x1, 2)
        elif self.zadatak == 2:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(0, 1)
            return pow(x1 - 4, 2) + 4 * pow(x2 - 2, 2)
        elif self.zadatak == 3:
            rez = 0
            for k in range(x.stupaca):
                one = x.dohvati_el(0, k)
                if i_fcija_3 == 0:
                    rez = rez + pow(one - k, 2)
                else:
                    rez = rez + pow(one - i_fcija_3, 2)
            return rez
        elif self.zadatak == 4:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(0, 1)
            return abs((x1 - x2) * (x1 + x2)) + pow(pow(x1, 2) + pow(x2, 2), 1 / 2)
        elif self.zadatak == 6:
            suma = 0
            for k in range(x.stupaca):
                one = x.dohvati_el(0, k)
                suma = suma + pow(one, 2)
            brojnik = pow(math.sin(suma), 2) - 0.5
            nazivnik = pow(1 + 0.001 * suma, 2)
            return 0.5 + brojnik / nazivnik

    # poziv fcije vise var sa zamjenom na i-tom indeksu
    def F_p(self, lambd, x, v):
        pom = x.zbroji_matrice(v.mnozenje_skalarom(lambd))
        return self.F(pom)

    def vrati_broj_poziva(self):
        return self.broj_poziva

    def resetiraj_broj_poziva(self):
        self.broj_poziva = 0


def zlatni_rez(*args):
    if len(args) == 2:  # zadana samo tocka i fcija
        x = args[0]
        zad = args[1]
        a, b = unimodalni_interval(x, zad)
    else:
        zad = args[2]
        a = min(args[0], args[1])
        b = max(args[0], args[1])
    print("Zlatni rez:")
    if koraci:
        print("Pocetno: a = " + str(a) + ", b = " + str(b))
    c = b - k * (b - a)
    d = a + k * (b - a)
    fc = zad.f(c)
    fd = zad.f(d)
    korak = 0
    while (b - a) > e:
        if koraci:
            print(str(korak) + ". korak:")
            print("a = " + str(a) + ", c = " + str(c) + ", d = " + str(d) + ", b = " + str(b))
            print("fc = " + str(fc) + ", fd = " + str(fd))
        if fc < fd:
            b = d
            d = c
            c = b - k * (b - a)
            fd = fc
            fc = zad.f(c)
        else:
            a = c
            c = d
            d = a + k * (b - a)
            fc = fd
            fd = zad.f(d)
        korak += 1
    return (a + b) / 2


def unimodalni_interval(tocka, zad):
    l = tocka - h
    r = tocka + h
    m = np.double(tocka)
    step = 1
    fm = zad.f(tocka)
    fl = zad.f(l)
    fr = zad.f(r)
    if fm < fr and fm < fl:
        return
    elif fm > fr:
        while fm > fr:
            l = m
            m = r
            fm = fr
            step *= 2
            r = tocka + h * step
            fr = zad.f(r)
    else:
        while fm > fl:
            r = m
            m = l
            fm = fl
            step *= 2
            l = tocka - h * step
            fl = zad.f(l)
    return l, r


def zlatni_rez_viseP(x, i, v, zad):
    a, b = unimodalni_interval_viseP(x, i, v, zad)
    if koraci:
        print("Pocetno: a = " + str(a) + ", b = " + str(b))
    c = b - k * (b - a)
    d = a + k * (b - a)
    fc = zad.F_p(c, x, v)
    fd = zad.F_p(d, x, v)
    korak = 0
    while (b - a) > e:
        if koraci:
            print(str(korak) + ". korak:")
            print("a = " + str(a) + ", c = " + str(c) + ", d = " + str(d) + ", b = " + str(b))
            print("fc = " + str(fc) + ", fd = " + str(fd))
        if fc < fd:
            b = d
            d = c
            c = b - k * (b - a)
            fd = fc
            fc = zad.F_p(c, x, v)
        else:
            a = c
            c = d
            d = a + k * (b - a)
            fc = fd
            fd = zad.F_p(d, x, v)
        korak += 1
    return (a + b) / 2


def unimodalni_interval_viseP(tocka1, i, v, zad):
    tocka = tocka1.dohvati_el(0, i)
    l = tocka - h
    r = tocka + h
    m = np.double(tocka)
    step = 1
    fm = zad.F_p(m, tocka1, v)
    fl = zad.F_p(l, tocka1, v)
    fr = zad.F_p(r, tocka1, v)
    if fm < fr and fm < fl:
        return l, r
    elif fm > fr:
        while fm > fr:
            l = m
            m = r
            fm = fr
            step *= 2
            r = tocka + h * step
            fr = zad.F_p(r, tocka1, v)
    else:
        while fm > fl:
            r = m
            m = l
            fm = fl
            step *= 2
            l = tocka - h * step
            fl = zad.F_p(l, tocka1, v)
    return l, r


# fcija odreduje nastavlja li se pretraga po koordinatnim osima
# ulazni parametri su matrica x, matrica xs i konstanta epsilon
# izlazni parametaran je boolean vrijednost koja oznacava nastavlja li se pretraga
def uvjet_nastavka_pretrage(x, xs, e):
    for i in range(x.stupaca):
        if abs(x.dohvati_el(0, i) - xs.dohvati_el(0, i)) > e:
            return True
    return False


def pretrazivanje_po_koordinantim_osima(x0, zad, e):
    ej = lab1.Matrica(x0.stupaca, x0.stupaca)
    for i in range(x0.stupaca):
        ej.postavi_el(i, i, 1)

    x = x0.pridruzivanje()
    xs = x.pridruzivanje()
    for i in range(x0.stupaca):
        red = ej.vrati_redak(i)
        lamb = zlatni_rez_viseP(x, i, red, zad)
        x.povecaj(0, i, lamb)

    while uvjet_nastavka_pretrage(x, xs, e):
        xs = x.pridruzivanje()
        for i in range(x0.stupaca):
            red = ej.vrati_redak(i)
            lamb = zlatni_rez_viseP(x, i, red, zad)
            x.povecaj(0, i, lamb)
    return x.matrica


# fcija odreduje nastavlja li se postupak
# ulazni parametri su lista vrijednosti fcije cilja, vrijednost fcije u tocki xc i konstanta epsilon
# izlazni parametaran je boolean vrijednost koja oznacava nastavlja li se postupak
def uvjet_nastavka(values, F_xc, e):
    rez = 0
    for one in values:
        rez = rez + pow(one - F_xc, 2)
    rez = rez / len(values)
    rez = pow(rez, 1 / 2)
    if rez > e:
        return True
    else:
        return False


# fcija racuna vrijednosti fcije cilja u zadanim tockama
# ulazni parametri su lista matrica x i fcija cilja
# izlazni parametar je lista vrijednosti fcije cilja
def vrijednosti(x, zad):
    rj = []
    for one in x:
        rj.append(zad.F(one))
    return rj


# fcija odreduje jeli F_xr veci od svakog clana liste values
# ulazni parametri su lista vrijedosti fcije cilja, indeks najlosije vrijednosti i iznos fcije cilja u tocki xr
# izlazni parametar je boolean vrijednost koja oznacava je li F_xr veci od svih clanova liste
def veci_za_svaki(values, h, F_xr):
    for j in range(len(values)):
        if j != h and F_xr <= values[j]:
            return False
    return True


# fcija racuna indekse na kojima se nalaze maksimum i minimum vrijednosti fcije cilja
# ulazni parametar je lista vrijednosti fcije cilja
# izlazni parametri su indeks na kojem se nalazi najveca i indeks na kojem se nalazi najmanja vrijednost fcije cilja
def izracunaj_h_l(values):
    h = l = 0
    max = min = values[0]
    for i in range(1, len(values)):
        if values[i] > max:
            h = i
            max = values[i]
        if values[i] < min:
            l = i
            min = values[i]
    return h, l


# fcija racuna centroid iz zadanih tocaka
# ulazni parametri su lista tocaka x i indeks tocke u kojoj fcija cilja poprima najlosiju vrijednost
# izlazni parametar je matrica koja predstavlja tocku koja je aritmeticka sredina tocaka iz liste bez one
# za koju ficja cilja poprima najlosiju vrijednost
def centroid(x, h):
    centroid = lab1.Matrica(x[0].redova, x[0].stupaca)
    for i in range(len(x)):
        if i != h:
            centroid = centroid.zbroji_matrice(x[i])
    centroid = centroid.mnozenje_skalarom(1 / (len(x) - 1))
    return centroid


def refleksija(xc, xh, alfa):
    return xc.mnozenje_skalarom(alfa + 1).oduzmi_matrice(xh.mnozenje_skalarom(alfa))


def ekspanzija(xc, xr, gama):
    return xc.mnozenje_skalarom(1 - gama).zbroji_matrice(xr.mnozenje_skalarom(gama))


def kontrakcija(xc, xh, beta):
    return xc.mnozenje_skalarom(1 - beta).zbroji_matrice(xh.mnozenje_skalarom(beta))


def pomak_prema_xl(x, l, sigma):
    rj = list()
    xl = x[l]
    for one in x:
        rj.append(one.zbroji_matrice(xl).mnozenje_skalarom(sigma))
    return rj


def simpleks_po_Nelderu_i_Meadu(x0, pomak, alfa, beta, gama, sigma, zad, e):
    x = list()
    x.append(x0)
    for i in range(x0.stupaca):
        pom = x0.pridruzivanje()
        pom.povecaj(0, i, pomak)
        x.append(pom)

    values = vrijednosti(x, zad)

    h, l = izracunaj_h_l(values)
    xc = centroid(x, h)
    xr = refleksija(xc, x[h], alfa)
    F_xr = zad.F(xr)
    korak = 1
    if F_xr < values[l]:
        xe = ekspanzija(xc, xr, gama)
        F_xe = zad.F(xe)
        if F_xe < values[l]:
            x[h] = xe
            values[h] = F_xe
        else:
            x[h] = xr
            values[h] = F_xr
    else:
        if veci_za_svaki(values, h, F_xr):
            if F_xr < values[h]:
                x[h] = xr
                values[h] = F_xr
            xk = kontrakcija(xc, x[h], beta)
            F_xk = zad.F(xk)
            if F_xk < values[h]:
                x[h] = xk
                values[h] = F_xk
            else:
                x = pomak_prema_xl(x, l, sigma)
        else:
            x[h] = xr
            values[h] = F_xr
    F_xc = zad.F(xc)
    if koraci:
        print(str(korak) + ". korak:")
        print("Centroid = ")
        xc.ispis_ekran()
        print("Vrijednost fcije u xc = " + str(F_xc))
    korak = korak + 1

    while uvjet_nastavka(values, F_xc, e):
        values = vrijednosti(x, zad)
        h, l = izracunaj_h_l(values)
        xc = centroid(x, h)
        xr = refleksija(xc, x[h], alfa)
        F_xr = zad.F(xr)
        if F_xr < values[l]:
            xe = ekspanzija(xc, xr, gama)
            F_xe = zad.F(xe)
            if F_xe < values[l]:
                x[h] = xe
                values[h] = F_xe
            else:
                x[h] = xr
                values[h] = F_xr
        else:
            if veci_za_svaki(values, h, F_xr):
                if F_xr < values[h]:
                    x[h] = xr
                    values[h] = F_xr
                xk = kontrakcija(xc, x[h], beta)
                F_xk = zad.F(xk)
                if F_xk < values[h]:
                    x[h] = xk
                    values[h] = F_xk
                else:
                    x = pomak_prema_xl(x, l, sigma)
            else:
                x[h] = xr
                values[h] = F_xr
        F_xc = zad.F(xc)
        if koraci:
            print(str(korak) + ". korak:")
            print("Centroid = ")
            xc.ispis_ekran()
            print("Vrijednost fcije u xc = " + str(F_xc))
        korak = korak + 1
    return xc.matrica


def Hooke_Jeeves(x0, dx, zad, e):
    xp = x0.pridruzivanje()
    xb = x0.pridruzivanje()
    korak = 0
    if koraci:
        print("Pocetno:")
        print("Bazna tocka = ")
        xb.ispis_ekran()
        print("Pocetna tocka pretrazivanja = ")
        xp.ispis_ekran()
    while dx > e:
        xn = istrazi(xp, dx, zad)
        if zad.F(xn) < zad.F(xb):
            xp = xn.mnozenje_skalarom(2).oduzmi_matrice(xb)
            xb = xn.pridruzivanje()
        else:
            dx = dx / 2
            xp = xb.pridruzivanje()
        if koraci:
            print(str(korak) + ". korak:")
            print("Bazna tocka = ")
            xb.ispis_ekran()
            print("Pocetna tocka pretrazivanja = ")
            xp.ispis_ekran()
            print("Tocka dobivena pretrazivanjem = ")
            xn.ispis_ekran()
        korak = korak + 1
    return xb.matrica


def istrazi(xp, dx, zad):
    x = xp.pridruzivanje()
    for i in range(xp.stupaca):
        P = zad.F(x)
        x.povecaj(0, i, dx)
        N = zad.F(x)
        if N > P:
            x.smanji(0, i, 2 * dx)
            N = zad.F(x)
            if N > P:
                x.povecaj(0, i, dx)
    return x


if __name__ == '__main__':
    f = open("izlaz2.txt", 'w')
    # sys.stdout = f

    # prvi zad
    ulaz = sys.argv[1]
    d = open(ulaz, encoding="utf8")
    par = d.read()
    par = par.split("\n")
    t = 0
    if par[0] == "tocka":
        t = 1
        x0 = np.double((par[1].split("=")[1]))
    else:
        l = par[1].split(",")
        a = float(l[0])
        b = float(l[1].split(" ")[1])
    e = float(par[2].split("=")[1])
    dx = float(par[3].split("=")[1])
    alfa = float(par[4].split("=")[1])
    beta = float(par[5].split("=")[1])
    gama = float(par[6].split("=")[1])
    sigma = float(par[7].split("=")[1])
    pomak = float(par[8].split("=")[1])

    print("1.")
    zadatak = 3
    i_fcija_3 = 3  # minimum u tocki 3
    zad = fcija(zadatak)
    if t:
        rez = zlatni_rez(x0, zad)
    else:
        rez = zlatni_rez(a, b, zad)
    print("rj = " + str(rez))
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    zad.resetiraj_broj_poziva()
    print()

    tocka = lab1.Matrica(1, 1, [[x0]])
    print("Pretrazivanje po koordinatnim osima:")
    rez = pretrazivanje_po_koordinantim_osima(tocka, zad, e)
    print("rj = " + str(rez))
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    zad.resetiraj_broj_poziva()
    print()

    rez = simpleks_po_Nelderu_i_Meadu(tocka, pomak, alfa, beta, gama, sigma, zad, e)
    print("Simpleks po Nelderu i Meadu:")
    print("rj = " + str(rez))
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    zad.resetiraj_broj_poziva()
    print()

    rez = Hooke_Jeeves(tocka, dx, zad, e)
    print("Postupak  Hooke-Jeeves:")
    print("rj = " + str(rez))
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    zad.resetiraj_broj_poziva()
    i_fcija_3 = 0
    print()

    # drugi zad
    ulaz = sys.argv[2]
    d = open(ulaz, encoding="utf8")
    par = d.read()
    par = par.split("\n")
    t1 = par[0].split(",")
    for i in range(len(t1)):
        t1[i] = np.double(t1[i])
    t1 = lab1.Matrica(1, len(t1), [t1])
    t2 = par[1].split(",")
    for i in range(len(t2)):
        t2[i] = np.double(t2[i])
    t2 = lab1.Matrica(1, len(t2), [t2])
    t3 = par[2].split(",")
    for i in range(len(t3)):
        t3[i] = np.double(t3[i])
    t3 = lab1.Matrica(1, len(t3), [t3])
    t4 = par[3].split(",")
    for i in range(len(t4)):
        t4[i] = np.double(t4[i])
    t4 = lab1.Matrica(1, len(t4), [t4])
    e = float(par[4].split("=")[1])
    dx = float(par[5].split("=")[1])
    alfa = float(par[6].split("=")[1])
    beta = float(par[7].split("=")[1])
    gama = float(par[8].split("=")[1])
    sigma = float(par[9].split("=")[1])
    pomak = float(par[10].split("=")[1])
    print("2.")
    t = [t1, t2, t3, t4]
    for i in range(4):
        tocka = t[i]
        zadatak = i + 1
        zad = fcija(zadatak)
        print("Funkcija " + str(i + 1))

        rez = simpleks_po_Nelderu_i_Meadu(tocka, pomak, alfa, beta, gama, sigma, zad, e)
        print("Simpleks po Nelderu i Meadu\t" + str(rez) + "\t" + str(zad.vrati_broj_poziva()))
        zad.resetiraj_broj_poziva()

        rez = Hooke_Jeeves(tocka, dx, zad, e)
        print("Postupak  Hooke-Jeeves:\t" + str(rez) + "\t" + str(zad.vrati_broj_poziva()))
        zad.resetiraj_broj_poziva()

        rez = pretrazivanje_po_koordinantim_osima(tocka, zad, e)
        print("Po koorinatnim osima:\t" + str(rez) + "\t" + str(zad.vrati_broj_poziva()))
        zad.resetiraj_broj_poziva()
        print()

    # treci zad
    ulaz = sys.argv[3]
    d = open(ulaz, encoding="utf8")
    par = d.read()
    par = par.split("\n")
    t = par[0].split(",")
    for i in range(len(t)):
        t[i] = np.double(t[i])
    t = lab1.Matrica(1, len(t), [t])
    e = float(par[1].split("=")[1])
    dx = float(par[2].split("=")[1])
    alfa = float(par[3].split("=")[1])
    beta = float(par[4].split("=")[1])
    gama = float(par[5].split("=")[1])
    sigma = float(par[6].split("=")[1])
    pomak = float(par[7].split("=")[1])

    print("3.")
    zadatak = 4
    zad = fcija(zadatak)

    rez = simpleks_po_Nelderu_i_Meadu(t, pomak, alfa, beta, gama, sigma, zad, e)
    print("Simpleks po Nelderu i Meadu\t" + str(rez) + "\t" + str(zad.vrati_broj_poziva()))
    zad.resetiraj_broj_poziva()

    rez = Hooke_Jeeves(t, dx, zad, e)
    print("Postupak  Hooke-Jeeves:\t" + str(rez) + "\t" + str(zad.vrati_broj_poziva()))
    zad.resetiraj_broj_poziva()
    print()

    # cetvrti zad
    ulaz = sys.argv[4]
    d = open(ulaz, encoding="utf8")
    par = d.read()
    par = par.split("\n")
    t = par[0].split(",")
    for i in range(len(t)):
        t[i] = np.double(t[i])
    t = lab1.Matrica(1, len(t), [t])
    e = float(par[1].split("=")[1])
    dx = float(par[2].split("=")[1])
    alfa = float(par[3].split("=")[1])
    beta = float(par[4].split("=")[1])
    gama = float(par[5].split("=")[1])
    sigma = float(par[6].split("=")[1])

    print("4.")
    zadatak = 1
    zad = fcija(zadatak)

    print("Pocetno x0 = ", end="")
    t.ispis_ekran()
    for pomak in range(1, 21):
        rez = simpleks_po_Nelderu_i_Meadu(t, pomak, alfa, beta, gama, sigma, zad, e)
        print("Pomak = " + str(pomak) + "\t" + str(rez) + "\t" + str(zad.vrati_broj_poziva()))
        zad.resetiraj_broj_poziva()

    print()
    t = lab1.Matrica(1, 2, [[20, 20]])
    print("Pocetno x0 = ", end="")
    t.ispis_ekran()
    for pomak in range(1, 21):
        rez = simpleks_po_Nelderu_i_Meadu(t, pomak, alfa, beta, gama, sigma, zad, e)
        print("Pomak = " + str(pomak) + "\t" + str(rez) + "\t" + str(zad.vrati_broj_poziva()))
        zad.resetiraj_broj_poziva()
    print()

    # peti zad
    print("5.")
    zadatak = 6
    zad = fcija(zadatak)
    min = [0, 0]

    krivih_h = 0
    krivih_s = 0
    N = 10000
    for i in range(N):
        num1 = random.randint(-50, 50)
        num2 = random.randint(-50, 50)
        t = lab1.Matrica(1, 2, [[num1, num2]])
        rez = Hooke_Jeeves(t, dx, zad, e)
        tocnost = "true"
        for i in range(len(min)):
            if abs(min[i] - rez[0][i]) > 0.0001:
                tocnost = "false"
                krivih_h = krivih_h + 1
                break
        # print("Postupak  Hooke-Jeeves:\t" + str(rez) + "\t" + str(zad.vrati_broj_poziva()) + "\t" + tocnost)
        zad.resetiraj_broj_poziva()

    print("Postotak tocnih uz koristenje Hooke - Jeeves postupka = " + str(100 * (N - krivih_h) / N) + " %")
    f.close()
