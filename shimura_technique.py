from operator import le
from ordered_weighted_avg import OWA

def shimura_technique(ranks, improve = False) :
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

    if not improve:
        find_minimum(length, f)

    else:
        improved_shimura_technique(length, f)
    

def find_minimum(length, f):
    minimum_c = []
    print("Where this func. is taken to be the membership of preferring  x_i over x_j")
    print("f(x_i|x_j) = f_x_j(x_i) / max(f_x_j(x_i), f_x_j(x_j)) = ")
    for x_i in range(length):
        minimum = f[x_i][0]
        for x_j in range(length):
            maximum = max(f[x_i][x_j], f[x_j][x_i])
            f[x_i][x_j] = round(f[x_i][x_j] / maximum, 4)
            minimum = min(f[x_i][x_j], minimum)
            print(f[x_i][x_j], end = "\t")
        minimum_c.append([minimum, x_i])
        print()

    print("C_j = minimum of each row = ")
    for minimum in minimum_c:
        print(minimum[1], f"[{minimum[0]}]") 

    print("ordering of pages with minimum value = ")
    minimum_c.sort()
    for minimum in minimum_c:
        print(minimum)

def improved_shimura_technique(length, f):
    minimum_c = []
    for x, val in enumerate(f):
        val.sort(reverse = True)
        ob = OWA(0.0, .5, val)
        atleast_half = ob.find_weight()
        minimum_c.append([atleast_half, x])
    
    print("Based on Condorcet Criteria: if some element d belonging to a set defeats \
        \nevery other element in pairwirse majority voting, then this element is ranked first; \
        \nnecessary for span fighting. ")
    print("Atleast half of each row = ")
    for minimum in minimum_c:
        print(minimum[1], f"[{minimum[0]}]") 

    print("ordering of pages with minimum value = ")
    minimum_c.sort(reverse=True)
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

    improved = input("Improved shimura technique (y/n) :") == 'y'
    shimura_technique(ranks, improved)
    
if __name__ == "__main__":
    main()