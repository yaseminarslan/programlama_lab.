# 08.04.20

from sympy import *
from sympy import Symbol
from sympy import factor
from sympy import expand
from sympy import pprint
import sympy.plotting as syp
import sympy as sym
import matplotlib.pyplot as plt

x = Symbol('x')
y = Symbol('y')

p = x * (x + x)
pprint("p = ", p)

p2 = (x + 2) * (x + 3)
print(p2)

from sympy import factor, expand
expr = (x**2) - (y**2)

factors = factor(expr)
expand = expand(factors)
pprint(factor(expr))
pprint(expand(factor(expr)))


expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
pprint(expand(factors))
pprint(factors)

def series():
    x = Symbol('x')
    series = x
    n = 5
    for i in range(2, n+1):
        series = series + (x**i) / i
    return series

pprint(series())

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1,y:2})
print(res)

r = expr.subs({x:1-y})
pprint(r)

x = Symbol('x')
series = x
n = 5 
x_value = 10
for i in range(2, n+1):
    series = series + (x**i) / i
series_value = series.subs({x:x_value})

pprint(series_value)

# --------------------------

#Formul gauss fonk

sigma = Symbol('sigma')
mu = Symbol('mu')
x = Symbol('x')

pprint(2*sym.pi*sigma)

part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part_2 = sym.exp(-1*((x-mu)*2) / (2*sigma*2))

gauss_function = part_1*part_2
pprint(gauss_function)

sym.plot(gauss_function.subs({mu:1, sigma:3}), (x, -100, 50), title = 'gauss_distribution')

for value in range(-5, 5):
    y = gauss_function.subs({mu:1, sigma:3, x:value}).evalf()
    print(value, y)

x__values = []
y__values = []
for value in range(-100, 100):
    y = gauss_function.subs({mu:1, sigma:3, x:value}).evalf()
    x__values.append(value)
    y__values.append(y)

plt.plot(x__values, y__values)
plt.show()
