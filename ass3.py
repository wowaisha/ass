def probability_king_not_king():
    favorable_cases = 4 * 48  #kedvezó eset, ha 4 király és 48 nem király
    total_cases = (52 * 51) // 2  #2 kártya húzása, összesen 52 lap
    probability = favorable_cases / total_cases # return probability
result = probability_king_not_king()
print(f"A valószínűsége annak, hogy az egyik kártya király, a másik pedig nem király: {result:.4f}")


import itertools
from collections import Counter

def calculate_distribution_given_W(target_sum):
    values = [0, 1, 2, 3] # X, y és z lehetséges értékei
    combinations = list(itertools.product(values, repeat=3)) összes lehetséges kombináció
    w_counts = Counter() #számláló a W = X + Y + Z -hez
    
    for x, y, z in combinations:
        w = x + y + z
        w_counts[w] += 1
    
    if target_sum not in w_counts: #lehetséges-e az eredmény
        return f"A W = {target_sum} nem lehetséges a megadott tartományban."
    
    x_distribution = Counter()  # x eloszlása milyen, ha W = target_sum
    
    for x, y, z in combinations:
        if x + y + z == target_sum:
            x_distribution[x] += 1
    
    total = sum(x_distribution.values())
    normalized_distribution = {x: count / total for x, count in x_distribution.items()}  # eloszlás normalizálás
    return normalized_distribution
    
target_sum = 7 #7 a célérték 
result = calculate_distribution_given_W(target_sum)
print(f"X eloszlása, ha W = {target_sum}: {result}") 
