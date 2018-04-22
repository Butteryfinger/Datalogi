# Lab 5
class Node:
    def __init__(self, key, val):
        self._key = key
        self._val = val
        self._left = None
        self._right = None

    def set_children(self, l, r):
        self._left = l
        self._right = r

    def data(self):
        return self._key, self._val

    def left_child(self):
        return self._left

    def right_child(self):
        return self._right
    

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        '''
        Public interface method to insert a key and value to the search tree.
        '''
        self.root = self.__insert(self.root, key, val)

    def __insert(self, v, key, val):
        '''
        Internal method to recursively decide where to insert a new node.
        Warning! This method has a bug, it does not behave according to specification!
        '''
        if v != None:
            v_key, x = v.data() # Ignoring x actually
            left = v.left_child()
            right = v.right_child()
            if key == v_key:
                self._val = val
            elif key < v_key:
                left = self.__insert(left, key, val)
            else:
                right = self.__insert(right, key, val)
            v.set_children(left, right)
            return v
        else:
            return Node(key, val)


    def find(self, key):
        return self._find(self.root, key)
        

    def _find(self, v, key):
        cur_key, cur_val = v.data()
        left = v.left_child()
        right = v.right_child()
        if cur_key == key:
            return cur_val
        elif key < cur_key:
            if left == None:
                  raise KeyError
            self._find(left, key)
        else:
            if right == None:
                  raise KeyError
            self._find(right, key)
	

    def remove(self, key):
        if self.root == None:
            print("Tree's empty")
        self._remove(self.root, key)
        


    def _remove(self, v, key):
        cur_key, o = v.data()
        left = v.left_child()
        right = v.right_child()
        if cur_key == key:
            if left != None or right != None:
                print("Leaf has children")
                return 
            v = None
            return
        elif cur_key < key:
            if right == None:
                print("ree")
                raise KeyError
            print("right")
            self._remove(right, key)
        else:
            if left == None:
                print("err")
                raise KeyError
            print("left")
            self._remove(left, key)
       


    def __size(self, v):
        left = v.left_child()
        right = v.right_child()
        if left != None:
            if right != None:
                return 1 + self.__size(left) + self.__size(right)
            return 1 + self.__size(left)
        if right != None:
            return 1 + self.__size(right)
        else:
            return 1

    def size(self):
        return self.__size(self.root)
        

    def __str__(self):
        return str(self.root)


def main():
    credits = BinarySearchTree()
    credits.insert('DA3018', 7.5)
    credits.insert('DA2004', 5)
    credits.insert('DA2003', 6)
    print(credits)
    n = credits.size()          # n = 3
    print(n)
    hp = credits.find('DA2004') # set hp to 5
    print(hp)
    print(credits.remove('DA2003'))
    print(credits.find('DA2003'))
    m = credits.size()          # m = 2
    print(m)

if __name__ == '__main__':
    main()    
