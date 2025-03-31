def probability_king_not_king():
    favorable_cases = 4 * 48  #kedvezó eset, ha 4 király és 48 nem király
    total_cases = (52 * 51) // 2  #2 kártya húzása, összesen 52 lap
    probability = favorable_cases / total_cases # return probability
result = probability_king_not_king()
print(f"A valószínűsége, hogy az egyik kártya király, a másik pedig nem király: {result:.4f}")
