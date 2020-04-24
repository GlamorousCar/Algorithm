#implementing a binary tree and algorithms DFS, BFS
import collections
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
                #node - узел?
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node 
    def DFS(self):
        print(self.value, end='->')
        
        if self.left_child:
            self.left_child.DFS()
        if self.right_child:
            self.right_child.DFS()
    def BFS(self):
        queue = Queue()
        queue.put(self)
        
        while not queue.empty():
            n = queue.get()
            print(now_node.value)
            
            if n.left_child:
                queue.put(n.left_child)
            if n.right_child:
                queue.put(n.right_child)
a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_left('e')
b_node.insert_right('d')

c_node = a_node.right_child         #    a
c_node.insert_left('f')             # b     c
c_node.insert_right('g')             #d e   f g

d_node = b_node.left_child
e_node = c_node.right_child
f_node = c_node.left_child
g_node = c_node.right_child

print('Выполняем алгоритм DFS для бинарного дерева')
a_node.DFS()
print('Выполняем алгоритм BFS для бинарного дерева')
a_node.BFS()
