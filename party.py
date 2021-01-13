#link to the problem https://codeforces.com/problemset/problem/115/A

#solve the problem
def solve(tree):
    levels = 0
    childs = []
    childs.append(tree[0])
    while len(childs) > 0:
        levels += 1
        new_childs = []
        for i in childs[0]:
            new_childs += tree[i]
        if len(new_childs) > 0:
            childs.append(new_childs)
        childs.pop(0)
    return levels             



#read the input
n = int(input())
#read input n times
node_list = []
for i in range(n + 1):
    node_list.append([])
for i in range(n):
    parent_pos = int(input())
    parent_pos = parent_pos + 1 if parent_pos < 0 else parent_pos
    node_list[parent_pos].append(i+1)

print(solve(node_list))
    


