""" Python interface to the C++ Person class """
import ctypes
lib = ctypes.cdll.LoadLibrary('./libperson.so')
from numba import njit
from time import perf_counter as pc

class Person(object):
    def __init__(self, age):
        lib.Person_new.argtypes = [ctypes.c_int]
        lib.Person_new.restype = ctypes.c_void_p
        lib.Person_get.argtypes = [ctypes.c_void_p]
        lib.Person_get.restype = ctypes.c_int
        lib.Person_set.argtypes = [ctypes.c_void_p,ctypes.c_int]
        lib.Person_delete.argtypes = [ctypes.c_void_p]
        lib.Person_fib.argtypes = [ctypes.c_void_p]
        lib.Person_fib.restype = ctypes.c_int
        self.obj = lib.Person_new(age)
    
    
    def get(self):
        return lib.Person_get(self.obj)

    def fib_py(self):

        def fib(n):
            if n <= 1:
                return n
            else:
                return(fib(n-1) + fib(n-2))
        start = pc()
        f = fib(self.get())
        end = pc()
        t_py = end - start
        
        return [f, t_py]
    
    def fib_numba(self):
        
        @njit
        def fib(n):
            if n  <= 1:
                return n
            else:
                 return(fib(n-1) + fib(n-2))
        start = pc()
        f = fib(self.get())
        end = pc()
        t_numba = end - start

        return [f, t_numba]
    
    def fib_cpp(self):
        start = pc()
        f = lib.Person_fib(self.obj)
        end = pc()
        t_cpp = end - start
        return [f, t_cpp]

    def set(self, age):
        lib.Person_set(self.obj, age)

    def __del__(self):
        return lib.Person_delete(self.obj)


