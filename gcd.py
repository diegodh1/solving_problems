
#link to the problem https://codeforces.com/problemset/problem/822/A

#solve the problem
def solve(a, b):
    min_v = min(a, b)
    if min_v == 0:
        return 0
    gcd = 1
    for i in range (min_v, 1, -1):
        gcd *=  i
    return gcd


#read inputs
values = input().split(" ")
values = [int(i) for i in values]
print(solve(values[0], values[1]))