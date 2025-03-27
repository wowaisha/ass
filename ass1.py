import math,random  #importalja a a math es random modulokat

feature1 = ['könyvtáros', 'tanár']  #meghatarozza az elso lehetseges szot
feature2 = ['csendes', 'cserfes']  #meghatarozza a masodik lehetseges szot
operator = [' és ', ' vagy ']  #az elso es masodik szo kozti op
dyslexia_prob = 0.5  #a diszle


def uniformDraw(array):
  return array[math.floor(random.random() * len(array))]

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

ComplexModel1()

