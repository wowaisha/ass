from math import comb

def probability_king_and_non_king():
    total_outcomes = comb(52, 2) #összes lehetséges kértya 
    favorable_outcomes = comb(4, 1) * comb(48, 1) # 1 király és 1 nem király
    probability = favorable_outcomes / total_outcomes # valószínűség = kedvező / összes
    return probability

print(f"Annak a valószínűsége, hogy az egyik kártya király, a másik nem király: {probability_king_and_non_king():.4f}")
