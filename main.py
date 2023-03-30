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

def Sumar(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = parse_latex(factor) # convierte de latex a formato Sympy
    eqLeft = parse_latex(parts[0]) + fac # Se suma al lado izquierdo el factor
    eqRight = parse_latex(parts[1]) + fac # Se suma al lado derecho el factor
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eqLatex  #Se devuelve la ecuacion en latex

def Restar(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = parse_latex(factor) # convierte de latex a formato Sympy
    eqLeft = parse_latex(parts[0]) - fac # Se suma al lado izquierdo el factor
    eqRight = parse_latex(parts[1]) - fac # Se suma al lado derecho el factor
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eqLatex  #Se devuelve la ecuacion en latex

def Multiplicar(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = parse_latex(factor) # convierte de latex a formato Sympy
    eqLeft = parse_latex(parts[0]) * fac # Se suma al lado izquierdo el factor
    eqRight = parse_latex(parts[1]) * fac # Se suma al lado derecho el factor
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eqLatex  #Se devuelve la ecuacion en latex

def Dividir(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = parse_latex(factor) # convierte de latex a formato Sympy
    eqLeft = parse_latex(parts[0]) / fac # Se suma al lado izquierdo el factor
    eqRight = parse_latex(parts[1]) / fac # Se suma al lado derecho el factor
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eqLatex  #Se devuelve la ecuacion en latex

def Simplificar(ecuacion):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    eqLeft = powdenest(simplify(parse_latex(parts[0]), inverse=True), force=True)  # Se suma al lado izquierdo el factor
    eqRight = powdenest(simplify(parse_latex(parts[1]), inverse=True), force=True)  # Se suma al lado derecho el factor
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eqLatex  #Se devuelve la ecuacion en latex




## Pruebas
print(Sumar(r"\frac {1 + \sqrt {\a}} {\b} = x^2", r"1"))
print(Restar(r"\frac {1 + \sqrt {\a}} {\b} = x^2", r"x"))
print(Multiplicar(r"\frac {1 + \sqrt {\a}} {\b} = x^2", r"x^2"))
print(Dividir(r"\frac {1 + \sqrt {\a}} {\b} = x^2", r"x^2"))

print(Simplificar(r"\frac {1 + \sqrt {\a}} {\b} = x^2"))
print(Simplificar(r"x^2+x+x+1=4"))
print(Simplificar(r"\frac {1 + \sqrt {\a}} {\b} = x^2"))
