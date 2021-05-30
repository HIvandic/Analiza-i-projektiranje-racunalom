import random
import math
from task1 import *
from task2 import *
from task3 import *
from task4 import *
from task5 import *

koraci = False


class fcija:
    def __init__(self, zadatak):
        self.broj_poziva = 0
        self.zadatak = zadatak

    def F(self, x):
        self.broj_poziva = self.broj_poziva + 1
        if self.zadatak == 1:
            x1 = x[0]
            x2 = x[1]
            return 100 * pow(x2 - pow(x1, 2), 2) + pow(1 - x1, 2)
        elif self.zadatak == 3:
            rez = 0
            for k in range(len(x)):
                one = x[k]
                rez = rez + pow(one - k, 2)
            return rez
        elif self.zadatak == 6:
            suma = 0
            for k in range(len(x)):
                one = x[k]
                suma = suma + pow(one, 2)
            brojnik = pow(math.sin(pow(suma, 1 / 2)), 2) - 0.5
            nazivnik = pow(1 + 0.001 * suma, 2)
            return 0.5 + brojnik / nazivnik
        elif self.zadatak == 7:
            suma = 0
            for k in range(len(x)):
                one = x[k]
                suma = suma + pow(one, 2)
            return pow(suma, 0.25) * (1 + pow(math.sin(50 * pow(suma, 0.1)), 2))

    def vrati_broj_poziva(self):
        return self.broj_poziva

    def resetiraj_broj_poziva(self):
        self.broj_poziva = 0


# verzija za pomicnu tocku
class jedinka:
    def __init__(self, x, zad):
        self.x = x
        self.vrijednost = zad.F(x)

    # fcija ispisuje jedinku
    def print(self):
        ispis = ""
        first = True
        for i in self.x:
            if first:
                ispis += str(i)
                first = False
            else:
                ispis += ", " + str(i)
        print(ispis)
        return


# fcija generira novu jedinku
# ulazni parametri su gornja i donja granica i broj varijabli
# izlazni parametar je generirana jedinka
def generiraj_pt(dg, gg, br_var):
    rez = []
    for i in range(br_var):
        rez.append((gg - dg) * random.random() + dg)
    return rez


# fcija stvara populaciju
# ulazni parametri su broj jedinki, gornja i donja granica, zadatak i broj varijabli
# izlazni parametar je stvorena populacija
def make_population_pt(N, dg, gg, zad, br_var):
    population = []
    for i in range(N):
        new = jedinka(generiraj_pt(dg, gg, br_var), zad)
        population.append(new)
    return population


# fcija provodi heuristicko krizanje jedinki (priblizavamo se boljoj)
# ulazni parametri su lita od dvije jedinke koje ce se krizati i zadatak
# izlazni parametar je novonastala jedinka
def crossHeuristic(nove, zad, gg, dg):
    # zbog prijasnjeg nacina odabira jedinki kod turnira, bolja jedinka nalazi se prva u listi
    x2 = nove[0].x
    x1 = nove[1].x
    p = list()
    for i in range(len(x1)):
        new = random.random() * (x2[i] - x1[i]) + x2[i]
        if new > gg:
            new = gg
        if new < dg:
            new = dg
        p.append(new)
    return jedinka(p, zad)


# fcija provodi aritmeticko krizanje jedinki
# ulazni parametri su lista od dvije jedinke koje ce se krizati i zadatak
# izlazni parametar je novonastala jedinka
def crossArithmetic(nove, zad):
    x1 = nove[0].x
    x2 = nove[1].x
    p = list()
    for i in range(len(x1)):
        a = random.random()
        p.append(a * x1[i] + (1 - a) * x2[i])
    return jedinka(p, zad)


# fcija poziva odgovarajucu fciju za krizanje jedinki
# izlazni parametar je novonastala jedinka
def cross_pt(nove, operator_krizanja, zad, gg, dg):
    if operator_krizanja:
        return crossHeuristic(nove, zad, gg, dg)
    else:
        return crossArithmetic(nove, zad)


# fcija provodi jednoliku mutaciju
# ulazni parametri su jedinka, gornja i donja granica, vjerojatnost mutacije i zadatak
# izlazni parametar je novonastala (mutirana) jedinka
def mute_pt(new, dg, gg, p_M, zad):
    elementi = new.x
    for i in range(len(elementi)):
        if random.random() <= p_M:
            elementi[i] = (gg - dg) * random.random() + dg
    return jedinka(elementi, zad)


# fcija pronalazi najbolju jedinku u populaciji
# ulazni parametar je populacija (lista svih jedinki)
# izlazni parametar je najbolja jedinka
def best(population):
    best_jedinka = population[0]
    for i in range(1, len(population)):
        if population[i].vrijednost < best_jedinka.vrijednost:
            best_jedinka = population[i]
    return best_jedinka


# fcija odreduje najbolje i najgoru jedinku
# ulazni parametar je lista jedinki
# izlazni parametar je par vrijednosti, prva vrijednost je lista najboljih jedinki (one ce se krizati),
# druga vrijednost je najlosija jedinka (ona koja ce se izbaciti iz populacije)
def izbaci(nove):
    maximum = nove[0]
    for i in range(1, len(nove)):
        current = nove[i]
        if current.vrijednost > maximum.vrijednost:
            maximum = current
    nove.remove(maximum)
    minimum = nove[0]
    ret = []
    for i in range(1, len(nove)):
        current = nove[i]
        if current.vrijednost < minimum.vrijednost:
            minimum = current
    ret.append(minimum)
    nove.remove(minimum)
    minimum = nove[0]
    for i in range(1, len(nove)):
        current = nove[i]
        if current.vrijednost < minimum.vrijednost:
            minimum = current
    ret.append(minimum)
    return ret, maximum


# fcija provodi genetski algoritam pomocu prikaza s pomicnom tockom
# fcija vraca najbolju jedinku
def pomicna_tocka_verzija_ga(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja, e, tur_size=3):
    population = make_population_pt(N, dg, gg, zad, br_var)
    best_one = best(population)
    eval_num = 1
    while zad.vrati_broj_poziva() < stop:
        # odabir tur_size jedinki
        nove = random.sample(population, tur_size)
        # izbaci najlosiju od 3 odabrane
        nove, izbacena = izbaci(nove)
        new = cross_pt(nove, operator_krizanja, zad, gg, dg)
        new = mute_pt(new, dg, gg, p_M, zad)
        # makni staru, dodaj novu jedinku
        population.remove(izbacena)
        population.append(new)
        if new.vrijednost < best_one.vrijednost:
            best_one = new
            if koraci:
                print(str(eval_num) + ". iteracija, najbolja = ", end="")
                best_one.print()
                print("Vrijednost fcije cilja = " + str(best_one.vrijednost))
            if best_one.vrijednost < e:
                break
        eval_num = eval_num + 1
    return best_one


# verzija za binarni
class jedinka_b:
    def __init__(self, x, zad, n, dg, gg, preciznost):
        self.x = x  # binarni broj
        self.n = n  # br bitova
        self.b = self.calc_bin()  # niz bitova
        self.dg = dg # donja granica
        self.gg = gg # gornja granica
        self.preciznost = preciznost
        self.num = self.pretvori()  # odgovarajuci broj
        self.vrijednost = zad.F(self.num)  # vrij fcije cilja

    # fcija ispisuje binarni prikaz
    def print(self):
        ispis = ""
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                ispis += str(self.b[i][j])
        print(ispis)
        return

    # fcija ispisuje odgovarajucu vrijednost tocke
    def printAsNum(self):
        ispis = ""
        first = True
        for i in self.num:
            if first:
                ispis += str(i)
                first = False
            else:
                ispis += ", " + str(i)
        print(ispis)
        return

    # fcija pretvara binarnu vrijednost u odgovarajucu vrijednost u intervalu
    def pretvori(self):
        r = []
        for i in self.x:
            r.append(binaryToNum(i, self.dg, self.gg, self.n, self.preciznost))
        return r

    # fcija prikazuje vrijednost kao niz bitova
    def calc_bin(self):
        r = []
        for i in self.x:
            one = bin(i)
            one = one.split("b")
            d = []
            cnt = 0
            for j in one[1]:
                d.append(int(j))
                cnt += 1
            if cnt < self.n:
                for k in range(int(self.n - cnt)):
                    d.insert(0, 0)
            r.append(d)
        return r


# fcija iz niza bitova odreduje broj
# ulazni parametar je niz bitova
# izlazni parametar je odgovarajuci broj
def calc_num(b):
    string = "0b"
    for i in b:
        string += str(i)
    return int(string, 2)


# fcija pretvara binaran prikaz u broj
# ulazni parametri su binarni broj, donja i gornja granica i broj bitova
# izlazni parametar je odgovarajuca vrijednost x
def binaryToNum(b, dg, gg, n, preciznost):
    return round(dg + b * (gg - dg) / (pow(2, n) - 1), preciznost)


# fcija pretvara broj u njegov binarni prikaz
# ulazni parametri su broj x, donja i gornja granica i broj bitova
# izlazni parametar je odgovarajuca binarna vrijednost x (binarni prikaz - broj)
def numToBinary(x, dg, gg, n):
    return (x - dg) * (pow(2, n) - 1) / (gg - dg)


# fcija generira novu jedinku
# ulazni parametri su gornja i donja granica i broj bitova
# izlazni parametar je generirana jedinka
def generiraj_b(br_var, n):
    rez = []
    for i in range(br_var):
        rez.append(random.randint(0, pow(2, n) - 1))
    return rez


# fcija stvara populaciju
# ulazni parametri su broj jedinki, gornja i donja granica, zadatak, broj varijabli, broj bitova i preciznost
# izlazni parametar je stvorena populacija
def make_population_b(N, dg, gg, zad, br_var, n, preciznost):
    population = []
    for i in range(N):
        new = jedinka_b(generiraj_b(br_var, n), zad, n, dg, gg, preciznost)
        population.append(new)
    return population


# fcija provodi uniformno krizanje jedinki
# ulazni parametri su jedinke koje se krizaju, donja i gornja granica, broj bitova, zadatak i preciznost
# izlazni parametar je novonastala jedinka
def crossUniform(nove, dg, gg, n, zad, preciznost):
    x1 = nove[0].b
    x2 = nove[1].b
    R = jedinka_b(generiraj_b(len(x1), n), zad, n, dg, gg, preciznost)
    new = []
    for i in range(len(x1)):
        l = []
        for j in range(len(x1[0])):
            if x1[i][j] == x2[i][j]:
                l.append(x1[i][j])
            else:
                l.append(R.b[i][j])
        new.append(calc_num(l))
    return jedinka_b(new, zad, n, dg, gg, preciznost)


# fcija provodi krizanje s jednom tockom prekida
# ulazni parametri su jedinke koje se krizaju, donja i gornja granica, broj bitova, zadatak i preciznost
# izlazni parametar je novonastala jedinka
def crossBreakPoint(nove, dg, gg, n, zad, preciznost):
    x1 = nove[0].b
    x2 = nove[1].b
    var = len(x1)
    point = random.randint(0, var * n - 1)
    new1 = []
    new2 = []
    for i in range(len(x1)):
        l1 = []
        l2 = []
        for j in range(len(x1[0])):
            if (i * n + j) < point:
                l1.append(x1[i][j])
                l2.append(x2[i][j])
            else:
                l1.append(x2[i][j])
                l2.append(x1[i][j])
        new1.append(calc_num(l1))
        new2.append(calc_num(l2))
    a = jedinka_b(new1, zad, n, dg, gg, preciznost)
    b = jedinka_b(new2, zad, n, dg, gg, preciznost)
    if a.vrijednost < b.vrijednost:
        return a
    else:
        return b


# fcija poziva odgovarajucu fciju za krizanje jedinki
# izlazni parametar je novonastala jedinka
def cross_b(nove, dg, gg, operator_krizanja, n, zad, preciznost):
    if operator_krizanja:
        return crossUniform(nove, dg, gg, n, zad, preciznost)
    else:
        return crossBreakPoint(nove, dg, gg, n, zad, preciznost)


# fcija provodi jednoliku mutaciju jedinke
# ulazni parametri su nova jedinka, vjerojatnost mutacije bita, zadatak i preciznost
# izlazni parametar je mutirana jedinka
def mute_b(new, p_M, zad, preciznost):
    novo = []
    for i in range(len(new.b)):
        l = []
        for j in range(len(new.b[0])):
            if random.random() < p_M:
                l.append(random.randint(0, 1))
            else:
                l.append(new.b[i][j])
        novo.append(calc_num(l))
    return jedinka_b(novo, zad, new.n, new.dg, new.gg, preciznost)


# fcija provodi genetski algoritam pomocu binarnog prikaza
# fcija vraca najbolju jedinku
def binarna_verzija_ga(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja, e, tur_size=3):
    n = math.ceil(math.log(1 + (gg - dg) * pow(10, preciznost)) / math.log(2))
    population = make_population_b(N, dg, gg, zad, br_var, n, preciznost)
    eval_num = 1
    best_one = best(population)
    while zad.vrati_broj_poziva() < stop:
        # odabir tur_size jedink
        nove = random.sample(population, tur_size)
        # izbaci najlosiju od 3 odabrane
        nove, izbacena = izbaci(nove)
        new = cross_b(nove, dg, gg, operator_krizanja, n, zad, preciznost)
        new = mute_b(new, p_M, zad, preciznost)
        # makni staru, dodaj novu jedinku
        population.remove(izbacena)
        population.append(new)
        if new.vrijednost < best_one.vrijednost:
            best_one = new
            if koraci:
                print(str(eval_num) + ". iteracija, najbolja = ", end="")
                best_one.print()
                print("vrijednost fcije cilja = " + str(best_one.vrijednost))
            if best_one.vrijednost < e:
                break
        eval_num = eval_num + 1
    return best_one


if __name__ == '__main__':
    prvi("./cetvrti_out/lab4_1.txt")
    drugi("./cetvrti_out/lab4_2.txt")
    treci(["./cetvrti_out/lab4_3_f6.txt", "./cetvrti_out/lab4_3_f7.txt"])
    cetvrti(["./cetvrti_out/lab4_4_N.txt", "./cetvrti_out/lab4_4_mut.txt"])
    peti("./cetvrti_out/lab4_5.txt")
