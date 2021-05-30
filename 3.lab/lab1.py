import numpy as np

konst = 0.00000000001
# varijabla koraci odreduje ispisuje li se medukoraci algoritma
# ako je postavljena na 0, ispisuje se samo krajnje rjesenje
# inace ispisuje i medukorake
koraci = 0

# zapis rjesenja u datoteku izlaz
izlaz = 'izlaz.txt'
d = open(izlaz, "w")


class Matrica:
    def __init__(self, redova=0, stupaca=0, lista=None):
        self.redova = redova
        self.stupaca = stupaca
        if lista is not None:
            self.matrica = lista
        else:
            self.matrica = []
            for i in range(self.redova):
                pom = []
                for j in range(self.stupaca):
                    pom.append(0)
                self.matrica.append(pom)

    # fcija cita matricu iz datoteke, ulazni parametar je ime datoteke, nema izlaznih parametara
    def citaj(self, ime):
        f = open(ime, encoding="utf8")
        i = 0
        self.matrica = []
        self.redova = self.stupaca = 0
        for line in f:
            line = line.strip()
            pom = line.split()
            for k in range(len(pom)):
                pom[k] = np.double(pom[k])
            self.matrica.append(pom)
            self.redova += 1
            if i == 0:
                self.stupaca = len(pom)
                i = 1
            elif len(pom) != self.stupaca:
                print("Neodgovrajuci broj elemenata u redu")
                print("Ovaj red ima " + str(len(pom)) + " elemenata umjesto potrebnih " + str(self.stupaca))

    # fcija ispisuje matricu na ekran, nema ni ulaznih niti izlaznih parametara
    def ispis_ekran(self):
        for i in range(self.redova):
            prvi_s = 0
            for j in range(self.stupaca):
                if prvi_s == 0:
                    prvi_s = 1
                    if str(self.matrica[i][j]) == "-0.0":
                        print(str(abs(self.matrica[i][j])), end="")
                    else:
                        print(str(self.matrica[i][j]), end="")
                else:
                    if str(self.matrica[i][j]) == "-0.0":
                        print(" " + str(abs(self.matrica[i][j])), end="")
                    else:
                        print(" " + str(self.matrica[i][j]), end="")
            print()

    # fcija ispisuje matricu u datoteku, ulazni parametar je ime datoteke, nema izlaznih parametara
    def ispis_dat(self, ime):
        f = open(ime, "w")
        prvi_r = 0
        for i in range(self.redova):
            if prvi_r == 0:
                prvi_r = 1
            else:
                f.write("\n")
            prvi_s = 0
            for j in range(self.stupaca):
                if prvi_s == 0:
                    prvi_s = 1
                    if str(self.matrica[i][j]) == "-0.0":
                        f.write(str(abs(self.matrica[i][j])))
                    else:
                        f.write(str(self.matrica[i][j]))
                else:
                    if str(self.matrica[i][j]) == "-0.0":
                        f.write(" " + str(abs(self.matrica[i][j])))
                    else:
                        f.write(" " + str(self.matrica[i][j]))

    # fcija ispisuje matricu u vec otvorenu datoteku, nema ni ulaznih niti izlaznih parametara
    def dopisi(self):
        prvi_r = 0
        for i in range(self.redova):
            if prvi_r == 0:
                prvi_r = 1
            else:
                d.write("\n")
            prvi_s = 0
            for j in range(self.stupaca):
                if prvi_s == 0:
                    prvi_s = 1
                    if str(self.matrica[i][j]) == "-0.0":
                        d.write(str(abs(self.matrica[i][j])))
                    else:
                        d.write(str(self.matrica[i][j]))
                else:
                    if str(self.matrica[i][j]) == "-0.0":
                        d.write(" " + str(abs(self.matrica[i][j])))
                    else:
                        d.write(" " + str(self.matrica[i][j]))
        d.write("\n")

    # fcija postavlja element matrice na definiranu vrijednost
    # ulazni parametri su redak i stupac elementa matrice te vrijednost na koju se postavlja
    # izlaznih parametara nema
    def postavi_el(self, redak, stupac, vrijednost):
        self.matrica[redak][stupac] = np.double(vrijednost)

    # fcija vraca element matrice
    # ulazni parametri su redak i stupac elementa koji se dohvaca
    # izlazni parametar je vrijednost trazenog elementa u matrici
    def dohvati_el(self, redak, stupac):
        return self.matrica[redak][stupac]

    # fcija stvara novu matricu jednaku trenutnoj
    # nema ulaznih parametara, izlazni parametar je novodobivena matrica
    def pridruzivanje(self):
        matr = []
        for i in range(self.redova):
            pom = []
            for j in range(self.stupaca):
                pom.append(self.matrica[i][j])
            matr.append(pom)
        return Matrica(self.redova, self.stupaca, matr)

    # fcija obavlja += zeljenog elementa matrice
    # ulazni parametri su redak i stupac elementa matrice koji se povecava te vrijednost za koju se zeli povecati
    # izlaznih parametara nema
    def povecaj(self, redak, stupac, vrijednost):
        self.matrica[redak][stupac] += vrijednost

    # fcija obavlja -= zeljenog elementa matrice
    # ulazni parametri su redak i stupac elementa matrice koji se smanjuje te vrijednost za koju se zeli smanjiti
    # izlaznih parametara nema
    def smanji(self, redak, stupac, vrijednost):
        self.matrica[redak][stupac] -= vrijednost

    # fcija zbraja matrice
    # ulazni parametar je matrica koja se pribraja trenutnoj
    # izlazni parametar je novostvorena matrica dobivena zbrojem
    def zbroji_matrice(self, druga):
        if (self.redova != druga.redova) | (self.stupaca != druga.stupaca):
            print("Nije moguce zbrojiti zeljene matrice (neodgovarajuce dimenzije)")
            return None
        matr = []
        for i in range(self.redova):
            pom = []
            for j in range(self.stupaca):
                pom.append(self.matrica[i][j] + druga.matrica[i][j])
            matr.append(pom)
        return Matrica(self.redova, self.stupaca, matr)

    # fcija oduzima matrice
    # ulazni parametar je matrica koja se oduzima od trenutne
    # izlazni parametar je novostvorena matrica dobivena razlikom
    def oduzmi_matrice(self, druga):
        if (self.redova != druga.redova) | (self.stupaca != druga.stupaca):
            print("Nije moguce oduzeti zeljene matrice (neodgovarajuce dimenzije)")
            return None
        matr = []
        for i in range(self.redova):
            pom = []
            for j in range(self.stupaca):
                pom.append(self.matrica[i][j] - druga.matrica[i][j])
            matr.append(pom)
        return Matrica(self.redova, self.stupaca, matr)

    # fcija mnozi matrice
    # ulazni parametar je matrica koja se mnozi s trenutnom
    # izlazni parametar je novostvorena matrica dobivena umnoskom
    def pomnozi_matrice(self, druga):
        if self.stupaca != druga.redova:
            print("Nije moguce pomnoziti zeljene matrice (neodgovarajuce dimenzije)")
            return None
        matr = []
        for i in range(self.redova):
            pom = []
            for j in range(druga.stupaca):
                c = 0
                for k in range(self.stupaca):
                    c += self.matrica[i][k] * druga.matrica[k][j]
                pom.append(c)
            matr.append(pom)
        return Matrica(self.redova, druga.stupaca, matr)

    # fcija transponira matricu
    # ulaznih parametara nema, izlazni parametar je transponirana matrica
    def transponiraj_matricu(self):
        matr = Matrica(self.stupaca, self.redova)
        for i in range(self.redova):
            for j in range(i, self.stupaca):
                if i == j:
                    matr.postavi_el(i, j, self.matrica[i][j])
                    continue
                p = self.matrica[i][j]
                matr.postavi_el(i, j, self.matrica[j][i])
                matr.postavi_el(j, i, p)
        return matr

    # fcija mnozi matricu skalarom
    # ulazni parametar je skalar kojim se mnozi matrica
    # izlazni parametar je matrica nastala umnoskom trenutne matrice sa skalarom
    def mnozenje_skalarom(self, value):
        matr = []
        for i in range(self.redova):
            pom = []
            for j in range(self.stupaca):
                pom.append(self.matrica[i][j] * value)
            matr.append(pom)
        return Matrica(self.redova, self.stupaca, matr)

    # fcija provjerava jesu li dvije matrice jednake
    # ulazni parametar je matrica koja se usporeduje s trenutnom
    # izlazni parametar je boolean vrijednost koja govori jesu li matrice jednake (True) ili ne (False)
    def jesu_li_jednake(self, druga):
        if (self.redova != druga.redova) | (self.stupaca != druga.stupaca):
            return False
        for i in range(self.redova):
            for j in range(self.stupaca):
                if abs(self.matrica[i][j] - druga.matrica[i][j]) > konst:
                    return False
        return True

    # dorada fcije == za usporedbu matrica
    # ulazni parametar je matrica koja se usporeduje s trenutnom
    # izlazni parametar je boolean vrijednost koja govori jesu li matrice jednake (True) ili ne (False)
    def __eq__(self, other):
        if (self.redova != other.redova) | (self.stupaca != other.stupaca):
            return False
        for i in range(self.redova):
            for j in range(self.stupaca):
                if abs(self.matrica[i][j] - other.matrica[i][j]) > konst:
                    return False
        return True

    # fcija provodi supstituciju unaprijed
    # ulazni parametar je vektor b, izlazni parametar je y (vrijednost nakon supstitucije unaprijed)
    def supstitucijaUnaprijed(self, b):
        if self.redova != self.stupaca:
            print("Matrica nije kvadratna")
            d.write("Matrica nije kvadratna\n")
            return None
        elif self.redova != b.redova:
            print("Neogovarajuci broj redaka")
            d.write("Neodgovarajuci broj redaka\n")
            return None
        elif b.stupaca != 1:
            print("Vektor b mora imati samo jedan stupac")
            d.write("Vektor b mora imati samo jedan stupac\n")
            return None
        for i in range(self.redova - 1):
            for j in range(i + 1, self.stupaca):
                b.matrica[j][0] -= self.matrica[j][i] * b.matrica[i][0]
        return b

    # fcija provodi supstituciju unatrag
    # ulazni parametar je vektor y
    # izlazni parametar je x (vrijednost nakon supstitucije unatrag)
    def supstitucijaUnatrag(self, y):
        if self.redova != self.stupaca:
            print("Matrica nije kvadratna")
            d.write("Matrica nije kvadratna\n")
            return None
        elif self.redova != y.redova:
            print("Neogovarajući broj redaka")
            d.write("Neodgovarajuci broj redaka\n")
            return None
        elif y.stupaca != 1:
            print("Vektor b mora imati samo jedan stupac")
            d.write("Vektor b mora imati samo jedan stupac\n")
            return None
        for i in range(self.redova - 1, -1, -1):
            if abs(self.dohvati_el(i, i)) < konst:
                print("Vrijednost manja od zadane granične, zaustavlja se")
                d.write("Vrijednost manja od zadane granicne, zaustavlja se\n")
                return None
            y.matrica[i][0] /= self.matrica[i][i]
            for j in range(i):
                y.matrica[j][0] -= self.matrica[j][i] * y.matrica[i][0]
        return y

    # fcija provodi LU dekompozicju matrice
    # ulaznih parametara nema, izlazni parametar je dekomponirana matrica
    def dekompozicijaLU(self):
        if self.redova != self.stupaca:
            print("Matrica nije kvadratna")
            d.write("Matrica nije kvadratna\n")
            return None
        for i in range(self.redova - 1):
            for j in range(i + 1, self.stupaca):
                if abs(self.dohvati_el(i, i)) < konst:
                    print("Vrijednost manja od zadane granične, zaustavlja se")
                    d.write("Vrijednost manja od zadane granicne, zaustavlja se\n")
                    return None
                self.matrica[j][i] /= self.matrica[i][i]
                for k in range(i + 1, self.redova):
                    self.matrica[j][k] -= self.matrica[j][i] * self.matrica[i][k]
        return self

    # fcija mijenja dva retka matrice
    # ulazni parametri su indeksi redaka koji se zele zamijeniti
    # izlaznih parametara nema
    def zamijeni(self, i, j):
        pom = self.matrica[i]
        self.matrica[i] = self.matrica[j]
        self.matrica[j] = pom

    # fcija provodi LUP dekompozicju matrice
    # ulaznih parametara nema
    # izlazni parametari su vektor P i broj zamjena
    def dekompozicijaLUP(self):
        if self.redova != self.stupaca:
            print("Matrica nije kvadratna")
            d.write("Matrica nije kvadratna\n")
            return None, None
        P = Matrica(self.redova, 1)
        br_zamjena = 0
        for i in range(self.redova):
            P.postavi_el(i, 0, i)
        for i in range(self.redova - 1):
            pivot = i
            for j in range(i + 1, self.redova):
                if abs(self.matrica[j][i]) > abs(self.matrica[pivot][i]):
                    pivot = j
            if i != pivot:
                br_zamjena += 1
            self.zamijeni(i, pivot)
            P.zamijeni(i, pivot)
            if abs(self.dohvati_el(i, i)) < konst:
                print("Vrijednost manja od zadane granične, zaustavlja se")
                d.write("Vrijednost manja od zadane granične, zaustavlja se\n")
                return None, None
            for j in range(i + 1, self.redova):
                self.matrica[j][i] /= self.matrica[i][i]
                for k in range(i + 1, self.redova):
                    self.matrica[j][k] -= self.matrica[j][i] * self.matrica[i][k]
        return P, br_zamjena

    # fcija mijenja retke stupcane matrice prema vektoru P
    # ulazni parametar je vektor P, izlazni parametar je matrica dobivena zamjenom redaka
    def permutirano(self, P):
        pom = Matrica(self.redova, 1)
        for i in range(self.redova):
            indeks = int(P.dohvati_el(i, 0))
            pom.postavi_el(i, 0, self.dohvati_el(indeks, 0))
        return pom

    # fcija izdvaja L dio matrice
    # ulaznih parametara nema, izlazni parametar je L matrica
    def izdvojiL(self):
        L = Matrica(self.redova, self.stupaca)
        for i in range(self.redova):
            for j in range(self.stupaca):
                if i < j:
                    L.postavi_el(i, j, 0)
                elif i == j:
                    L.postavi_el(i, j, 1)
                else:
                    L.postavi_el(i, j, self.dohvati_el(i, j))
        return L

    # fcija izdvaja U dio matrice
    # ulaznih parametara nema, izlazni parametar je U matrica
    def izdvojiU(self):
        U = Matrica(self.redova, self.stupaca)
        for i in range(self.redova):
            for j in range(self.stupaca):
                if i <= j:
                    U.postavi_el(i, j, self.dohvati_el(i, j))
                else:
                    U.postavi_el(i, j, 0)
        return U

    # fcija rjesava sustav pomocu LU dekompozicije
    # ulazni parametar je vektor b, izlazni parametar je rjesenje sustava
    def rijesiLU(self, b):
        if self.redova != self.stupaca:
            print("Matrica nije kvadratna, nije moguca LU dekompozicija")
            d.write("Matrica nije kvadratna, nije moguca LU dekompozicija\n")
            return None
        elif self.redova != b.redova:
            print("Neodgovarajući broj redaka")
            d.write("Neodgovarajuci broj redaka\n")
            return None
        elif b.stupaca != 1:
            print("Vektor b mora imati samo jedan stupac")
            d.write("Vektor b mora imati samo jedan stupac\n")
            return None
        pom = self.dekompozicijaLU()
        if pom is None:
            return None
        L = self.izdvojiL()
        U = self.izdvojiU()
        if koraci:
            print("L=")
            L.ispis_ekran()
            print("U=")
            U.ispis_ekran()
        y = L.supstitucijaUnaprijed(b)
        if y is None:
            return None
        elif koraci:
            print("y=")
            y.ispis_ekran()
        x = U.supstitucijaUnatrag(b)
        if x is not None and koraci:
            print("x=")
        return x

    # fcija rjesava sustav pomocu LUP dekompozicije
    # ulazni parametar je vektor b, izlazni parametar je rjesenje sustava
    def rijesiLUP(self, b):
        if self.redova != self.stupaca:
            print("Matrica nije kvadratna, nije moguca LUP dekompozicija")
            d.write("Matrica nije kvadratna, nije moguca LUP dekompozicija\n")
            return None
        if self.redova != b.redova:
            print("Neodgovarajući broj redaka")
            d.write("Neodgovarajući broj redaka\n")
            return None
        elif b.stupaca != 1:
            print("Vektor b mora imati samo jedan stupac")
            d.write("Vektor b mora imati samo jedan stupac\n")
            return None
        P, br_zamjena = self.dekompozicijaLUP()
        if P is None:
            return None
        L = self.izdvojiL()
        U = self.izdvojiU()
        b = b.permutirano(P)
        if koraci:
            print("L=")
            L.ispis_ekran()
            print("U=")
            U.ispis_ekran()
            print("P=")
            P.ispis_ekran()
        y = L.supstitucijaUnaprijed(b)
        if y is None:
            return None
        elif koraci:
            print("y=")
            y.ispis_ekran()
        x = U.supstitucijaUnatrag(y)
        if x is not None and koraci:
            print("x=")
        return x

    # fcija izdvaja zeljeni stupac matrice
    # ulazni parametar je indeks trazenog stupca, izlazni parametar je matrica koju cini trazeni stupac
    def vratiStupac(self, k):
        stupac = Matrica(self.redova, 1)
        for i in range(self.redova):
            stupac.postavi_el(i, 0, self.matrica[i][k])
        return stupac

    # fcija racuna inverz matrice
    # ulaznih parametara nema, izlazni parametar je matrica koja predstavlja inverz trenutne matrice
    def inverz(self):
        if self.redova != self.stupaca:
            print("Matrica nije kvadratna, nije moguca LUP dekompozicija")
            d.write("Matrica nije kvadratna, nije moguca LUP dekompozicija\n")
            return
        inv = Matrica(self.redova, self.stupaca)
        P, br_zamjena = self.dekompozicijaLUP()
        if P is None:
            print('Ne postoji inverz')
            d.write("Ne postoji inverz\n")
            return None
        L = self.izdvojiL()
        U = self.izdvojiU()
        if koraci:
            print("L=")
            L.ispis_ekran()
            print("U=")
            U.ispis_ekran()
            print("P=")
            P.ispis_ekran()
        E = Matrica(self.redova, self.stupaca)
        for i in range(self.redova):
            for j in range(self.stupaca):
                if i == j:
                    E.postavi_el(i, j, 1)
                else:
                    E.postavi_el(i, j, 0)
        for i in range(self.stupaca):
            stupac = E.vratiStupac(i)
            b = stupac.permutirano(P)
            y = L.supstitucijaUnaprijed(b)
            if y is None:
                print('Ne postoji inverz')
                d.write("Ne postoji inverz\n")
                return None
            x = U.supstitucijaUnatrag(y)
            if x is None:
                print('Ne postoji inverz')
                d.write("Ne postoji inverz\n")
                return None
            for j in range(x.redova):
                inv.postavi_el(j, i, x.dohvati_el(j, 0))
        if koraci:
            print("Inv= ")
        return inv

    # fcija racuna determinantu matrice
    # ulaznih parametara nema, izlazni parametar je determinanta matrice
    def determinanta(self):
        if self.redova != self.stupaca:
            print("Matrica nije kvadratna, nije moguca LUP dekompozicija")
            d.write("Matrica nije kvadratna, nije moguca LUP dekompozicija\n")
            return None
        P, br_zamjena = self.dekompozicijaLUP()
        if P is None:
            return None
        L = self.izdvojiL()
        U = self.izdvojiU()
        if koraci:
            print("L=")
            L.ispis_ekran()
            print("U=")
            U.ispis_ekran()
            print("P=")
            P.ispis_ekran()
        det = pow(-1, br_zamjena)
        for i in range(self.redova):
            det *= L.dohvati_el(i, i) * U.dohvati_el(i, i)
        if koraci:
            print("Det=")
        return det

    def vrati_redak(self, k):
        redak = Matrica(1, self.stupaca)

        for i in range(self.stupaca):
            redak.postavi_el(0, i, self.matrica[k][i])
        return redak


'''ime = '1.txt'
ime2A = '2A.txt'
ime2b = '2b.txt'
ime3 = '3.txt'
ime4A = '4A.txt'
ime4b = '4b.txt'
ime5A = '5A.txt'
ime5b = '5b.txt'
ime6A = '6A.txt'
ime6b = '6b.txt'
ime7 = '7.txt'
ime8 = '8.txt'
ime9 = '9.txt'
ime10 = '10.txt'

# prvi zad
d.write("1. zadatak:\n")
print("1. zadatak")
A = Matrica()
A.citaj(ime)
B = A.pridruzivanje()  # B = A
B = B.mnozenje_skalarom(1 / 25897)
B = B.mnozenje_skalarom(25897)
d.write(str(A == B) + "\n\n")
print(str(A == B) + "\n")

# drugi zad
d.write("2. zadatak:\n")
print("2. zadatak")
d.write("Rjesenje nakon LU dekompozicije:\n")
print("Rjesenje nakon LU dekompozicije:")
A.citaj(ime2A)
C = Matrica()
C.citaj(ime2b)
x1 = A.rijesiLU(C)
if x1 is not None:
    x1.dopisi()
    x1.ispis_ekran()
print()
d.write("\n")
A.citaj(ime2A)  # ponovno citanje jer je koristen isti memorijski prostor
C.citaj(ime2b)

d.write("Rjesenje nakon LUP dekompozicije:\n")
print("Rjesenje nakon LUP dekompozicije:")
x2 = A.rijesiLUP(C)
if x2 is not None:
    x2.dopisi()
    x2.ispis_ekran()
print()
d.write("\n")

# treci zad
d.write("3. zadatak:\n")
print("3. zadatak")
A.citaj(ime3)
d.write("LU dekompozicija:\n")
print("LU dekompozicija:")
x1 = A.dekompozicijaLU()
if x1 is not None:
    x1.dopisi()
    x1.ispis_ekran()
print()
d.write("\n")
A.citaj(ime3)
d.write("LUP dekompozicija:\n")
print("LUP dekompozicija:")
x2, z = A.dekompozicijaLUP()
if A is not None:
    A.dopisi()
    A.ispis_ekran()
print()
d.write("\n")

# provjera rjesivosti
A.citaj(ime3)
C = Matrica()
C.citaj(ime2b)
d.write("Rjesenje nakon LU dekompozicije:\n")
print("Rjesenje nakon LU dekompozicije:")
x1 = A.rijesiLU(C)
if x1 is not None:
    x1.dopisi()
    x1.ispis_ekran()
print()
d.write("\n")
A.citaj(ime3)  # ponovno citanje jer je koristen isti memorijski prostor
C.citaj(ime2b)

d.write("Rjesenje nakon LUP dekompozicije:\n")
print("Rjesenje nakon LUP dekompozicije:")
x2 = A.rijesiLUP(C)
if x2 is not None:
    x2.dopisi()
    x2.ispis_ekran()
print()
d.write("\n")

# cetvrti zad
d.write("4. zadatak:\n")
print("4. zadatak")
d.write("Rjesenje nakon LU dekompozicije:\n")
print("Rjesenje nakon LU dekompozicije:")
A.citaj(ime4A)
C = Matrica()
C.citaj(ime4b)
x1 = A.rijesiLU(C)
if x1 is not None:
    x1.dopisi()
    x1.ispis_ekran()
print()
d.write("\n")
A.citaj(ime4A)  # ponovno citanje jer je koristen isti memorijski prostor
C.citaj(ime4b)

d.write("Rjesenje nakon LUP dekompozicije:\n")
print("Rjesenje nakon LUP dekompozicije:")
x2 = A.rijesiLUP(C)
if x2 is not None:
    x2.dopisi()
    x2.ispis_ekran()
print()
d.write("\n")

# peti zad
d.write("5. zadatak:\n")
print("5. zadatak")
d.write("Rjesenje nakon LU dekompozicije:\n")
print("Rjesenje nakon LU dekompozicije:")
A.citaj(ime5A)
C = Matrica()
C.citaj(ime5b)
x1 = A.rijesiLU(C)
if x1 is not None:
    x1.dopisi()
    x1.ispis_ekran()
print()
d.write("\n")
A.citaj(ime5A)  # ponovno citanje jer je koristen isti memorijski prostor
C.citaj(ime5b)

d.write("Rjesenje nakon LUP dekompozicije:\n")
print("Rjesenje nakon LUP dekompozicije:")
x2 = A.rijesiLUP(C)
if x2 is not None:
    x2.dopisi()
    x2.ispis_ekran()
print()
d.write("\n")

# sesti zad
konst = 0.000001
d.write("6. zadatak:\n")
print("6. zadatak")
d.write("Rjesenje nakon LU dekompozicije:\n")
print("Rjesenje nakon LU dekompozicije:")
A.citaj(ime6A)
C = Matrica()
C.citaj(ime6b)
x1 = A.rijesiLU(C)
if x1 is not None:
    x1.dopisi()
    x1.ispis_ekran()
print()
d.write("\n")
A.citaj(ime6A)  # ponovno citanje jer je koristen isti memorijski prostor
C.citaj(ime6b)

d.write("Rjesenje nakon LUP dekompozicije:\n")
print("Rjesenje nakon LUP dekompozicije:")
x2 = A.rijesiLUP(C)
if x2 is not None:
    x2.dopisi()
    x2.ispis_ekran()
print()
d.write("\n")
konst = 0.00000000001

# sedmi zad
d.write("7. zadatak:\n")
print("7. zadatak")
A.citaj(ime7)
inv = A.inverz()
if inv is not None:
    inv.dopisi()
    inv.ispis_ekran()
print()
d.write("\n")

# osmi zad
d.write("8. zadatak:\n")
print("8. zadatak")
A.citaj(ime8)
inv = A.inverz()
if inv is not None:
    inv.dopisi()
    inv.ispis_ekran()
print()
d.write("\n")

# deveti zad
d.write("9. zadatak:\n")
print("9. zadatak")
A.citaj(ime9)
det = A.determinanta()
d.write(str(det) + "\n")
print(str(det) + "\n")
d.write("\n")

# deseti zad
d.write("10. zadatak:\n")
print("10. zadatak")
A.citaj(ime10)
det = A.determinanta()
d.write(str(det) + "\n")
print(str(det))'''

