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
    Comp.sort()
    return Prim, Comp

# Test med 10 000 element ger drygt 0.255 sek med unittest



