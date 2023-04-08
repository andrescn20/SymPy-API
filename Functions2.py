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
    fac = factor # convierte de latex a formato Sympy
    eqLeft = parts[0] + fac # Se suma al lado izquierdo el factor
    eqRight = parts[1] + fac # Se suma al lado derecho el factor
    eq = Eq(eqLeft, eqRight) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eq  #Se devuelve la ecuacion en latex

def Restar(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = factor # convierte de latex a formato Sympy
    eqLeft = parts[0] - fac # Se suma al lado izquierdo el factor
    eqRight = parts[1] - fac # Se suma al lado derecho el factor
    eq = Eq(eqLeft, eqRight) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eq  #Se devuelve la ecuacion en latex

def Multiplicar(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = factor # convierte de latex a formato Sympy
    eqLeft = parts[0] * fac # Se suma al lado izquierdo el factor
    eqRight = parts[1] * fac # Se suma al lado derecho el factor
    eq = Eq(eqLeft, eqRight) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eq  #Se devuelve la ecuacion en latex

def Dividir(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = factor # convierte de latex a formato Sympy
    eqLeft = parts[0] * fac # Se suma al lado izquierdo el factor
    eqRight = parts[1] * fac # Se suma al lado derecho el factor
    eq = Eq(eqLeft, eqRight) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eq  #Se devuelve la ecuacion en latex

def Potencia(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = factor # convierte de latex a formato Sympy
    eqLeft = powdenest(Pow(parts[0], fac ),
                                      force=True) # Se suma al lado izquierdo el factor
    eqRight = powdenest(Pow(parts[1], fac ),
                                      force=True)# Se suma al lado derecho el factor
    eq = Eq(eqLeft, eqRight) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eq  #Se devuelve la ecuacion en latex

def Raiz(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    fac = factor # convierte de latex a formato Sympy
    eqLeft = powdenest(root(parts[0], fac ),
                                      force=True) # Se suma al lado izquierdo el factor
    eqRight = powdenest(root(parts[1], fac ),
                                      force=True)# Se suma al lado derecho el factor
    eq = Eq(eqLeft, eqRight) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eq  #Se devuelve la ecuacion en latex

def Simplificar(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    eqLeft = powdenest(simplify(parts[0], inverse=True), force=True)  # Se suma al lado izquierdo el factor
    eqRight = powdenest(simplify(parts[1], inverse=True), force=True)  # Se suma al lado derecho el factor
    eq = Eq(eqLeft, eqRight) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eq  #Se devuelve la ecuacion en latex

def Expandir(ecuacion, factor):
    parts = ecuacion.split("=")  # Divide la ecuacion en dos partes, dividiendo en el igual
    eqLeft = powdenest(expand(parts[0], inverse=True), force=True)  # Se suma al lado izquierdo el factor
    eqRight = powdenest(expand(parts[1], inverse=True), force=True)  # Se suma al lado derecho el factor
    eq = Eq(eqLeft, eqRight) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return eq  #Se devuelve la ecuacion en latex

def getLatex(ecuacion, factor): # Función cuyo único propósito es crear el latex
    eqLatex = latex(ecuacion) 
    return(eqLatex)
