import lab4
import sys
import task3
import task4

# definirani parametri
N = 50
p_M = 0.3
stop = 10000
tur_size = 3
index = 0
dg = -50
gg = 150
e = 0.000001


def peti(file):
    sys.stdout = open(file, "w")
    print("5.zad")
    it = 10
    zad = lab4.fcija(6)
    operator_krizanja = 0
    br_var = 2
    hit_and_median = dict()
    for one in range(3, 10):
        tur_size = one
        print("k = " + str(one))
        cnt, median = task3.call_pomicna_cnt_and_median(N, dg, gg, zad, p_M, stop, br_var,
                                                        operator_krizanja, e, it, tur_size)
        hit_and_median[one] = cnt, median
        print()
    tur_size = task4.nadi_najbolji(hit_and_median)  # taj N se koristi za optimitanje vjv mutacije
    print("Pronadeni tur_size = " + str(tur_size))
    sys.stdout.close()
