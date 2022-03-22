import math

def d_and_p(ranks):
    length = len(ranks[0])
    n = len(ranks)
    print("Mean - ")
    means = []
    for i in range(length):
        sum =0 
        for rank in ranks:
            sum += rank[i]
        print(f"~x_{i+1} = {round(sum/n, 2)}")
        means.append(round(sum/n, 2))
    
    variances = []
    print("Variance -")
    for i in range(length):
        variance = 0
        for rank in ranks:
            variance += (rank[i] - means[i])**2
        print(f"\u03C3{i+1}^2 = {round(variance/n, 2)}")
        variances.append(round(variance/n, 2))

    print("Dubios and Prade formula - ")
    print("Gaussian Membership Function - degree of belonginess of doc i at position x")
    print("\u03BC_d_i(x) = 1/(2pi(\u03C3_d)^2)^.5 * exp (-0.5[(x - x_d)^ 2 / (\u03C3_d)^2])")
    belong = []
    for i in range(length):
        belonginess = []
        for j in range(length):
            val = math.exp(-((j+1 - means[i])**2/variances[i])/2) / math.sqrt(2*math.pi *variances[i])
            print(f"\u03BC_{i+1}({j+1}) = 1/(2pi({variances[i]}))^.5 * exp (-0.5[({j+1} - {means[i]})^ 2 / ({variances[i]})]) = ", "{:.2e}".format(val))
            belonginess.append(val)
        print("Using Zadeh Notation - ")
        val = 0
        print(f"d{i+1} = (", end = "")
        belong.append(belonginess)
        for pos, b in enumerate(belonginess):
            print("{:.2e}".format(b), f"/ {pos+1}", end = " + ")

        print(")")
    return belong

def compare(belonginess, i, j, details = False):
    if details:
        print(f"T({i+1} >= {j+1}) = max(", end = "")
    else:
        print(f"T({i+1} >= {j+1}) = ", end = "")

    maximum = float(-math.inf)
    for index, val in enumerate(belonginess[i]):
        for pos in range(index+1):
            if details:
                print("min(", "{:.2e}".format(val), ",", "{:.2e}".format(belonginess[j][pos]), ")", end = " , ")
            maximum = max(maximum, min(val, belonginess[j][pos]))
    if details:
        print(") = ", maximum)
    else:
        print(maximum)

    return maximum

def main():
    n = int(input("Enter the number of lists : "))
    k = int(input("Enter the number of pages : "))
    ranks = []
    for i in range(n):
        ranks.append([0]*k)
        for j,rank in enumerate(input().strip().split()):
            ranks[i][int(rank)-1] = j+1

    belonginess = d_and_p(ranks)
    new_rank = []
    for i in range(k):
        minimum = float(math.inf)
        for j in range(k):
            if i == j: 
                continue
            minimum = min(minimum, compare(belonginess, i, j, i == 0 and j == 1))
        print(f"T({i+1} >= all other) = ", minimum)
        new_rank.append([minimum, i+1])

    new_rank.sort()
    print(new_rank)

main()