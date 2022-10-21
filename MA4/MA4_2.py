#!/usr/bin/env python3.9

from person import Person
import matplotlib.pyplot as plt
import numpy as np
def main():
    f = Person(7)
   # print(f.get())
   # print(f.fib())

    t2_py = []
    t2_numba = []
    fib2 = np.arange(20,31)
    for i in fib2:
        f.set(i)
        t2_py += [f.fib()[3]]
        t2_numba += [f.fib()[4]]
    plt.plot(fib2, t2_py)
    plt.plot(fib2, t2_numba)
    plt.savefig('fib2')

if __name__ == '__main__':
	main()
