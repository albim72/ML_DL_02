from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer

def floop(a):
    for i in range(10000000):
        a[i]+=1

#dekorator Pythona -> funkcja dekorująca -> funkcja wrapper
@jit(target_backend='cuda')
def floopg(a):
    for i in range(10000000):
        a[i]+=1

if __name__ == '__main__':
    n = 10000000
    a = np.ones(n,dtype=np.float64)
    start = timer()
    floop(a)
    print(f"wynik z użyciem CPU: {timer()-start}")

    start = timer()
    floopg(a)
    print(f"wynik z użyciem GPU: {timer() - start}")




