# Base done, kolla för eventuella krav

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
    startpar = 0
    endpar = 0
    for a in inp:
        if a == "(":
            startpar += 1
        elif a == ")":
            endpar += 1
    if not startpar == endpar:
        raise ValueError("Uneven amount of parenthesis")
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

    def mostheight(self, cal):
        if cal > self.__height:
            self.__height = cal

    def deletet(self):
        self.__leaves = 0
        self.__height = 0

def parse_newick(terminal):

    if ";" not in terminal:
        raise ValueError("No end in sight")
    while " " in terminal:
        terminal.remove(" ")
    while "," in terminal:
        terminal.remove(",")
    present = Tree()
    cur, *other = terminal
    if other == [";"]:
       present.mostheight(1)
       present.addleaves()
    elif cur == "(":
       parse_main(terminal, 1, present,0)
    else: # Om nånting gick fel
       raise NameError("Något gick fel")
    return present
       

def parse_main(terminal, high, cla, leaf):
    if terminal == [";"]:
        return
    cur, *other = terminal
    if cur == "(":
        parse_main(other, high + 1, cla, 0)
    elif cur == ")":
        cla.mostheight(high)
        parse_main(other, high - 1, cla, 0)
    else:
        if leaf == 2:
            raise ValueError("Tree can't have 3 leaf silly!")
        cla.addleaves()
        parse_main(other, high, cla, leaf + 1)   


term1 = "(a, (b, (c, (d, e))));"
term2 = "((a,b), (c, d));"
term3 = "((a,b)[SECRET!],(b,c));" # Bracket killing
term4 = "(a,);" # Tom löv
term5 = "(((()));" # Ojämnt parenteser
term6 = "(1,2)" # Slut tecken utelagt
term7 = "(1,2,3);" # Triple leaf power

t = parse_newick(lexer(term3))
print(t.n_leaves())
print(t.height())




