import lab4
import sys


def get_median(val):
    val.sort()
    duljina = len(val)
    if duljina % 2 == 0:
        median = (val[duljina // 2 - 1] + val[duljina // 2]) / 2
    else:
        median = val[duljina // 2 - 1]
    return median


def call_pomicna_cnt_and_median(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja, e, it, tur_size=3):
    print("Prikaz s pomicnom tockom:")
    cnt = 0
    val = list()
    for i in range(it):
        rj = lab4.pomicna_tocka_verzija_ga(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja, e, tur_size)
        val.append(rj.vrijednost)
        print(rj.vrijednost)
        if rj.vrijednost < e:
            cnt += 1
    print()
    median = get_median(val)
    return cnt, median


def call_binarni_cnt_and_median(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja, e, it):
    print("Binarni prikaz:")
    cnt = 0
    val = list()
    for i in range(it):
        rj = lab4.binarna_verzija_ga(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja, e)
        val.append(rj.vrijednost)
        print(rj.vrijednost)
        if rj.vrijednost < e:
            cnt += 1
    print()
    median = get_median(val)
    return cnt, median


def usporedi(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja, operator_krizanja_b, e, it):
    cnt_p, median_p = call_pomicna_cnt_and_median(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja, e, it)
    cnt_b, median_b = call_binarni_cnt_and_median(N, dg, gg, zad, p_M, stop, br_var, preciznost,
                                                  operator_krizanja_b, e, it)
    if cnt_b > cnt_p:
        print("-> Bolje s binarnim prikazom")
    elif cnt_b < cnt_p:
        print("-> Bolje s prikazom s pomicnom tockom")
    else:
        if median_b < median_p:
            print("-> Bolje s binarnim prikazom")
        else:
            print("-> Bolje s prikazom s pomicnom tockom")


# definirani parametri
N = 100
p_M = 0.3
stop = 100000
tur_size = 3
index = 0
dg = -50
gg = 150
e = 0.000001


def treci(files):
    it = 10
    fcije = [6, 7]
    dimenzije = [3, 6]
    preciznost = 4
    operator_krizanja = 0
    operator_krizanja_b = 1
    index = 0
    for f in fcije:
        zad = lab4.fcija(f)
        sys.stdout = open(files[index], "w")
        for br_var in dimenzije:
            print("Fcija = " + str(f) + ", br var = " + str(br_var))
            usporedi(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja, operator_krizanja_b, e, it)
            print()
        index = index + 1
        sys.stdout.close()

