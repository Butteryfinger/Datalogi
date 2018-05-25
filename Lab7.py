def lexer(inp):
    inp = list(inp)
    while True:
        if "[" in inp:
            t1 = inp.index("[")
            if "]" in inp:
                t2 = inp.index("]")
                inp = inp[:t1] + inp[t2+1:]
        else:
            break
    return inp

class Tree:

    def __init__(self):
        self.__leaves = 0
        self.__height = 0
  
    def n_leaves(self):
        return self.__leaves

    def height(self):
        return self.__height

    def addleaves(self):
        self.__leaves += 1

    def addheight(self):
        self.__height += 1

d = "(a, ( b,[sfagdsfdsfs] c )));"
print(lexer(d))

def parse_newick(terminals):
    if cur == "(":
        
