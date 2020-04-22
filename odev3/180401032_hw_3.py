# Uniform Distribution
# 180401032

import sympy as sym
from sympy import Symbol
from sympy import *
import matplotlib.pyplot as plt
from sympy import Piecewise
import sympy.plotting as syp

a = Symbol(' a ')
b = Symbol(' b ')
x = Symbol(' x ')

uni_func = 1 / (b - a)
pprint(uni_func)

def uni_sympy():
    while (1):
        min = int(input("minimum val : "))
        max = int(input("maximum val : "))
        # min degerinin max degerinden daha dusuk olmasi icin kontrol ediyoruz.
        if min > max:
            print("try again")
        else:
            break

    syp.plot(Piecewise((0, (x < min) | (x > max)), (uni_func.subs({a: min, b: max}), (x >= min) & (x <= max))) ,
    (x, -10, 10), title="uniform distribution")

    uni_graph(min, max)


def uni_graph(min, max):
    count = float(0)
    x_value = []
    y_value = []
    uni_function = Piecewise((0, (x < min) | (x > max)), (uni_func.subs({a: min, b: max}), (x >= min) & (x <= max)))
    while count < 10.0:
        y = uni_function.subs({x: count})
        y_value.append(y)
        x_value.append(count)
        count+= 0.1
    plt.plot(x_value, y_value)
    plt.show()

uni_sympy()
