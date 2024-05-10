import nltk

# Definimos los símbolos no terminales
v0 = nltk.Nonterminal('v0')
v1 = nltk.Nonterminal('v1')
v1_prime = nltk.Nonterminal("v1'")
v2_prime = nltk.Nonterminal("v2'")
a = nltk.Nonterminal('a')
b = nltk.Nonterminal('b')
c = nltk.Nonterminal('c')

# Definimos las reglas de producción
production_rules = [
    nltk.Production(v0, ['aa', v0]),
    nltk.Production(v0, ['b', v1]),
    nltk.Production(v1, ['c', v1_prime, 'b']),
    nltk.Production(v1_prime, ['c', 'b']),
    nltk.Production(v2_prime, ['a', 'b', v2_prime]),
    nltk.Production(v2_prime, ['b', 'b'])
]

# Creamos la gramática
GRAMA = nltk.CFG(v0, production_rules)

# Imprimimos la gramática
print("Gramática:")
print(GRAMA)
print("\n")

# Alfabeto
alf = {'a', 'b', 'c'}
print("Alfabeto:", alf)

# Palabras terminales
pala = {'aa', 'b', 'c'}
print("Palabras Terminales:", pala)

# Estructura de producción
print("Estructura de Producción:")
for production in production_rules:
    print(production)

# Símbolos especiales
simbolos_especiales = {v0, v1, v1_prime, v2_prime, a, b, c}
print("Símbolos Especiales:", simbolos_especiales)

