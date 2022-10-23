#!/usr/bin/env python3.9

from person import Person
import matplotlib.pyplot as plt
import numpy as np
def main():
    f = Person(7)
    #print(f.fib_cpp())
    
    #fib1 = np.arange(30,46)
    #t1_py = []
    #t1_numba = []
    #t1_cpp = []
    
    #for i in fib1:
    #    f.set(i)
    #    t1_py += [f.fib_py()[1]]
    #    t1_numba += [f.fib_numba()[1]]
    #    t1_cpp += [f.fib_cpp()[1]]
    #    print(i)
    #plt.plot(fib1, t1_py, 'o-')
    #plt.plot(fib1, t1_numba, 'o-')
    #plt.plot(fib1, t1_cpp, 'o-')
    #plt.legend(labels = ['python', 'numba', 'c++'])
    #plt.savefig('fib1')

    t2_py = []
    t2_numba = []
    fib2 = np.arange(20,31)

    for i in fib2:
        f.set(i)
        t2_py += [f.fib_py()[1]]
        t2_numba += [f.fib_numba()[1]]
    plt.plot(fib2, t2_py, 'o-')
    plt.plot(fib2, t2_numba, 'o-')
    plt.legend(labels = ['python', 'numba'])
    plt.savefig('fib2')

    f.set(47)
    print(f.fib_numba(), 'fib(47) with numba')
    print(f.fib_cpp(), 'fib(47) with c++')
if __name__ == '__main__':
	main()
