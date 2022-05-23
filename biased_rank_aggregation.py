from rank_aggregation import borda_score

def main():
    n = int(input("Enter the number of lists : "))
    k = int(input("Enter the number of pages : "))
    ranks = []
    for i in range(n):
        ranks.append([0]*k)
        for j,rank in enumerate(input().strip().split()):
            ranks[i][int(rank)-1] = j+1

    print("Enter the weights - ")
    weights = []
    for page in range(n):
        weights.append(float(input(f"Enter weight for searh engine {page+1} :")))

    borda_score(ranks[0], ranks[1], weights[0], weights[1])

if __name__ == "__main__":
    main()