'''
Aprioi is an algorithm for frequent item set mining and association rule 
learning over relational databases. The frequent item sets determined by 
Apriori can be used to determine association rules which highlight general 
trends in the database.
'''

from hashlib import new
from re import A


class Apriori:
    def __init__(self, items, transaction, support_threshold):
        self.transaction = transaction
        self.support_threshold = support_threshold
        self.items = items
        self.frequent_set = {}
        self.non_frequent_set = []
        self.subsets = self.generate_subsets([], set(), 0) 


    def solve(self):
        # for k = 1
        k = 1
        self.frequent_set[k] = [{i} for i in self.items]
        freq = self.count(k)
        self.prune(k, freq)
        k = 2
        while(self.frequent_set[k-1] != []):
            self.join(k)
            freq = self.count(k)
            self.non_frequent_set = []
            self.prune(k, freq)
            k += 1
        
        return self.frequent_set
    
    def count(self, k):
        freq = {}

        for i in self.frequent_set[k]:
            curr_set = frozenset(i)
            for trans in self.transaction:
                if i.issubset(trans):
                    if curr_set in freq:
                        freq[curr_set] = freq[curr_set] + 1
                    else :
                        freq[curr_set] = 1
            
            if curr_set not in freq:
                freq[curr_set] = 0

        return freq

    '''
    Generate kth item sets from (k-1)th item sets
    '''
    def join(self, k):
        new_sequence = []
        for i in self.subsets:
            if len(i) != k:
                continue
            can_add = True
            for j in self.non_frequent_set:
                if j in i:
                    can_add = False
                    break
            if can_add:
                new_sequence.append(i.copy())

        self.frequent_set[k] = new_sequence
    
    '''
    This funtion removes all the item sets that do not 
    fulfill the minimum support criterion.
    '''
    def prune(self, k, freq):
        for i in self.frequent_set[k].copy():
            current_set = frozenset(i)
            if freq[current_set] < self.support_threshold:
                self.non_frequent_set.append(i)
                self.frequent_set[k].remove(i)

    '''
    Generate all possible subsets using the following items
    '''
    def generate_subsets(self, subset, current,index):
        if index == len(self.items):
            subset.append(set(current))
            return
        
        current.add(self.items[index])
        self.generate_subsets(subset, current, index+1)
        current.remove(self.items[index])
        self.generate_subsets(subset, current, index+1)

        return subset
        

def main():
    transaction = [{"I1", "I2", "I3"}, 
                    {"I2","I3","I4"},
                    {"I4","I5"},
                    {"I1","I2","I4"},
                    {"I1", "I2", "I3", "I5"},
                    {"I1", "I2", "I3", "I4"},]
    support_threshold = 3
    items = ["I1", "I2", "I3", "I4", "I5"]
    # Computing the support for each individual item
    obj = Apriori(items, transaction, support_threshold)
    frequent_itemset = obj.solve()
    
    print("Printing the frequent itemsets")
    for key, val in frequent_itemset.items():
        print("At k =", key, "," ,  val)
    

main()
