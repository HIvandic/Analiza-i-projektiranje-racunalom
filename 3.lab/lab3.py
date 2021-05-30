import math
import sys

import numpy as np
import lab1
import random
k = 1 / 2 * (pow(5, 1 / 2) - 1)
koraci = 0
h = 1


class fcija3:
    def __init__(self, zadatak):
        self.broj_poziva = 0
        self.zadatak = zadatak

    # fcije vise varijabli
    def F(self, x):
        self.broj_poziva = self.broj_poziva + 1
        if self.zadatak == 1:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            return 100 * pow(x2 - pow(x1, 2), 2) + pow(1 - x1, 2)
        elif self.zadatak == 2:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            return pow(x1 - 4, 2) + 4 * pow(x2 - 2, 2)
        elif self.zadatak == 3:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            return pow(x1 - 2, 2) + pow(x2 + 3, 2)
        elif self.zadatak == 4:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            return pow(x1 - 3, 2) + pow(x2, 2)

    def F_p(self, lambd, x, v):
        pom = x.zbroji_matrice(v.mnozenje_skalarom(lambd))
        return self.F(pom)

    def vrati_broj_poziva(self):
        return self.broj_poziva

    def resetiraj_broj_poziva(self):
        self.broj_poziva = 0


class gradijenti:
    def __init__(self, zadatak):
        self.broj_poziva = 0
        self.zadatak = zadatak

    # fcije vise varijabli
    def racunaj_gradijent(self, x):
        self.broj_poziva = self.broj_poziva + 1
        if self.zadatak == 1:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            d1 = -400 * (x2 - pow(x1, 2)) * x1 - 2 * (1 - x1)
            d2 = 200 * (x2 - pow(x1, 2))
            m = lab1.Matrica(2, 1)
            m.postavi_el(0, 0, d1)
            m.postavi_el(1, 0, d2)
            return m
        elif self.zadatak == 2:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            d1 = 2 * (x1 - 4)
            d2 = 8 * (x2 - 2)
            m = lab1.Matrica(2, 1)
            m.postavi_el(0, 0, d1)
            m.postavi_el(1, 0, d2)
            return m
        elif self.zadatak == 3:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            d1 = 2 * (x1 - 2)
            d2 = 2 * (x2 + 3)
            m = lab1.Matrica(2, 1)
            m.postavi_el(0, 0, d1)
            m.postavi_el(1, 0, d2)
            return m
        elif self.zadatak == 4:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            d1 = 2 * (x1 - 3)
            d2 = 2 * x2
            m = lab1.Matrica(2, 1)
            m.postavi_el(0, 0, d1)
            m.postavi_el(1, 0, d2)
            return m

    def vrati_broj_poziva(self):
        return self.broj_poziva

    def resetiraj_broj_poziva(self):
        self.broj_poziva = 0


class hesseova:
    def __init__(self, zadatak):
        self.broj_poziva = 0
        self.zadatak = zadatak

    def racunaj_hesseovu(self, x):
        self.broj_poziva = self.broj_poziva + 1
        if self.zadatak == 1:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            d11 = -400 * (x2 - pow(x1, 2)) * x1 + 800 * pow(x1, 2) + 2
            d12 = -400 * x1
            d21 = -400 * x1
            d22 = 200
            m = lab1.Matrica(2, 2)
            m.postavi_el(0, 0, d11)
            m.postavi_el(0, 1, d12)
            m.postavi_el(1, 0, d21)
            m.postavi_el(1, 1, d22)
            return m
        elif self.zadatak == 2:
            d11 = 2
            d12 = 0
            d21 = 0
            d22 = 8
            m = lab1.Matrica(2, 2)
            m.postavi_el(0, 0, d11)
            m.postavi_el(0, 1, d12)
            m.postavi_el(1, 0, d21)
            m.postavi_el(1, 1, d22)
            return m
        elif self.zadatak == 3:
            d11 = 2
            d12 = 0
            d21 = 0
            d22 = 2
            m = lab1.Matrica(2, 2)
            m.postavi_el(0, 0, d11)
            m.postavi_el(0, 1, d12)
            m.postavi_el(1, 0, d21)
            m.postavi_el(1, 1, d22)
            return m
        elif self.zadatak == 4:
            d11 = 2
            d12 = 0
            d21 = 0
            d22 = 2
            m = lab1.Matrica(2, 2)
            m.postavi_el(0, 0, d11)
            m.postavi_el(0, 1, d12)
            m.postavi_el(1, 0, d21)
            m.postavi_el(1, 1, d22)
            return m

    def vrati_broj_poziva(self):
        return self.broj_poziva

    def resetiraj_broj_poziva(self):
        self.broj_poziva = 0



class ogranicenja_nejednakosti:
    def __init__(self, ogranicenje):
        self.broj_poziva = 0
        self.ogranicenje = ogranicenje

    def provjeri_ogranicenja(self, x):
        self.broj_poziva = self.broj_poziva + 1
        if self.ogranicenje == 1:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            return x2 - x1
        elif self.ogranicenje == 2:
            x1 = x.dohvati_el(0, 0)
            return 2 - x1
        elif self.ogranicenje == 3:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            return 3 - x2 - x1
        elif self.ogranicenje == 4:
            x1 = x.dohvati_el(0, 0)
            x2 = x.dohvati_el(1, 0)
            return 3 + 1.5 * x1 - x2

    def vrati_broj_poziva(self):
        return self.broj_poziva

    def resetiraj_broj_poziva(self):
        self.broj_poziva = 0


class ogranicenja_jednakosti:
    def __init__(self, ogranicenje):
        self.broj_poziva = 0
        self.ogranicenje = ogranicenje

    def provjeri_ogranicenja(self, x):
        self.broj_poziva = self.broj_poziva + 1
        if self.ogranicenje == 1:
            x2 = x.dohvati_el(1, 0)
            return x2 - 1

    def vrati_broj_poziva(self):
        return self.broj_poziva

    def resetiraj_broj_poziva(self):
        self.broj_poziva = 0


def zlatni_rez(x, v, zad):
    a, b = unimodalni_interval(x, v, zad)
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


def unimodalni_interval(tocka1, v, zad):
    tocka = 0
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


# fcija racuna normu zadanog vektora
# ulazni parametar e vektor
# izlazni parametar je norma
def norma(x):
    rj = 0
    for i in range(x.redova):
        rj = rj + pow(x.dohvati_el(i, 0), 2)
    return pow(rj, 1/2)


# fcija provodi postupak gradijentnog spusta
# ulazni parametri su preciznost, početna točka, metoda (ako = 1 zlatni rez) i zadatak
# izlazni parametri su pronadena tocka i broj poziva racunanja gradijenta
def gradijenti_spust(e, x0, metoda, zad):
    grad = gradijenti(zad.zadatak)
    gradijent = grad.racunaj_gradijent(x0)
    prev = zad.F(x0)
    ponavljanje = 0

    while norma(gradijent) >= e:
        if metoda:
            lambd = zlatni_rez(x0, gradijent, zad)
            x0 = x0.zbroji_matrice(gradijent.mnozenje_skalarom(lambd))
        else:
            x0 = x0.oduzmi_matrice(gradijent)

        trenutni = zad.F(x0)
        if trenutni == prev:
            ponavljanje += 1
            if ponavljanje >= 100:
                print("Divergencija, prekidam")
                return None, None
        else:
            ponavljanje = 0
            prev = trenutni
        gradijent = grad.racunaj_gradijent(x0)

    return x0, grad.vrati_broj_poziva()


# fcija normira vektor
# ulazni parametar je vektor
# izlazni parametar je normirani vektor
def normiraj(delta_x):
    norm = norma(delta_x)
    for i in range(delta_x.redova):
        delta_x.postavi_el(i, 0, delta_x.dohvati_el(i, 0)/norm)
    return delta_x


# fcija provodi newton-raphsonov postupak
# ulazni parametri su preciznost, početna točka, metoda (ako = 1 zlatni rez) i zadatak
# izlazni parametri su pronadena tocka, broj poziva racunanja gradijenta i broj poziva racunanja Hesseove matrice
def newton_raphson(e, x0, metoda, zad):
    grad = gradijenti(zad.zadatak)
    gradijent = grad.racunaj_gradijent(x0)
    hess = hesseova(zad.zadatak)
    hesseova_matrica = hess.racunaj_hesseovu(x0)
    delta_x = hesseova_matrica.rijesiLUP(gradijent.mnozenje_skalarom(-1))

    prev = zad.F(x0)
    ponavljanje = 0
    k = 0
    e10 = lab1.Matrica(x0.redova, 1)
    e10.postavi_el(0, 0, 1)
    e01 = lab1.Matrica(x0.redova, 1)
    e01.postavi_el(1, 0, 1)
    while norma(delta_x) >= e:
        if metoda:
            pom1 = e10.mnozenje_skalarom(delta_x.dohvati_el(0, 0))
            lambd = zlatni_rez(x0, pom1, zad)
            x0 = x0.zbroji_matrice(pom1.mnozenje_skalarom(lambd))
            pom2 = e01.mnozenje_skalarom(delta_x.dohvati_el(1, 0))
            lambd = zlatni_rez(x0, pom2, zad)
            x0 = x0.zbroji_matrice(pom2.mnozenje_skalarom(lambd))
            ##delta_x = normiraj(delta_x)
            # lambd = zlatni_rez(x0, delta_x, zad)
            # x0 = x0.zbroji_matrice(delta_x.mnozenje_skalarom(lambd))
        else:
            x0 = x0.zbroji_matrice(delta_x.mnozenje_skalarom(-1))

        trenutni = zad.F(x0)
        if trenutni == prev:
            ponavljanje += 1
            if ponavljanje >= 100:
                print("Divergencija, prekidam")
                return None, None, None
        else:
            ponavljanje = 0
            prev = trenutni

        gradijent = grad.racunaj_gradijent(x0)
        hesseova_matrica = hess.racunaj_hesseovu(x0)
        delta_x = hesseova_matrica.rijesiLUP(gradijent)
        k = k + 1
        if k > 10000:
            print("Divergencija, prekidam")
            return None, None, None
    return x0, grad.vrati_broj_poziva(), hess.vrati_broj_poziva()


# fcija proverava je li tocka x0 u zadanim granicama
# ulazni parametri su tocka x0 te gornja i donja granica za svaku varijablu
# izlazni parametar je boolean vrijednost koja oznacava zadovoljava li tocka ogranicenja
def provjeri(x0, xd, xg):
    for i in range(x0.redova):
        el = x0.dohvati_el(i, 0)
        if el < xd.dohvati_el(i, 0) or el > xg.dohvati_el(i, 0):
            return False
    return True


# fcija racuna vrijednosti fcije cilja u zadanim tockama
# ulazni parametri su lista matrica x i fcija cilja
# izlazni parametar je lista vrijednosti fcije cilja
def vrijednosti(x, zad):
    rj = []
    for one in x:
        rj.append(zad.F(one))
    return rj


# fcija racuna centroid iz zadanih tocaka
# ulazni parametri su lista tocaka x i indeks tocke u kojoj fcija cilja poprima najlosiju vrijednost
# izlazni parametar je matrica koja predstavlja tocku koja je aritmeticka sredina tocaka iz liste bez one
# za koju ficja cilja poprima najlosiju vrijednost
def centroid(x, h):
    centroid = lab1.Matrica(x[0].redova, x[0].stupaca)
    for i in range(len(x)):
        if i != h:
            centroid = centroid.zbroji_matrice(x[i])
    if h is None:
        return centroid.mnozenje_skalarom(1 / len(x))

    centroid = centroid.mnozenje_skalarom(1 / (len(x) - 1))
    return centroid


# fcija racuna indekse na kojima se nalaze maksimum i drugi idući maksimum fcije cilja
# ulazni parametar je lista vrijednosti fcije cilja
# izlazni parametri su indeks na kojem se nalazi najveca i indeks na kojem se nalazi druga najveća vrijednost fcije cilja
def izracunaj_h_h2(values):
    h = 0
    max = values[0]
    h2 = 0
    max2 = values[0]

    for i in range(1, len(values)):
        if values[i] > max:
            h = i
            max = values[i]

    if h == 0:
        h2 = 1
        max2 = values[1]
    for i in range(1, len(values)):
        if i != h and values[i] > max2:
            h2 = i
            max2 = values[i]
    return h, h2


def refleksija(xc, xh, alfa):
    return xc.mnozenje_skalarom(alfa + 1).oduzmi_matrice(xh.mnozenje_skalarom(alfa))


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


def provjera_ogr(x0, ogr):
    for one in ogr:
        if one.provjeri_ogranicenja(x0) < 0:
            return False
    return True


# fcija provodi postupak po boxu
# ulazni parametri su preciznost, alfa, početna točka, zadatak, eksplicitna i implicitna ogranicenja
# izlazni parametar je pronadena tocka
def postupak_po_boxu(e, alfa, x0, zad, xd, xg, ogr):
    if not provjeri(x0, xd, xg) or not provjera_ogr(x0, ogr):
        print("Pocetna tocka ne zadovoljava ogranicenja")
        return None

    xc = x0
    x = list()

    for t in range(2 * x0.redova):
        v = lab1.Matrica(x0.redova, 1)
        for i in range(x0.redova):
            R = random.random() * (1 - 0) + 0
            v.postavi_el(i, 0, xd.dohvati_el(i, 0) + R * (xg.dohvati_el(i, 0) - xd.dohvati_el(i, 0)))
        x.append(v)
        while not provjera_ogr(x[t], ogr):
            x.append(x.pop().zbroji_matrice(xc).mnozenje_skalarom(1/2))
        xc = centroid(x, None)

    values = vrijednosti(x, zad)
    F_xc = zad.F(xc)
    prev = F_xc
    ponavljanje = 0
    uvjet = True

    while uvjet:
        h, h2 = izracunaj_h_h2(values)
        xc = centroid(x, h)
        xr = refleksija(xc, x[h], alfa)

        for i in range(x0.redova):
            if xr.dohvati_el(i, 0) < xd.dohvati_el(i, 0):
                xr.postavi_el(i, 0, xd.dohvati_el(i, 0))
            elif xr.dohvati_el(i, 0) > xg.dohvati_el(i, 0):
                xr.postavi_el(i, 0, xg.dohvati_el(i, 0))
        while not provjera_ogr(xr, ogr):
            xr = xr.zbroji_matrice(xc).mnozenje_skalarom(1 / 2)

        value_h = zad.F(xr)
        if value_h > values[h2]:
            xr = xr.zbroji_matrice(xc).mnozenje_skalarom(1 / 2)
            value_h = zad.F(xr)
        values[h] = value_h
        x[h] = xr

        trenutni = zad.F(xc)
        if trenutni == prev:
            ponavljanje += 1
            if ponavljanje >= 100:
                print("Divergencija, prekidam")
                return None
        else:
            ponavljanje = 0
            prev = trenutni
        uvjet = uvjet_nastavka(values, trenutni, e)

    return xc


def Hooke_Jeeves(x0, dx, zad, e, t, ogranicenja_nejed, ogranicenja_jed):
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
        xn = istrazi(xp, dx, zad, t, ogranicenja_nejed, ogranicenja_jed)
        if racunaj_novu_fciju(xn, zad, t, ogranicenja_nejed, ogranicenja_jed) < racunaj_novu_fciju(xb, zad, t, ogranicenja_nejed, ogranicenja_jed):
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

    return xb


def istrazi(xp, dx, zad, t, ogranicenja_nejed, ogranicenja_jed):
    x = xp.pridruzivanje()
    for i in range(xp.redova):
        P = racunaj_novu_fciju(x, zad, t, ogranicenja_nejed, ogranicenja_jed)
        x.povecaj(i, 0, dx)
        N = racunaj_novu_fciju(x, zad, t, ogranicenja_nejed, ogranicenja_jed)

        if N > P:
            x.smanji(i, 0, 2 * dx)
            N = racunaj_novu_fciju(x, zad, t, ogranicenja_nejed, ogranicenja_jed)
            if N > P:
                x.povecaj(i, 0, dx)
    return x


def racunaj_novu_fciju(x0, zad, t, ogranicenja_nejed, ogranicenja_jed):
    rez = zad.F(x0)
    if ogranicenja_nejed is not None:
        for one in ogranicenja_nejed:
            iznos = one.provjeri_ogranicenja(x0)
            if iznos <= 0:
                return float('inf')
            else:
                rez -= 1/t * math.log(iznos)

    if ogranicenja_jed is not None:
        for one in ogranicenja_jed:
            iznos = one.provjeri_ogranicenja(x0)
            rez += t * pow(iznos, 2)
    return rez


def trazi_unutarnju_tocku(x0, ogranicenja_nejed, dx):
    xp = x0.pridruzivanje()
    xb = x0.pridruzivanje()
    korak = 0

    if koraci:
        print("Pocetno:")
        print("Bazna tocka = ")
        xb.ispis_ekran()
        print("Pocetna tocka pretrazivanja = ")
        xp.ispis_ekran()

    while G(xb, ogranicenja_nejed) != 0:
        xn = nadi(xp, dx, ogranicenja_nejed)
        if G(xn, ogranicenja_nejed) < G(xb, ogranicenja_nejed):
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

    return xb


def nadi(xp, dx, ogranicenja_nejed):
    x = xp.pridruzivanje()
    for i in range(xp.redova):
        P = G(x, ogranicenja_nejed)
        x.povecaj(i, 0, dx)
        N = G(x, ogranicenja_nejed)
        if N > P:
            x.smanji(i, 0, 2 * dx)
            N = G(x, ogranicenja_nejed)
            if N > P:
                x.povecaj(i, 0, dx)
    return x


# fcija koja se koristi pri trazenju unutarnje tocke
# ulazni parametri su tocka i ogranicenja nejednakosti
# izlazni parametar je vrijednost fcije G (0 ako je tocka u dozvoljenom podrucju)
def G(x, ogranicenja_nejed):
    g = 0
    for one in ogranicenja_nejed:
        iznos = one.provjeri_ogranicenja(x)
        if iznos < 0:
            g -= iznos
    return g


#fcija ispisuje tocku
def ispisi_kao_red(x0):
    first = True
    for i in range(x0.redova):
        if first:
            first = False
        else:
            print(", ", end="")
        print(x0.dohvati_el(i, 0), end="")
    print()


def transformacija_na_mjesoviti_nacin(e, t, x0, zad, ogranicenja_nejed, ogranicenja_jed, dx):
    zastavica = 0
    for one in ogranicenja_nejed:
        if one.provjeri_ogranicenja(x0) < 0:
            x0 = trazi_unutarnju_tocku(x0, ogranicenja_nejed, dx)
            zastavica = 1

    if zastavica:
        print("Unutrasnja tocka: ", end="")
        ispisi_kao_red(x0)
    x = Hooke_Jeeves(x0, dx, zad, e, t, ogranicenja_nejed, ogranicenja_jed)
    prev = zad.F(x)
    ponavljanje = 0

    while udaljenost(x, x0) > e:
        t = t * 10
        x0 = x
        x = Hooke_Jeeves(x0, dx, zad, e, t, ogranicenja_nejed, ogranicenja_jed)
        trenutni = zad.F(x)
        if trenutni == prev:
            ponavljanje += 1
            if ponavljanje >= 100:
                print("Divergencija, prekidam")
                return None
        else:
            ponavljanje = 0
            prev = trenutni

    return x


# fcija racuna udaljenost dvije tocke
# ulazni parametri su dvije tocke
# izlazni parametar je udaljenost zadanih tocaka
def udaljenost(x, x0):
    dist = 0
    for i in range(x.redova):
        dist += pow(x.dohvati_el(i, 0) - x0.dohvati_el(i, 0), 2)
    return pow(dist, 1/2)


f = open("izlaz3.txt", 'w')
sys.stdout = f

# prvi zad
print("1.")
print("Uz odredivanje optimalnog iznosa koraka:")
ulaz = sys.argv[1]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
metoda = float(par[2].split("=")[1])
zadatak = 3
zad = fcija3(zadatak)

rez, br_poziva = gradijenti_spust(e, x0, metoda, zad)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print(str(br_poziva) + " racunanja gradijenta")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

print("Bez odredivanja optimalnog iznosa koraka:")
ulaz = sys.argv[2]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
metoda = float(par[2].split("=")[1])
zadatak = 3
zad = fcija3(zadatak)

rez, br_poziva = gradijenti_spust(e, x0, metoda, zad)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print(str(br_poziva) + " racunanja gradijenta")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

# drugi zad
print("2.")
print("Postupak gradijentnog spusta za fciju 1:")
ulaz = sys.argv[3]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
metoda = float(par[2].split("=")[1])
zadatak = 1
zad = fcija3(zadatak)

rez, br_poziva = gradijenti_spust(e, x0, metoda, zad)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print(str(br_poziva) + " racunanja gradijenta")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

print("Newton-Raphsonov postupak za fciju 1:")
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])

rez, br_poziva, br_poziva2 = newton_raphson(e, x0, metoda, zad)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print(str(br_poziva) + " racunanja gradijenta")
    print(str(br_poziva2) + " racunanja Hesseove matrice")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

print("Postupak gradijentnog spusta za fciju 2:")
ulaz = sys.argv[4]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
metoda = float(par[2].split("=")[1])
zadatak = 2
zad = fcija3(zadatak)

rez, br_poziva = gradijenti_spust(e, x0, metoda, zad)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print(str(br_poziva) + " racunanja gradijenta")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

print("Newton-Raphsonov postupak za fciju 2:")
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])

rez, br_poziva, br_poziva2 = newton_raphson(e, x0, metoda, zad)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print(str(br_poziva) + " racunanja gradijenta")
    print(str(br_poziva2) + " racunanja Hesseove matrice")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

# treci zad
print("3.")
print("Boxov postupak za fciju 1:")
ulaz = sys.argv[5]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
alfa = float(par[2].split("=")[1])
zadatak = 1
zad = fcija3(zadatak)
xd = lab1.Matrica(2, 1)
xd.postavi_el(0, 0, -100)
xd.postavi_el(1, 0, -100)
xg = lab1.Matrica(2, 1)
xg.postavi_el(0, 0, 100)
xg.postavi_el(1, 0, 100)
ogr = list()
ogr1 = ogranicenja_nejednakosti(1)
ogr2 = ogranicenja_nejednakosti(2)
ogr.append(ogr1)
ogr.append(ogr2)

rez = postupak_po_boxu(e, alfa, x0, zad, xd, xg, ogr)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

print("Boxov postupak za fciju 2:")
ulaz = sys.argv[6]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
alfa = float(par[2].split("=")[1])
zadatak = 2
zad = fcija3(zadatak)
xd = lab1.Matrica(2, 1)
xd.postavi_el(0, 0, -100)
xd.postavi_el(1, 0, -100)
xg = lab1.Matrica(2, 1)
xg.postavi_el(0, 0, 100)
xg.postavi_el(1, 0, 100)

rez = postupak_po_boxu(e, alfa, x0, zad, xd, xg, ogr)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

# cetvrti zad
print("4.")
print("Postupak transformacije u oblik bez ogranicenja za fciju 1:")
ulaz = sys.argv[7]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
t = float(par[2].split("=")[1])
zadatak = 1
zad = fcija3(zadatak)
xd = lab1.Matrica(2, 1)
dx = 1

ogranicenja_nejed = list()
ogr1 = ogranicenja_nejednakosti(1)
ogr2 = ogranicenja_nejednakosti(2)
ogranicenja_nejed.append(ogr1)
ogranicenja_nejed.append(ogr2)
ogranicenja_jed = None

rez = transformacija_na_mjesoviti_nacin(e, t, x0, zad, ogranicenja_nejed, ogranicenja_jed, dx)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

print("Postupak transformacije u oblik bez ogranicenja za fciju 2:")
ulaz = sys.argv[8]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
t = float(par[2].split("=")[1])
zadatak = 2
zad = fcija3(zadatak)
xd = lab1.Matrica(2, 1)
dx = 1

ogranicenja_nejed = list()
ogr1 = ogranicenja_nejednakosti(1)
ogr2 = ogranicenja_nejednakosti(2)
ogranicenja_nejed.append(ogr1)
ogranicenja_nejed.append(ogr2)
ogranicenja_jed = None

rez = transformacija_na_mjesoviti_nacin(e, t, x0, zad, ogranicenja_nejed, ogranicenja_jed, dx)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

# peti zad
print("5.")
print("Postupak transformacije u oblik bez ogranicenja za fciju 4:")
ulaz = sys.argv[9]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
print("Pocetna tocka: " + str(tocka[0]) + ", " + str(tocka[1]))
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
t = float(par[2].split("=")[1])
zadatak = 4
zad = fcija3(zadatak)
xd = lab1.Matrica(2, 1)
dx = 1

ogranicenja_nejed = list()
ogr1 = ogranicenja_nejednakosti(3)
ogr2 = ogranicenja_nejednakosti(4)
ogranicenja_nejed.append(ogr1)
ogranicenja_nejed.append(ogr2)
ogranicenja_jed = list()
ogr3 = ogranicenja_jednakosti(1)
ogranicenja_jed.append(ogr3)

rez = transformacija_na_mjesoviti_nacin(e, t, x0, zad, ogranicenja_nejed, ogranicenja_jed, dx)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()

print("Postupak transformacije u oblik bez ogranicenja za fciju 4:")
ulaz = sys.argv[10]
d = open(ulaz, encoding="utf8")

par = d.read()
par = par.split("\n")
tocka = par[0].split(",")
print("Pocetna tocka: " + str(tocka[0]) + ", " + str(tocka[1]))
x0 = lab1.Matrica(2, 1)
x0.postavi_el(0, 0, tocka[0])
x0.postavi_el(1, 0, tocka[1])
e = float(par[1].split("=")[1])
t = float(par[2].split("=")[1])
zadatak = 4
zad = fcija3(zadatak)
xd = lab1.Matrica(2, 1)
dx = 1

ogranicenja_nejed = list()
ogr1 = ogranicenja_nejednakosti(3)
ogr2 = ogranicenja_nejednakosti(4)
ogranicenja_nejed.append(ogr1)
ogranicenja_nejed.append(ogr2)
ogranicenja_jed = list()
ogr3 = ogranicenja_jednakosti(1)
ogranicenja_jed.append(ogr3)

rez = transformacija_na_mjesoviti_nacin(e, t, x0, zad, ogranicenja_nejed, ogranicenja_jed, dx)
if rez is not None:
    rez.ispis_ekran()
    print()
    print(str(zad.vrati_broj_poziva()) + " evaluacija funkcije")
    print("Vrijednost funkcije u dobivenoj tocki = " + str(zad.F(rez)))
zad.resetiraj_broj_poziva()
print()
