import random
import math
import sys

koraci = False


class fcija:
    def __init__(self, zadatak):
        self.zadatak = zadatak

    def F(self, x):
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


# fcija provodi heuristicko krizanje jedinki
# ulazni parametri su lita od dvije jedinke koje ce se krizati i zadatak
# izlazni parametar je novonastala jedinka
def crossHeuristic(nove, zad):
    x1 = nove[0].x
    x2 = nove[1].x
    p = list()
    for i in range(len(x1)):
        p.append(random.random() * (x2[i] - x1[i]) + x2[i])
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
def cross_pt(nove, operator_krizanja, zad):
    if operator_krizanja:
        return crossHeuristic(nove, zad)
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
def pomicna_tocka_verzija(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja):
    population = make_population_pt(N, dg, gg, zad, br_var)
    eval_num = 1
    best_one = best(population)
    while eval_num < stop:
        # odabir tur_size jedinki
        nove = random.sample(population, tur_size)
        # izbaci najlosiju od 3 odabrane
        nove, izbacena = izbaci(nove)
        new = cross_pt(nove, operator_krizanja, zad)
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
            r.append(binaryToNum(i, self.dg, self.gg, self.n))
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
def binaryToNum(b, dg, gg, n):
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
            if (i + j) < point:
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
def binarna_verzija(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja):
    n = math.ceil(math.log(1 + (gg - dg) * pow(10, preciznost)) / math.log(2))
    population = make_population_b(N, dg, gg, zad, br_var, n, preciznost)
    eval_num = 1
    best_one = best(population)
    while eval_num < stop:
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


# fcija poziva zeljeni genetski algoritam (binarna verzija ili verzija s posmicnom tockom)
# N = velicina populacije
# dg = donja granica, gg = gornja granica
# zad.F = koristena fcija
# p_M = vjerojatnost mutacije
# stop = kriterij zaustavljanja (br evaluacija)
# br_var = broj varijabli
# binarni = ako True binarni prikaz, inace prikaz brojem s pomicnom tockom
# preciznost = ako binarni br decimala, ako ne None
# operator_krizanja -> za binarni prikaz 0 -> krizanje s tockom prekida
#                                        1 -> uniformno krizanje
#                   -> za pom tocku      0 -> aritmeticko krizanje
#                                        1 -> heuristicko krizanje
# fcija vraca najbolju jedinku
def genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja):
    if binarni:
        return binarna_verzija(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja)
    else:
        return pomicna_tocka_verzija(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja)


izlazi = ["lab4_1.txt", "lab4_2.txt", "lab4_3_f6_3.txt", "lab4_3_f6_6.txt", "lab4_3_f7_3.txt",
          "lab4_3_f7_6.txt", "lab4_4_N.txt", "lab4_4_mut.txt", "lab4_5.txt"]
dg = -50
gg = 150
e = 0.000001
N = 100
p_M = 0.3
stop = 30000
tur_size = 3
index = 0

# prvi zad
sys.stdout = open(izlazi[0], "w")
print("1.zad")
# fcija 1
print("Fcija 1:")
zad = fcija(1)
br_var = 2
it = 15
# prikaz s pomicnom tockom
binarni = False
preciznost = None
operator_krizanja = 1
min = None
najblize = True
for i in range(it):
    rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
    if rj.vrijednost < e:
        print("Prikaz s pomicnom tockom:")
        print("\tRj pronadeno u " + str(i + 1) + " iteracija = ", end="")
        rj.print()
        print("\tVrijednost fcije cilja = " + str(rj.vrijednost))
        najblize = False
        break
    if min is None:
        min = rj
    elif min.vrijednost > rj.vrijednost:
        min = rj
if najblize:
    print("Prikaz s pomicnom tockom:")
    print("\tRjesenje nije pronadeno u " + str(it) + " iteracija")
    print("\tNajbolja jedinka = ", end="")
    min.print()
    print("\tVrijednost fcije cilja = " + str(min.vrijednost))

# binarni prikaz
binarni = True
preciznost = 3
operator_krizanja = 0
min = None
najblize = True
for i in range(it):
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        if rj.vrijednost < e:
            print("Binarni prikaz:")
            print("\tRj pronadeno u " + str(i+1) + " iteracija = ", end="")
            rj.print()
            print("\tSto odgovara: ", end="")
            rj.printAsNum()
            print("\nVrijednost fcije cilja = " + str(rj.vrijednost))
            najblize = False
            break
        if min is None:
            min = rj
        elif min.vrijednost > rj.vrijednost:
            min = rj
if najblize:
    print("Binarni prikaz:")
    print("\tRjesenje nije pronadeno u " + str(it) + " iteracija")
    print("\tNajbolja jedinka = ", end="")
    min.print()
    print("\tSto odgovara: ", end="")
    min.printAsNum()
    print("\tVrijednost fcije cilja = " + str(min.vrijednost))

# fcija 3
print("Fcija 3:")
zad = fcija(3)
br_var = 5
it = 15
preciznost = 3
# prikaz s pomicnom tockom
binarni = False
operator_krizanja = 0
min = None
najblize = True
for i in range(it):
    rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
    if rj.vrijednost < e:
        print("Prikaz s pomicnom tockom:")
        print("\tRj pronadeno u " + str(i + 1) + " iteracija = ", end="")
        rj.print()
        print("\tVrijednost fcije cilja = " + str(rj.vrijednost))
        najblize = False
        break
    if min is None:
        min = rj
    elif min.vrijednost > rj.vrijednost:
        min = rj
if najblize:
    print("Prikaz s pomicnom tockom:")
    print("\tRjesenje nije pronadeno u " + str(it) + " iteracija")
    print("\tNajbolja jedinka = ", end="")
    min.print()
    print("\tVrijednost fcije cilja = " + str(min.vrijednost))

# binarni prikaz
binarni = True
preciznost = 3
operator_krizanja = 1
min = None
najblize = True
for i in range(it):
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        if rj.vrijednost < e:
            print("Binarni prikaz:")
            print("\tRj pronadeno u " + str(i+1) + " iteracija = ", end="")
            rj.print()
            print("\tSto odgovara: ", end="")
            rj.printAsNum()
            print("\nVrijednost fcije cilja = " + str(rj.vrijednost))
            najblize = False
            break
        if min is None:
            min = rj
        elif min.vrijednost > rj.vrijednost:
            min = rj
if najblize:
    print("Binarni prikaz:")
    print("\tRjesenje nije pronadeno u " + str(it) + " iteracija")
    print("\tNajbolja jedinka = ", end="")
    min.print()
    print("\tSto odgovara: ", end="")
    min.printAsNum()
    print("\tVrijednost fcije cilja = " + str(min.vrijednost))

# fcija 6
print("Fcija 6:")
zad = fcija(6)
br_var = 2
# prikaz s pomicnom tockom
binarni = False
operator_krizanja = 0
min = None
najblize = True
for i in range(it):
    rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
    if rj.vrijednost < e:
        print("Prikaz s pomicnom tockom:")
        print("\tRj pronadeno u " + str(i + 1) + " iteracija = ", end="")
        rj.print()
        print("\tVrijednost fcije cilja = " + str(rj.vrijednost))
        najblize = False
        break
    if min is None:
        min = rj
    elif min.vrijednost > rj.vrijednost:
        min = rj
if najblize:
    print("Prikaz s pomicnom tockom:")
    print("\tRjesenje nije pronadeno u " + str(it) + " iteracija")
    print("\tNajbolja jedinka = ", end="")
    min.print()
    print("\tVrijednost fcije cilja = " + str(min.vrijednost))
# binarni prikaz
binarni = True
preciznost = 3
operator_krizanja = 1
min = None
najblize = True
for i in range(it):
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        if rj.vrijednost < e:
            print("Binarni prikaz:")
            print("\tRj pronadeno u " + str(i+1) + " iteracija = ", end="")
            rj.print()
            print("\tSto odgovara: ", end="")
            rj.printAsNum()
            print("\nVrijednost fcije cilja = " + str(rj.vrijednost))
            najblize = False
            break
        if min is None:
            min = rj
        elif min.vrijednost > rj.vrijednost:
            min = rj
if najblize:
    print("Binarni prikaz:")
    print("\tRjesenje nije pronadeno u " + str(it) + " iteracija")
    print("\tNajbolja jedinka = ", end="")
    min.print()
    print("\tSto odgovara: ", end="")
    min.printAsNum()
    print("\tVrijednost fcije cilja = " + str(min.vrijednost))

# fcija 7
print("Fcija 7:")
zad = fcija(7)
br_var = 2
# prikaz s pomicnom tockom
binarni = False
operator_krizanja = 0
min = None
najblize = True
for i in range(it):
    rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
    if rj.vrijednost < e:
        print("Prikaz s pomicnom tockom:")
        print("\tRj pronadeno u " + str(i + 1) + " iteracija = ", end="")
        rj.print()
        print("\tVrijednost fcije cilja = " + str(rj.vrijednost))
        najblize = False
        break
    if min is None:
        min = rj
    elif min.vrijednost > rj.vrijednost:
        min = rj
if najblize:
    print("Prikaz s pomicnom tockom:")
    print("\tRjesenje nije pronadeno u " + str(it) + " iteracija")
    print("\tNajbolja jedinka = ", end="")
    min.print()
    print("\tVrijednost fcije cilja = " + str(min.vrijednost))
# binarni prikaz
binarni = True
preciznost = 3
operator_krizanja = 1
min = None
najblize = True
for i in range(it):
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        if rj.vrijednost < e:
            print("Binarni prikaz:")
            print("\tRj pronadeno u " + str(i+1) + " iteracija = ", end="")
            rj.print()
            print("\tSto odgovara: ", end="")
            rj.printAsNum()
            print("\nVrijednost fcije cilja = " + str(rj.vrijednost))
            najblize = False
            break
        if min is None:
            min = rj
        elif min.vrijednost > rj.vrijednost:
            min = rj
if najblize:
    print("Binarni prikaz:")
    print("\tRjesenje nije pronadeno u " + str(it) + " iteracija")
    print("\tNajbolja jedinka = ", end="")
    min.print()
    print("\tSto odgovara: ", end="")
    min.printAsNum()
    print("\tVrijednost fcije cilja = " + str(min.vrijednost))
sys.stdout.close()

# drugi zad
sys.stdout = open(izlazi[1], "w")
print("2. zad")
stop = 10000
fcije = [6, 7]
dimenzije = [1, 3, 6, 10]
for f in fcije:
    zad = fcija(f)
    print("Fcija " + str(f))
    for br_var in dimenzije:
        print("Dimenzija = " + str(br_var))
        # binarni prikaz
        print("Binarni prikaz:")
        binarni = True
        preciznost = 3
        operator_krizanja = 1
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        if rj.vrijednost < e:
            print("\tPronadeno rj = ", end="")
        else:
            print("\tNije pronadeno rj,  najbolja jedinka = ", end="")
        rj.print()
        print("\tSto odgovara: ", end="")
        rj.printAsNum()
        print("\tVrijednost fcije cilja = " + str(rj.vrijednost))

        # prikaz s pomicnom tockom
        print("Prikaz s pomicnom tockom")
        binarni = False
        preciznost = None
        operator_krizanja = 0
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        if rj.vrijednost < e:
            print("\tPronadeno rj = ", end="")
        else:
            print("\tNije pronadeno rj,  najbolja jedinka = ", end="")
        rj.print()
        print("\tVrijednost fcije cilja = " + str(rj.vrijednost))
        print()
sys.stdout.close()

# treci zad
stop = 100000
iteracija = 10
dimenzije = [3, 6]

zad = fcija(6)
index = 2
for br_var in dimenzije:
    cnt = 0
    val = list()
    sys.stdout = open(izlazi[index], "w")
    index += 1
    print("Fcija " + str(6) + ", br var = " + str(br_var))
    print("Prikaz s pomicnom tockom:")
    # prikaz s pomicnom tockom
    binarni = False
    preciznost = None
    operator_krizanja = 0
    for i in range(iteracija):
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        val.append(rj.vrijednost)
        print(rj.vrijednost)
        if rj.vrijednost < e:
            cnt += 1
    print()
    val.sort()
    duljina = len(val)
    if duljina % 2 == 0:
        median = (val[duljina // 2 - 1] + val[duljina // 2]) / 2
    else:
        median = val[duljina // 2 - 1]

    # binarni prikaz
    binarni = True
    preciznost = 4
    operator_krizanja = 1
    cnt_b = 0
    val = list()
    print("Binarni prikaz:")
    for i in range(iteracija):
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        val.append(rj.vrijednost)
        print(rj.vrijednost)
        if rj.vrijednost < e:
            cnt_b += 1
    print()
    val.sort()
    duljina = len(val)
    if duljina % 2 == 0:
        median_b = (val[duljina // 2 - 1] + val[duljina // 2]) / 2
    else:
        median_b = val[duljina // 2 - 1]
    if cnt_b > cnt:
        print("Bolje s binarnim prikazom")
    elif cnt_b < cnt:
        print("Bolje s prikazom s pomicnom tockom")
    else:
        if median_b < median:
            print("Bolje s binarnim prikazom")
        else:
            print("Bolje s prikazom s pomicnom tockom")
    sys.stdout.close()


zad = fcija(7)
index = 4
for br_var in dimenzije:
    cnt = 0
    val = list()
    sys.stdout = open(izlazi[index], "w")
    index += 1
    print("Fcija " + str(7) + ", br var = " + str(br_var))
    print("Prikaz s pomicnom tockom:")
    # prikaz s pomicnom tockom
    binarni = False
    preciznost = None
    operator_krizanja = 0
    for i in range(iteracija):
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        val.append(rj.vrijednost)
        print(rj.vrijednost)
        if rj.vrijednost < e:
            cnt += 1
    print()
    val.sort()
    duljina = len(val)
    if duljina % 2 == 0:
        median = (val[duljina // 2 - 1] + val[duljina // 2]) / 2
    else:
        median = val[duljina // 2 - 1]

    # binarni prikaz
    binarni = True
    preciznost = 4
    operator_krizanja = 1
    cnt_b = 0
    val = list()
    print("Binarni prikaz:")
    for i in range(iteracija):
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        val.append(rj.vrijednost)
        print(rj.vrijednost)
        if rj.vrijednost < e:
            cnt_b += 1
    print()
    val.sort()
    duljina = len(val)
    if duljina % 2 == 0:
        median_b = (val[duljina // 2 - 1] + val[duljina // 2]) / 2
    else:
        median_b = val[duljina // 2 - 1]
    if cnt_b > cnt:
        print("Bolje s binarnim prikazom")
    elif cnt_b < cnt:
        print("Bolje s prikazom s pomicnom tockom")
    else:
        if median_b < median:
            print("Bolje s binarnim prikazom")
        else:
            print("Bolje s prikazom s pomicnom tockom")
    sys.stdout.close()

# cetvrti zad
zad = fcija(6)
velicina_pop = [30, 50, 100, 200]
vjv_mut = [0.1, 0.3, 0.6, 0.9]
p_M = 0.1
stop = 10000
br_var = 2
iteracija = 10
binarni = False
preciznost = None
operator_krizanja = 1
hit_and_median = dict()
sys.stdout = open(izlazi[6], "w")
for k in velicina_pop:
    cnt = 0
    val = list()
    print("Velicina populacije = " + str(k))
    for i in range(iteracija):
        rj = genetski_algoritam(k, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        val.append(rj.vrijednost)
        print(rj.vrijednost)
        if rj.vrijednost < e:
            cnt += 1
    val.sort()
    duljina = len(val)
    if duljina % 2 == 0:
        median = (val[duljina // 2 - 1] + val[duljina // 2]) / 2
    else:
        median = val[duljina // 2 - 1]
    hit_and_median[k] = cnt, median
most_hits = 0
smallest_median = math.inf
N = 0
for one in hit_and_median.keys():
    hit, median = hit_and_median.get(one)

    if hit > most_hits:
        most_hits = hit
        smallest_median = median
        N = one
    elif hit == most_hits and median < smallest_median:
        most_hits = hit
        smallest_median = median
        N = one
print("Pronadeni N = " + str(N))
sys.stdout.close()

sys.stdout = open(izlazi[7], "w")
hit_and_median = dict()
for k in vjv_mut:
    cnt = 0
    val = list()
    print("Vjerojatnost mutacije = " + str(k))
    for i in range(iteracija):
        rj = genetski_algoritam(N, dg, gg, zad, k, stop, br_var, binarni, preciznost, operator_krizanja)
        val.append(rj.vrijednost)
        print(rj.vrijednost)
        if rj.vrijednost < e:
            cnt += 1
    val.sort()
    duljina = len(val)
    if duljina % 2 == 0:
        median = (val[duljina // 2 - 1] + val[duljina // 2]) / 2
    else:
        median = val[duljina // 2 - 1]
    hit_and_median[k] = cnt, median
    print()
most_hits = 0
smallest_median = math.inf
p_M = 0
for one in hit_and_median.keys():
    hit, median = hit_and_median.get(one)
    if hit > most_hits:
        most_hits = hit
        smallest_median = median
        p_M = one
    elif hit == most_hits and median < smallest_median:
        most_hits = hit
        smallest_median = median
        p_M = one
print("Pronadeni p_M = " + str(p_M))
sys.stdout.close()

# peti zad
sys.stdout = open(izlazi[8], "w")
print("5. zad")
zad = fcija(6)
binarni = False
preciznost = None
operator_krizanja = 0
iteracija = 10
p_M = 0.3
N = 50
stop = 10000
br_var = 2
hit_and_median = dict()
for one in range(3, 10):
    tur_size = one
    cnt = 0
    val = list()
    print("k = " + str(one))
    for i in range(iteracija):
        rj = genetski_algoritam(N, dg, gg, zad, p_M, stop, br_var, binarni, preciznost, operator_krizanja)
        val.append(rj.vrijednost)
        print(rj.vrijednost)
        if rj.vrijednost < e:
            cnt += 1
    val.sort()
    duljina = len(val)
    if duljina % 2 == 0:
        median = (val[duljina // 2 - 1] + val[duljina // 2]) / 2
    else:
        median = val[duljina // 2 - 1]
    hit_and_median[one] = cnt, median
    print()
most_hits = 0
smallest_median = math.inf
tur_size = 0
for one in hit_and_median.keys():
    hit, median = hit_and_median.get(one)
    if hit > most_hits:
        most_hits = hit
        smallest_median = median
        tur_size = one
    elif hit == most_hits and median < smallest_median:
        most_hits = hit
        smallest_median = median
        tur_size = one
print("Najbolji tur_size = " + str(tur_size))
sys.stdout.close()
