from math import *

if __name__ == '__main__':
    data = {}
    data['coefficients'] = ''
    data['derivative'] = ''
print('If there is a sinx function input it as sin(x)')
print('If there is a cosx function input it as cos(x)')
print('If there is a tanx function input it as tan(x)')
print('If there is a cotx function input it as cot(x)')
print('If there is a secx function input it as sec(x)')
print('If there is a cscx function input it as csc(x)')
print('If there is a log(x)/log(base) function input it as log(x,base)')
print('If there is an lnx function input it as log(x)')
print('If there is a e^x function input it as exp(x)')
print('If there is a a^x function input it as pow(a,x)')
print('If there is an inverse sin(x) function input it as asin(x)')
print('If there is an inverse cos(x) function input it as acos(x)')
print('If there is an inverse tan(x) function input it as atan(x)')
print('If there is an inverse cot(x) function input it as acot(x)')
print('If there is an inverse sec(x) function input it as asec(x)')
print('If there is an inverse csc(x) function input it as acsc(x)')
print('Input x^ as x**')
print('Use the * to show multiplication. Ex: 3x^2 is 3*x**2')

function = input('Enter the function: ')
function = function.replace('cot','1/tan')
function = function.replace('sec','1/cos')
function = function.replace('csc','1/sin')
function = function.replace('acot','1/atan')
function = function.replace('asec','1/acos')
function = function.replace('acsc','1/asin')
deltax = float(input('Enter delta x: '))
y = float(input('Enter y value: '))
x = float(input('Enter x value: '))
finalx = float(input('Enter final x value: '))
deltay=0
if deltax >= 0:
    while x<=finalx:
        dydx=float(eval(function))
        deltay=dydx*deltax
        y+=deltay
        x+=deltax
if deltax <= 0:
    while x>=finalx:
        dydx=float(eval(function))
        deltay=dydx*deltax
        y+=deltay
        x+=deltax
print('y('+str(deltax)+'):',y)