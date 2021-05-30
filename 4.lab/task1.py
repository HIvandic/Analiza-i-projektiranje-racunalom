from lab4 import *
import sys


def call_pomicna(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja, e, it):
    min = None
    najblize = True
    for i in range(it):
        rj = lab4.pomicna_tocka_verzija_ga(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja, e)
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


def call_binarni(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja, e, it):
    min = None
    najblize = True
    for i in range(it):
        rj = lab4.binarna_verzija_ga(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja, e)
        if rj.vrijednost < e:
            print("Binarni prikaz:")
            print("\tRj pronadeno u " + str(i + 1) + " iteracija = ", end="")
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


# definirani parametri
N = 100  # N = velicina populacije
p_M = 0.3  # p_M = vjerojatnost mutacije
stop = 30000  # stop = kriterij zaustavljanja (br evaluacija)
tur_size = 3
index = 0
dg = -50  # dg = donja granica
gg = 150  # gg = gornja granica
e = 0.000001


def prvi(file):
    sys.stdout = open(file, "w")
    print("1.zad")
    it = 15

    fcije = [1, 3, 6, 7]
    dimenzije = [2, 5, 2, 2]
    preciznost = 3  # br decimala
    for i in range(len(fcije)):
        f = fcije[i]
        br_var = dimenzije[i]
        print("Fcija " + str(f) + ":")
        zad = lab4.fcija(f)
        if i == 0:
            operator_krizanja = 1  # heuristicko krizanje
            operator_krizanja_b = 0  # krizanje s tockom prekida
        else:
            operator_krizanja = 0  # br_var aritmeticko krizanje
            operator_krizanja_b = 1  # uniformno krizanje
        call_pomicna(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja, e, it)
        call_binarni(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja_b, e, it)
    sys.stdout.close()
