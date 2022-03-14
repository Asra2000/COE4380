'''
A pageRank algorithm helps in rannking the pages based on the probability that, the page will be viewed by a random sufer.

Let PR(p) be the PageRank of a given page p: the probability that a random surfer ends up on that page. 
There are two ways that a random surfer could end up on the page:
1.  With probability d, the surfer chose a page at random and ended up on page p.
2.  With probability 1-d, the surfer followed a link from a page i to page p. (where i can be any page pointing to p)
'''
class Page:
    def __init__(self, val) -> None:
        self.initial_value = val
        self.links = []
        self.out_deg = 0

    def add_links(self, links):
        self.links = links

    def set_out_deg(self, deg):
        self.out_deg = deg

    def set_initial_value(self, val):
        self.initial_value = val

def main():
    iterations  = int(input("Enter # iterations:"))
    # A damping factor helps in identifying how likely is for a random surfer to randomly click on external link.
    d = float(input("d(damping factor):"))
    page_count = int(input("Enter # of pages:"))
    print("Enter initial values - ")
    pages = []

    for i in range(page_count):
        pages.append(Page(float(input(f"P{i+1} = "))))

    for i in range(page_count):
        pages[i].add_links(list(int(num)-1 for num in input(f"For P{i+1} enter the pages that point towards it - ").strip().split()))
        pages[i].set_out_deg(int(input("Enter # out pointing links :")))

    print("Formula to be used - \nR(Pj) = d/T  + (1-d)\u03A3(R(Pi)/C(Pi))\n")
    for iteration in range(iterations):
        print(f"Iteration {iteration+1}")
        for page in range(page_count):
            print(f"R(P{page+1}) = {d}/{page_count} + {1-d}(", " + ".join(str(pages[p].initial_value)+"/"+str(pages[p].out_deg) for p in pages[page].links), " )", end = " = ")
            t = round(d/page_count +  (1-d) * sum([pages[p].initial_value/pages[p].out_deg for p in pages[page].links]), 5)
            print(t)
            pages[page].set_initial_value(t)

        print("----------------------------------")


    print("Finished!")

if __name__ == "__main__":
    main()    

    