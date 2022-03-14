from logging.config import valid_ident


class OWA:
    def __init__(self, a, b, val) -> None:
        self.val = val
        self.a = a
        self.b = b
        self.n = len(val)+1
        self.weight = list()

    def find_weight(self):
        print("i", end = "\t")
        for i in range(self.n):
            print(i, end = "\t")

        print("\n(i/m)",  end = "\t")
        for i in range(self.n):
            calc = round(i/(self.n-1), 5)
            self.weight.append(calc)
            print(calc, end="\t")

        print("\nq(i/m)",  end = "\t")
        for i in range(self.n):
            if self.weight[i] < self.a:
                calc = 0
            elif self.weight[i] > self.b:
                calc = 1
            else:
                calc = round((self.weight[i] - self.a)/(self.b - self.a), 5)

            self.weight[i] = calc
            print(calc, end="\t")

        print("\nw(i)", end = "\t\t")
        prev = self.weight[0]
        for i in range(1, self.n):
            temp = self.weight[i]
            self.weight[i] -= prev
            print(round(self.weight[i], 5), end="\t")
            prev = temp

        print(f"\nk = ", end = " ")
        k = 0
        for i in  range(1, self.n):
            print(f"{round(self.weight[i], 5)} * {round(self.val[i-1], 5)} + ", end = " ")
            k += self.weight[i] * self.val[i-1]

        print("\n\nk = " ,  round(k, 5))

def main():
    a = float(input("a: "))
    b = float(input("b: "))
    val = list(float(num) for num in input(f"Enter the val : ").strip().split())
    val.sort(reverse = True)
    if a < .5:
        print("\nMost")
        print("1 |                --------")
        print("  |              -")
        print("  |            -")
        print("  |           -")
        print("  |          -")
        print("  |         -")
        print("  |        -")
        print("  |------")
        print("  | 0      .3     .8")
    elif a == .5:
        print("\nAtleast half")
        print("1 |             --------")
        print("  |           -")
        print("  |         -")
        print("  |       -")
        print("  |     -")
        print("  |   -")
        print("  | -")
        print("  | 0         .5      1")
    else :
        print("\nAs many as possible")
        print("1 |                --------")
        print("  |              -")
        print("  |            -")
        print("  |           -")
        print("  |          -")
        print("  |         -")
        print("  |        -")
        print("  |------")
        print("  | 0      .5     1")

    ob = OWA(a, b, val)
    ob.find_weight()

main()