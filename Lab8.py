from multiprocessing import Pool
import time
from functools import partial
#import matplotlib.pyplot as plt

def Sieve(n):
    Prim = list(range(2,n+1))
    Comp = []
    if len(Prim) < 3:
       return Prim, Comp
    else:
       Pointer = 0
    while Prim[Pointer]**2 < n:
       for e in Prim:
           if e == Prim[Pointer]:
               pass
           elif e%Prim[Pointer] == 0:
               Comp.append(e)
               Prim.remove(e)
       Pointer += 1
    Prim = list(set(Prim)-set(Comp))
    #Comp = sorted(Comp)
    return Prim, Comp

    # paralell variant, 2 trådar
def ThreadSieve(n):
    Prim = [] # För helheten skull
    ls1 = list(range(2,round(n/2))) # Två paralella listor
    ls2 = list(range(round(n/2), n+1))
    comp1 = ls1
    comp2 = ls2
    p = Pool(2)
    while ls1[0]**2 < n: # Första element i stora lista är alltid en primtal
       InrePrim = partial(innerPrim, prim = ls1[0]) # Högre ordning function
       Prim.append(ls1[0])
       ls1, ls2 = p.map(InrePrim, [ls1, ls2]) # Hugger ner 2 listor med aktuella primtal och ersätter listorna
    Prim = Prim + ls1 + ls2 # Primtal från båda halvor
    incomp = partial(compcount, prim = Prim)
    comp1, comp2 = p.map(incomp, [comp1, comp2]) # Threaded composit samling
    comp = comp1 + comp2
    return Prim, comp

def innerPrim(ls, prim): # Tar en prim och hugger ner stora lista av delbara tal
    comp = []
    for e in ls:
       if e%prim == 0:
           ls.remove(e)
    return ls

def compcount(inp, prim):
    return list(set(inp)-set(prim))

if __name__ == '__main__':
    
    ex = [100, 1000, 10000, 100000]
    thread = []
    serial = []

    for e in ex:
        now = time.time()
        ThreadSieve(e)
        (thread.append(round(time.time()-now, 5)))
    print("thread")
    print(thread)

    for e in ex:
        now = time.time()
        Sieve(e)
        (serial.append(round(time.time()-now, 5)))
    print("serial")
    print(serial)


    #plt.plot(thread, experiments)
    #plt.savefig("Threaded")

    #plt.plot(serial, experiments)
    #plt.savefig("Serial")

