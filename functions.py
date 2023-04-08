#  Hay que instalar pip install antlr4-python3-runtime==4.10
# pip install sympy


# Aquí están los paquetes que deben ser importados
import antlr4
from sympy import *
from sympy.parsing.latex import parse_latex

# Aqui comienzo a definir la función de suma
# Esta funcion recibe como parámetro la equation y el factor en latex
# Y da como resultado un string con el latex de la nueva equation

#Muy importante, los inputs deben venir con una r al inicio, como en
# r"\frac {1 + \sqrt {\a}} {\b} = x^2"
# Esto,para que python pueda leer correctamente los backlashes

def Sumar(equation, factor):
    fac = parse_expr(factor) # convierte de latex a formato Sympy
    eqLeft = parse_expr(equation).lhs + fac # Se suma al lado izquierdo el factor
    eqRight = parse_expr(equation).rhs + fac # Se suma al lado derecho el factor
    eq = str(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return {'sympy' : eq , 'latex' : eqLatex }  #Se devuelve la equation en ambos formatos

def Restar(equation, factor):
    fac = parse_expr(factor) # convierte de latex a formato Sympy
    eqLeft = parse_expr(equation).lhs - fac # Se suma al lado izquierdo el factor
    eqRight = parse_expr(equation).rhs - fac # Se suma al lado derecho el factor
    eq = str(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return {'sympy' : eq , 'latex' : eqLatex }  #Se devuelve la equation en ambos formatosx
 

def Multiplicar(equation, factor):
    fac = parse_expr(factor) # convierte de latex a formato Sympy
    eqLeft = parse_expr(equation).lhs * fac # Se suma al lado izquierdo el factor
    eqRight = parse_expr(equation).rhs * fac # Se suma al lado derecho el factor
    eq = str(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return {'sympy' : eq , 'latex' : eqLatex }  #Se devuelve la equation en ambos formatos

def Dividir(equation, factor):
    fac = parse_expr(factor) # convierte de latex a formato Sympy
    eqLeft = parse_expr(equation).lhs * fac # Se suma al lado izquierdo el factor
    eqRight = parse_expr(equation).rhs * fac # Se suma al lado derecho el factor
    eq = str(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return {'sympy' : eq , 'latex' : eqLatex }  #Se devuelve la equation en ambos formatos

def Potencia(equation, factor):
    fac = parse_expr(factor) # convierte de latex a formato Sympy
    eqLeft = powdenest(Pow(parse_expr(equation).lhs, fac ),
                                      force=True) # Se suma al lado izquierdo el factor
    eqRight = powdenest(Pow(parse_expr(equation).rhs, fac ),
                                      force=True)# Se suma al lado derecho el factor
    eq = str(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return {'sympy' : eq , 'latex' : eqLatex }  #Se devuelve la equation en ambos formatos

def Raiz(equation, factor):
    fac = parse_expr(factor) # convierte de latex a formato Sympy
    eqLeft = powdenest(root(parse_expr(equation).lhs, fac ),
                                      force=True) # Se suma al lado izquierdo el factor
    eqRight = powdenest(root(parse_expr(equation).rhs, fac ),
                                      force=True)# Se suma al lado derecho el factor
    eq = str(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return {'sympy' : eq , 'latex' : eqLatex }  #Se devuelve la equation en ambos formatos

def Simplificar(equation, factor):
    eqLeft = powdenest(simplify(parse_expr(equation).lhs, inverse=True), force=True)  # Se suma al lado izquierdo el factor
    eqRight = powdenest(simplify(parse_expr(equation).rhs, inverse=True), force=True)  # Se suma al lado derecho el factor
    eq = str(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return {'sympy' : eq , 'latex' : eqLatex }  #Se devuelve la equation en ambos formatos

def Expandir(equation, factor):
    eqLeft = powdenest(expand(parse_expr(equation).lhs, inverse=True), force=True)  # Se suma al lado izquierdo el factor
    eqRight = powdenest(expand(parse_expr(equation).rhs, inverse=True), force=True)  # Se suma al lado derecho el factor
    eqLatex = latex(Eq(eqLeft, eqRight)) # Se combinan los dos lados en una nueva ecuación, en formato latex
    return {'sympy' : equation , 'latex' : eqLatex }  #Se devuelve la equation en ambos formatos

