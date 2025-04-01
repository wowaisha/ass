import math,random,time  #importalja a a math es random modulokat

feature1 = ['könyvtáros', 'tanár']  #meghatarozza az elso lehetseges szot
feature2 = ['csendes', 'cserfes']  #meghatarozza a masodik lehetseges szot
operator = [' és ', ' vagy ']  #az elso es masodik szo kozti op
dyslexia_prob = 0.5  #a diszle
misinterpret_prob = 0.8


def uniformDraw(array, chance = True):
    prob_number = random.random()
    if chance == True:
        return array[math.floor(random.random() * len(array))]
    else:
        value = ' vagy ' if 0.95 > prob_number else ' és '
        return value

def ComplexModel1():
  word1 = uniformDraw(feature1)
  op = uniformDraw(operator)
  word2 = uniformDraw(feature2)
  if (random.random() < dyslexia_prob):
    word2 = 'cserfes' if (word2 == 'csendes') else 'csendes'

  print('Premissza: Panni ' + word1 + op + word2 + '.')

  word3 = uniformDraw(feature2);
  print('Konklúzió: Panni ' + word3 + '.')

  if (op == ' és '):
    ervenyes = 'érvényes' if (word2 == word3) else 'nem érvényes'
  else:
    ervenyes = 'érvényes'

  print(ervenyes);
  
  return ervenyes

def uniformDraw(array, chance = True):
    prob_number = random.random()
    if chance == True:
        return array[math.floor(random.random() * len(array))]
    else:
        value = ' vagy ' if 0.95 > prob_number else ' és '
        return value
    

def ComplexModel2():
  word1 = uniformDraw(feature1)
  op = uniformDraw(operator, False)
  if op == ' vagy ':
      op = ' vagy ' if random.random() > misinterpret_prob else ' és '
  word2 = uniformDraw(feature2)
  if (random.random() < dyslexia_prob):
    word2 = 'cserfes' if (word2 == 'csendes') else 'csendes'

  print('Premissza: Panni ' + word1 + op + word2 + '.')

  word3 = uniformDraw(feature2);
  print('Konklúzió: Panni ' + word3 + '.')

  if (op == ' és '):
    ervenyes = 'érvényes' if (word2 == word3) else 'nem érvényes'
  else:
    ervenyes = 'érvényes'

  print(ervenyes);
  
  return ervenyes

print('ComplexModel1 Tölt...')
ComplexModel1()
print('ComplexModel1 Vege. Kerem varjon par masodpercet')
time.sleep(5)
print('ComplexModel2 Tölt...')
ComplexModel2()


import itertools
def probability_dice_sum_at_least_4():
    total_outcomes = 6 * 6  # 2 kocka összes lehetséges kimenete 6x6
    favorable_outcomes = sum(1 for d1, d2 in itertools.product(range(1, 7), repeat=2) if d1 + d2 >= 4) #kedvező kimenetel   
    return favorable_outcomes / total_outcomes  # kedvező / összes kimenet
print("Annak a valószínűsége, hogy az összeg legalább 4: {:.2%}".format(probability_dice_sum_at_least_4()))  #eredmény
