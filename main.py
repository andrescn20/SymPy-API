#  Hay que instalar pip install antlr4-python3-runtime==4.10
# pip install sympy


# Aquí están los paquetes que deben ser importados
import antlr4
from sympy import *
from sympy.parsing.latex import parse_latex

# Aqui comienzo a definir la función de suma
# Esta funcion recibe como parámetro la ecuacion y el factor en latex
# Y da como resultado un string con el latex de la nueva ecuacion

#Muy importante, los inputs deben venir con una r al inicio, como en
# r"\frac {1 + \sqrt {\a}} {\b} = x^2"
# Esto,para que python pueda leer correctamente los backlashes

def suma(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = parse_latex(factor) # convierte de latex a formato Sympy
    eqLeft = parse_latex(parts[0]) + fac # Se suma al lado izquierdo el factor
    eqRight = parse_latex(parts[1]) + fac # Se suma al lado derecho el factor
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eqLatex  #Se devuelve la ecuacion en latex


## Pruebas
print(suma(r"\frac {1 + \sqrt {\a}} {\b} = x^2", "1"))
print(suma(r"\frac {1 + \sqrt {\a}} {\b} = x^2", "x"))
print(suma(r"\frac {1 + \sqrt {\a}} {\b} = x^2", "x^2"))