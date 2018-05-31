from multiprocessing import Process
import time
#import matplotlib.pyplot as plt

def Sieve(n):
    Prim = list(range(1,n+1))
    Comp = []
    if len(Prim) < 3:
       return Prim, Comp
    else:
       Pointer = 1
    while Prim[Pointer]**2 < n:
       for e in Prim:
           if e == Prim[Pointer]:
               pass
           elif e%Prim[Pointer] == 0:
               Comp.append(e)
               Prim.remove(e)
       Pointer += 1
    Prim = list(set(Prim)-set(Comp))
    Comp = sorted(Comp)
    return Prim

# Test med 10 000 element ger drygt 0.205 sek med time modulen

if __name__ == '__main__':
    experiments = list(range(2,6))
    thread = []
    serial = []

    
    for it in experiments:
        jobs = []
        now = time.clock()
        S = Process(target = Sieve, args = (10**it,))
        jobs.append(S)
        S.start()
        S.join()
        thread.append(time.clock()- now)
    print(thread)

    """
    for it in experiments:
        now = time.clock()
        Sieve(10**it)
        serial.append(time.clock() - now)
    print(serial)
    
    
    now = time.clock()
    Sieve(10**5)
    print(time.clock() - now)
    
    jobs = []
    now = time.clock()
    while True:
        S = Process(target = Sieve, args = (10**5,))
        
        S.start()
        #S.join()
        break
    print(time.clock()- now)
    """

    #plt.plot(thread, experiments)
    #plt.savefig("Threaded")

    #plt.plot(serial, experiments)
    #plt.savefig("Serial")
        

# Intressant att vid låga antal, så märks nästan ingen förbättring

# Ser om skolans dator är bättre.

# Misc frågor om vissa ämne
# Vid heaps, kan det finnas "tomma" löv alltså gren 3 och 5 har löv men inga andra vid samma nivå
# Vilka graph metoder finns det annars

