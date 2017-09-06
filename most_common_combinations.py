'''
This is a sample code of a function, that gets a list of combinations, and 
counts the occurences of the combinations and returns the most common of them.
'''
from collections import Counter
from itertools import combinations

duo_products = [
    ['product2', 'product1'],
    ['product2', 'product1'],
    ['product2', 'product2'],
    ['product2', 'product3'],
    ['product2', 'product1'],
    ['product2', 'product4'],
    ['product2', 'product5'],
    ['product2', 'product5'],
    ['product2', 'product5'],
    ['product3', 'product1'],
    ['product1', 'product2'],
    ['product7', 'product1']
]

triple_products = [
    ['product1', 'product5', 'product7'],
    ['product1', 'product3', 'product7'],
    ['product1', 'product2', 'product7'],
    ['product1', 'product5', 'product7'],
    ['product1', 'product5', 'product7'],
    ['product1', 'product6', 'product7'],
    ['product1', 'product2', 'product7'],
    ['product1', 'product2', 'product7'],
    ['product1', 'product5', 'product7'],
    ['product1', 'product5', 'product7']
]


def get_most_common(arr, n=None):
    """
    Returns a list with the most common combinations of elements in the arr
    list, together with the number of occurences.
    :param arr: The list of list including the elements of combinations
    :param n: Number of most common results to return
    :return: [((), number)]
    """
    d = Counter()
    for sub in arr:
        if len(arr) < 2:
            continue
        sub.sort()
        for comb in combinations(sub, len(sub)):
            d[comb] += 1
    return d.most_common(n)

if __name__ == 'main':
  # Get the duets alone
  common_duets = get_most_common(duo_products)
  # Get the triplets alone
  common_triplets = get_most_common(triple_products)
  # Get the combination of all products together to check that it works
  combined = get_most_common(duo_products + triple_products)

  print(common_duets)
  print(common_triplets)
  print(combined)
  
