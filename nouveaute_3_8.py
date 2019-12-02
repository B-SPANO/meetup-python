# Liste des nouveauté en Python 3.8
# https://www.python.org/dev/peps/pep-0569/


# Quelques une des features les plus importantes:

# Le Morse n'est pas mort:
# Walrus operator
# Il permet l'affectation d'une valeur á une variable même si celle-ci n'as pas été déclarer.

a = [1, 2, 3, 4] 
if (n := len(a)) > 3: 
	print(f"List is too long ({n} elements, expected <= 3)") 


# Positional-Only Arguments
# pour completer la feature Keyword-only de Python 3.0

def greet(name, /, greeting="Hello"):
     return f"{greeting}, {name}"
 
greet("Łukasz")
'Hello, Łukasz'

greet("Łukasz", greeting="Awesome job")
'Awesome job, Łukasz'

greet(name="Łukasz", greeting="Awesome job")
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: greet() got some positional-only arguments passed as
            keyword arguments: 'name'

# another one:
def headline(text, /, border="♦", *, width=50):
    return f" {text} ".center(width, border)

# Il est possible de combiner les deux positional et keyword arguments
# en specifiant / et *. Dans l'exemple precedent 'text' est en positional, car
# on lui as passer "/" apres (il y aurait pu avoir d'autres arguments apres text
# et avant le "/"). 'border' est un arguments standart pouvant etre appelé de maniere
# positionelle ou nommée, 'width' quand a lui est nommé seulement.
# "*" permet de spécifier les arguments nommés exclusivement.


# Ajout de nouveaux Typages
Literal Types
Typed dictionaries
Final objects
Protocols


# Amelioration des F-Strings (débuggage simple intégré)

nom = "brice"
f"Mon nom est {name}"
'Mon nom est brice'

f"Mon nom est {name=}"
'Mon nom est name=brice'

# plus d'info en anglais sur:
# https://realpython.com/python-f-strings/