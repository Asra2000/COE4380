'''Speaeman rank order coefficient'''

def main():
    print("Spearman Rank order Coefficient can be given as - ")
    print("r_s = 1 - 6(\u03A3(l(ai) - l(bi))^2 / (n * (n^2-1))")
    n = int(input("Enter # pages :"))
    rank1 = list(int(i) for i in input("Enter the rank - ").split())
    rank2 = list(int(i) for i in input("Enter the rank - ").strip().split())
    sum = 0
    for i in range(n):
        d = rank1[i] - rank2[i]
        print(rank1[i], rank2[i], d, d**2)
        sum += d**2
    print(sum)
    print(str(1 - 6 *(sum/(n * (n**2-1)))))

main()