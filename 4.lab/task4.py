import lab4
import sys
import math
import task3


def nadi_najbolji(hit_and_median):
    most_hits = 0
    smallest_median = math.inf
    par = 0
    for one in hit_and_median.keys():
        hit, median = hit_and_median.get(one)
        if hit > most_hits:
            most_hits = hit
            smallest_median = median
            par = one
        elif hit == most_hits and median < smallest_median:
            most_hits = hit
            smallest_median = median
            par = one
    return par


# definirani parametri
p_M = 0.1
stop = 10000
tur_size = 3
index = 0
dg = -50
gg = 150
e = 0.000001


def cetvrti(files):
    sys.stdout = open(files[0], "w")
    it = 10
    zad = lab4.fcija(6)
    velicina_pop = [30, 50, 100, 200]
    vjv_mut = [0.1, 0.3, 0.6, 0.9]
    p_M = 0.1 # potrebno za optimiranje N
    br_var = 2
    operator_krizanja = 1
    hit_and_median = dict()
    for k in velicina_pop:
        print("Velicina populacije = " + str(k))
        cnt, median = task3.call_pomicna_cnt_and_median(k, dg, gg, zad, p_M, stop, br_var, operator_krizanja, e, it)
        hit_and_median[k] = cnt, median
        print()
    N = nadi_najbolji(hit_and_median) # taj N se koristi za optimitanje vjv mutacije
    print("Pronadeni N = " + str(N))
    sys.stdout.close()

    sys.stdout = open(files[1], "w")
    hit_and_median = dict()
    for k in vjv_mut:
        print("Vjerojatnost mutacije = " + str(k))
        cnt, median = task3.call_pomicna_cnt_and_median(N, dg, gg, zad, k, stop, br_var, operator_krizanja, e, it)
        hit_and_median[k] = cnt, median
        print()
    p_M = nadi_najbolji(hit_and_median)  # taj N se koristi za optimitanje vjv mutacije
    print("Pronadeni p_M = " + str(p_M))
    sys.stdout.close()
