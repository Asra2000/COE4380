def get_reference(n, order):
    print("R_v(i, j) = [1 + (v_j - v_i)/(N-1)] / 2")
    R_v = list()
    for i in range(n):
        row_order = [] 
        for j in range(n):
            if i == j:
                row_order.append(0.5)
            else:
                row_order.append(round((1 + (order[j] - order[i])/ (n-1))/2 , 5))
        R_v.append(row_order)
    
    return R_v


def main():
    n = int(input("Enter # document :"))
    order = [-1]*n
    rank = 1
    for i in list(int(num) for num in input().strip().split()):
        order[i-1] = rank
        rank += 1

    reference=  get_reference(n, order)
    for i in range(n):
        for j in range(n):
            print(reference[i][j], end = "\t")
        print("")
    
main()