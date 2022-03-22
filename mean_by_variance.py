from cmath import inf
from statistics import variance
from dubois_prade_method import get_mean, get_variance

def main():
    n = int(input("Enter the number of lists : "))
    k = int(input("Enter the number of pages : "))
    ranks = []
    for i in range(n):
        ranks.append([0]*k)
        for j,rank in enumerate(input().strip().split()):
            ranks[i][int(rank)-1] = j+1

    means = get_mean(ranks)
    variances = get_variance(ranks, means)

    print("MBV")
    new_ranks = []
    for i in range(k):
        print(f"mbv({i+1}) = (" , f"-x{i+1}/\u03C3{i+1}^2 = ", end ="")
        val = round(means[i]/variances[i],2)
        print(val)
        new_ranks.append([val, i+1])

    new_ranks.sort()

    for i in new_ranks:
        print(f"l({i[1]}) <", end= "")


if __name__ == "__main__":
    main()
