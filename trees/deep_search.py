class Node:
    #constructor
    def __init__(self, data, parent):
        self.parent = parent
        self.data = data
        self.children = []
    #add children
    def add_child(self, child):
        self.children.append(child)
    #is root
    def is_root(self):
        return True if self.parent == None else False
    #is leaf
    def is_leaf(self):
        return True if len(self.children) == 0 else  False
    #get parent
    def get_parent(self):
        return self.parent

class Tree:
    def __init__(self, root):
        self.root = root
    
    #deep first search
    def dfs(self, x):
        node = self.root
        expanded_nodes = []
        visited_nodes = []
        expanded_nodes.append(node)
        found = False
        while len(expanded_nodes) > 0:
            if expanded_nodes[0].data == x:
                found = True
                visited_nodes.append(expanded_nodes[0])
                break
            else:
                element = expanded_nodes.pop(0)
                expanded_nodes = element.children + expanded_nodes
                visited_nodes.append(element)
        #print the path
        for x in visited_nodes:
            print(x.data)
        #return
        return found

    #breadth first search
    def bfs(self, x):
        node = self.root
        expanded_nodes = []
        visited_nodes = []
        expanded_nodes.append(node)
        found = False
        while len(expanded_nodes) > 0:
            if expanded_nodes[0].data == x:
                found = True
                visited_nodes.append(expanded_nodes[0])
                break
            else:
                element = expanded_nodes.pop(0)
                expanded_nodes =  expanded_nodes + element.children 
                visited_nodes.append(element)
        #print the path
        for x in visited_nodes:
            print(x.data)
        #return
        return found
    




root = Node(2, None)
child = Node(3, root)
child2 = Node(5, root)
child3 = Node(4, root)
child4 = Node(1, child)
child5 = Node(10, child)
child6 = Node(20, child2)
child7 = Node(50, child3)
child8 = Node(60, child3)
child9 = Node(70, child4)
child10 = Node(32, child4)
child4.children = [child9, child10]
child4.children = [child9, child10]
child.children = [child4, child5]
child2.children = [child6]
child3.children = [child7, child8]
root.children = [child, child2, child3]

tree = Tree(root)
print("___DFS___")
tree.dfs(60)
print("___BFS___")
tree.bfs(60)