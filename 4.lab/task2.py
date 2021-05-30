import lab4
import sys
import task1


# definirani parametri
N = 100
p_M = 0.3
stop = 10000
tur_size = 3
index = 0
dg = -50
gg = 150
e = 0.000001


def drugi(file):
    sys.stdout = open(file, "w")
    print("2.zad")
    fcije = [6, 7]
    dimenzije = [1, 3, 6, 10]
    preciznost = 3
    operator_krizanja = 0
    operator_krizanja_b = 1
    it = 1

    for f in fcije:
        zad = lab4.fcija(f)
        print("Fcija " + str(f))
        for br_var in dimenzije:
            print("Dimenzija = " + str(br_var))
            task1.call_pomicna(N, dg, gg, zad, p_M, stop, br_var, operator_krizanja, e, it)
            task1.call_binarni(N, dg, gg, zad, p_M, stop, br_var, preciznost, operator_krizanja_b, e, it)
            print()
    sys.stdout.close()
