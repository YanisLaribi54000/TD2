#==== Imports 

import math 

#==== Script/main 

class Fraction :
  """ Fraction est une classe permettant de creer et representer des fractions."""
  def __init__(self,n,d) :
	
    """ n est le numérateur, d le dénominateur, ce sont des entiers """
    
    self.numerateur = n
    
    self.denominateur = d 
  
  def afficher(self):
    
    """ on prend en entrée une Fraction et on l'affiche au format (n/d)"""
    
    print(f"({self.numerateur}/{self.denominateur})")
  
  def IsEqual(self,other):
    """prends en argument deux Fractions et test si elles sont égales """
    if self.numerateur == other.numerateur and self.denominateur == other.denominateur :
      return True
    return False 
  
  def add(self,other):
  	
    """ prends en argument deux fractions et retourne leurs somme sous forme de Fraction """

    num = self.numerateur * other.denominateur + other.numerateur*self.denominateur
    
    denom = self.denominateur*other.denominateur
    
    return Fraction(num,denom)


  def mult(self,other):
   
    """prends en argument deux fractions et retourne leurs produit sous forme de Fraction """

    num = self.numerateur*other.numerateur
    
    denom = self.denominateur*other.denominateur
    
    return Fraction(num,denom)
  
  def simplify(self):
    """prends en argument un Fraction et retourne sa version irréductible """
    
    p = math.gcd(self.numerateur,self.denominateur) # on calcul le pgcd
    
    num = self.numerateur//p # la division est entiere
    
    denom = self.denominateur//p
    
    return Fraction(num,denom)

def harmonique(n):
  """ Prends en argument un entier et retourne le n-ème terme de la serie harmonique """
  sum = Fraction(1,1)
  
  for k in range(1,n+1):
  
    sum = sum.add(Fraction(1,k))
    sum = sum.simplify() #on simplifie à chaque itération pour réduire la taille du numérateur et dénominateur
  
  print(f"valeur approchée : {sum.numerateur/sum.denominateur}\n") # au cas où la Fraction est trop grande pour etre affichée
  
  return sum


def leibniz(n) :
  
  sum = Fraction(1,1)
  
  for k in range(1,n+1):
    
    sum = sum.add(Fraction((-1)**k,2*k + 1))
    
    sum = sum.simplify()
  
  print(f"valeur approchée de la somme :{sum.numerateur/sum.denominateur}\n")
  
  print(f"valeur approchée de pi/4 : {math.pi/4}\n") # afin que l'on puisse comparer 
  
  return sum


def first_non_nul(liste):
  # cette fonction n'est utile que pour l'attribu valuation que je définis après 
  """ prends en entrée un liste et renvoi l'indice de la première occurence d'un entier non nul """
  for i in range(len(liste)) :
    if liste[i] != 0 :
      return i

class Polynomial :
  """Classe permettant de creer et d'afficher des polynomes à partir de la liste de ses coefficients"""

  def __init__(self,liste_coef):

    self.degre = len(liste_coef)-1
    
    self.valuation = first_non_nul(liste_coef) #valuation du polynome, indice du premier coef non nul

    self.coefs = liste_coef

  def __str__(self) :
    """ Prends en argument un polynome et l'affiche sous la forme ( X**2 + 3*X + 4 ) par exemple """

    poly = ""
    
    for i in range(len(self.coefs)-1,-1,-1) :
      
      if self.coefs[i] == 0 :
        continue
      elif self.coefs[i] == 1 and i != 0 :
        poly = poly + f"+ X**{i} "
      elif i == 0 :
        poly = poly + f"+ {self.coefs[i]} "
      elif i == 1 :
        poly = poly + f"+ {self.coefs[i]}*X "
      else :
        poly = poly + f"+ {self.coefs[i]}*X**{i} "
    
    print(f"({poly[1:]})")

  def add_poly(self,other) :

    """prends en argument deux polynomes et renvoie la somme de ces derniers sous forme de polynome """

    if self.degre == max(self.degre,other.degre):

      liste_res = self.coefs

      for i in range(other.degre + 1) :

        liste_res[i] += other.coefs[i]

      return Polynomial(liste_res)

    else :

      liste_res = other.coefs

      for i in range(self.degre + 1) :

        liste_res[i] += self.coefs[i]

      return Polynomial(liste_res)

  def deriv(self) :
    """ Prends en argument un polnyme et renvoie son polynome dérivé """

    liste_res = [ 0 for i in range(self.degre) ]

    for k in range(len(liste_res)):

      liste_res[k] = self.coefs[k+1]*(k+1)

    return Polynomial(liste_res)

  def integrate(self,cte) :
    """Prends en argument un polynome et une constante et renvoie une primitive de ce polynome avec cette constante d'intégration"""

    primitive = [ 0 for i in range(self.degre+2) ]

    primitive[0] = cte

    for k in range(self.degre+1):

      primitive[k+1] = round(self.coefs[k]/(k+1),3) # on arrondit au 3 ème chiffre après la virgule pour éviter d'avoir des coefficients trop longs

    return Polynomial(primitive)


#===== Tests 

if __name__ == "__main__" :
	
	#=== Tests pour la classe Fraction

  my_fraction = Fraction(32,13)
  frac2 = Fraction(25,7)
	
  frac3 = my_fraction.add(frac2) 
  frac4 = my_fraction.mult(frac2)
  frac5 = frac4.simplify()

  print(frac3.IsEqual(Fraction(549,91)))
  print(frac4.IsEqual(Fraction(800,91)))
  print(frac5.IsEqual(Fraction(800,91)))

  my_fraction.afficher()
  frac2.afficher()

  print(" Somme des deux précédentes fractions :\n ")
  frac3.afficher()
  
  print(" Version simplifié : \n")
  frac3.simplify().afficher()
  
  print(" Produit des deux précédentes fractions : \n")
  frac4.afficher()
  
  # Dans se qui suit on se cantonne à n = 1000 car les Fraction deviennent bien trop grosses pour n = 10 000 

  print(" Calcul de H(1000) : \n ")
  harmonique(1000).simplify().afficher()
  
  print(" Formule de leibniz pour n = 1000 : \n ")
  leibniz(1000).simplify().afficher()
	
  #=== Tests pour la classe Polyniomial 
  
  liste1 = [1,2,0,0,4,5,0,0,0,13,16]
  
  liste2 = [2,4,0,0,0,3,1,6]


  cte = 10

  my_polynome = Polynomial(liste1)
  
  poly2 = Polynomial(liste2)
  
  sum = my_polynome.add_poly(poly2)

  print("Le premier polynome est :\n")
  my_polynome.__str__()
  print(f"son degré vaut :{my_polynome.degre}\n")

  print("son polynome dérivé est :\n")
  my_polynome.deriv().__str__()

  print(f"une primitive ayant pour constante d'intégration {cte} est :\n")
  my_polynome.integrate(cte).__str__()


  print("le second est :\n")
  poly2.__str__()
  print(f"son degré vaut :{poly2.degre}\n")

  print("son polynome dérivé est :\n")
  poly2.deriv().__str__()

  print(f"une primitive ayant pour constante d'intégration {cte} est :\n")
  poly2.integrate(cte).__str__()

  print("la somme des deux polynomes donne :\n")
  sum.__str__()
  print(f"son degré vaut : {sum.degre}\n")

  print("son polynome dérivé est :\n")
  sum.deriv().__str__()

  print(f"une primitive ayant pour constante d'intégration {cte} est :\n")
  sum.integrate(cte).__str__()




