from cmath import inf
from dubois_prade_method import d_and_p

def main():
    n = int(input("Enter the number of lists : "))
    k = int(input("Enter the number of pages : "))
    ranks = []
    for i in range(n):
        ranks.append([0]*k)
        for j,rank in enumerate(input().strip().split()):
            ranks[i][int(rank)-1] = j+1

    belonginess = d_and_p(ranks)
    print("Membership Function Optimisation")
    print()
    included = set()
    for i in range(k):
        maximum = float(-inf)
        pos = []
        for j, belong in enumerate(belonginess):
            if j in included:
                continue
            if belong[i] > maximum:
                maximum = belong[i]
                pos = [j]
            elif belong[i] == maximum:
                pos.append(j)

        included.update(pos)
        print(f"\u03A3 \u03BC_i({i+1}) = ", end = "")
        for p in pos:
            print(f"d{p+1}", end="~" if len(pos) > 1 else "")
        print()


if __name__ == "__main__":
    main()
