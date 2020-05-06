from pprint import pprint as pp
from itertools import chain, combinations

# class kullanilarak name, value ve weight degerleri olusturulur
class  Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + (self.name) + ', ' + str(self.value)  + ', ' + str(self.weight) + '>'
        return result
        
def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

# returns Value/Weight
def density(item):
    return item.getValue()/item.getWeight()


""" Assumes Items a list, maxWeight >= 0, keyFunction maps elements of Items to numbers """
def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalWeight = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if(totalWeight + itemsCopy[i].getWeight()) <= maxWeight:
            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return(result, totalValue)

# degerler atanir
def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    # values = [175, 90, 20, 50, 10, 200]
    # weights = [10, 9, 4, 2, 1, 20]
    values = [26, 76, 98, 10, 16, 305]
    weights = [20, 16, 9, 1, 3, 8]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items

# degerler yazdirilir
def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print("Total value of this taken is = ", val)
    for item in taken:
        print('  ', item)

# fonksiyonlar birlestiriliyor.
def testGreedys(maxWeight = 30):
    items = buildItems()
    # value en yüksek alinir
    print("Use greedy by value to fill knapsack of size = ", maxWeight)
    testGreedy(items, maxWeight, value)
    # weight en dusuk alinir
    print("\nUse greedy by weight to fill knapsack of size = ", maxWeight)
    testGreedy(items, maxWeight, weightInverse)
    # value/weight
    print("\nUse greedy by density to fill knapsack of size = ", maxWeight)
    testGreedy(items, maxWeight, density)

print(testGreedys())

# en iyi ihtimal seciliyor
# pset = power set
def chooseBest(pset, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)


# def testBest(maxWeight = 20):
def testBest(maxWeight = 30):
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print("Total value of items taken is = ", val)
    for item in taken:
        print(item)


# kombinasyonlari yazdirir
def genPowerset(iterable):
    "powerset([1, 2, 3]) --> () (1,) (2,) (3,) (1, 2) (1, 3), (1, 2, 3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


print(testBest())


pp(set(genPowerset({1, 2, 3, 4})))

print("-----------------------")

pset = set(genPowerset({1, 2}))
for set_1 in pset:
   print(set_1)
