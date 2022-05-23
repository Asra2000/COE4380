import math

def borda_score(rank1, rank2, w1 =  1, w2 = 1):
    print("S(c_j) = \u03A3S_i(c_j)")
    length = len(rank1)
    f = {}
    for i in range(length):
        f[i] = w1 * (length - rank1[i]) + w2 * (length - rank2[i])
        if w1 == w2 and w1 == 1:
            print(f"S({i+1}) = S_1({i+1} + S_2({i+1})) = {length - rank1[i]} + {length - rank2[i]} = {f[i]}")
        else:
            print(f"S({i+1}) = S_1({i+1} + S_2({i+1})) = {w1} * {length - rank1[i]} + {w2} * {length - rank2[i]} = {f[i]}")

    print({k+1: v for k, v in sorted(f.items(), key=lambda item: item[1], reverse=True)})


def spearman_footrule_formula(rank1, rank2):
    print("F(l1, l2) = \u03A3|l1(i) - l2(i)| / (0.5 * |len|^2)")
    length = len(rank1)
    f = 0
    print("F(l1, l2) =", end = " ")
    for i in range(length):
        f  += abs(rank1[i] - rank2[i])
        print(f"|{rank1[i]} - {rank2[i]}|", end = " + ")
    print("\n\t\t----------------------")
    print(f"\t\t0.5 * {length}^2")
    print(f" = {f} / {math.floor(0.5 * length**2)}")
    print("F(l1, l2) =", round(f/(math.floor(0.5 * length**2)), 5))

def main():
    choice = int(input("Options available\n1-Spearman footrule Formula\n2-Positional Borda's Method"))
    n = int(input("Enter the number of lists : "))
    k = int(input("Enter the number of pages : "))
    ranks = []
    for i in range(n):
        ranks.append([0]*k)
        for j,rank in enumerate(input().strip().split()):
            ranks[i][int(rank)-1] = j+1

    if choice == 1:
        spearman_footrule_formula(ranks[0], ranks[1])
    else:
        borda_score(ranks[0], ranks[1])

if __name__ == "__main__":
    main()