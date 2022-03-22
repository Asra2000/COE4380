def shimura_technique(ranks) :
    print("Shimura Technique")
    length = len(ranks[0])
    n = len(ranks)
    f = [[0.0 for x in range(length)] for y in range(length)] 

    print("f_x_j(x_i) = |k\u0395[1, N] ^ l_k(x_i) < l_k(x_j)| / N = ")
    for x_i in range(length):
        for x_j in range(length):
            if x_i == x_j:
                f[x_i][x_j] = 1
            else:
                count = 0
                for rank in ranks:
                    if rank[x_i] < rank[x_j]:
                        count+=1
                f[x_i][x_j] = round(count/n, 4)
            print(f[x_i][x_j], end = "\t")
        print()

    minimum_c = []
    print("Where this func. is taken to be the membership of preferring  x_i over x_j")
    print("f(x_i|x_j) = f_x_j(x_i) / max(f_x_j(x_i), f_x_j(x_j)) = ")
    for x_i in range(length):
        minimum = f[x_i][0]
        for x_j in range(length):
            maximum = max(f[x_i][x_j], f[x_j][x_i])
            # print("\np", x_i, x_j, f[x_i][x_j], f[x_j][x_i])
            f[x_i][x_j] = round(f[x_i][x_j] / maximum, 4)
            minimum = min(f[x_i][x_j], minimum)
            print(f[x_i][x_j], end = "\t")
        minimum_c.append([minimum, x_i])
        print()

    print("C_j = minimum of each row = ")
    for minimum in minimum_c:
        print(minimum[1], f"[{minimum[0]}]") 

    minimum_c.sort()
    for minimum in minimum_c:
        print(minimum)

def main():
    n = int(input("Enter the number of lists : "))
    k = int(input("Enter the number of pages : "))
    ranks = []
    for i in range(n):
        ranks.append([0]*k)
        for j,rank in enumerate(input().strip().split()):
            ranks[i][int(rank)-1] = j+1

    shimura_technique(ranks)
    
main()