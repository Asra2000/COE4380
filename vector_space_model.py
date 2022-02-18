import math

class Resource():
    def __init__(self, count):
        self.word_count = count
        self.frequencies = []
        self.max_freq = 0

    def add_freq(self, freq):
        if self.max_freq < freq:
                self.max_freq  = freq
        self.frequencies.append(freq)

    def __repr__(self):
        return " + ".join(f"{self.freq}w{i}" for i, t in enumerate(self.frequencies))

            

class VectorSpace(Resource):
    def __init__(self, n, word_count):
        self.n  = n
        self.word_count = word_count
        self.resources = []

    def add_resource(self, r):
        self.resources.append(r)

    def print_resource(self):
        for resource in self.resources:
            print(resource)

    def dot_product(self, r1, r2):

        cosines = 0
        r1_normal = 0  
        r2_normal = 0
        for i in range(self.word_count):
            count = self.get_count(i) 
            r1_norm = self.resources[r1].frequencies[i] / self.resources[r1].max_freq * math.log(self.n/count,10)
            r2_norm = self.resources[r2].frequencies[i] / self.resources[r2].max_freq * math.log(self.n/count, 10)
            r1_normal += r1_norm**2
            r2_normal += r2_norm**2
            cosines += r1_norm * r2_norm
            print(f"{r1_norm * r2_norm}w{i+1}", end = " + ")

        print("\ncosine = ", str(cosines/(math.sqrt(r1_normal) * math.sqrt(r2_normal))))

    def get_count(self, i):
        count = 0
        for resource in self.resources:
            if resource.frequencies[i] != 0:
                count += 1

        return count

    def generate_table(self):
        print("Freq of words in resources")
        print("Word\t", "\t".join("w" + str(i+1) for i in range(self.n)))
        for i in range(self.word_count):
            count = self.get_count(i) 
            print(f"w{i+1}", end = "\t")
            for resource in self.resources:
                print(f"{resource.frequencies[i]}/{resource.max_freq}log({self.n}/{count})", end = "\t")
            print("")

def main():
    n = int(input("Enter the # resources:"))
    word_count = int(input("Enter the # words:"))
    obj  = VectorSpace(n, word_count)
    for i in range(n):
        print(f"Enter freq for R{i+1}")
        resource = Resource(word_count)
        for j in range(word_count):
            resource.add_freq(int(input(f"w{j+1} = ")))

        obj.add_resource(resource)


    obj.generate_table()

    r1= int(input("Enter r1:"))
    r2= int(input("Enter r2:"))
    obj.dot_product(r1-1, r2-1)


if __name__ == "__main__":
    main()