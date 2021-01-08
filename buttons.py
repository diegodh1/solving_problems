#link of the problem https://codeforces.com/problemset/problem/268/B

#read the input
n = int(input())
#solving the problem
def solve():
    times = 0
    nivel = 1
    for i in range(n, 0, -1):
        if i == n:
            times += i
        else:
            times = times + i + (i-1) * nivel
            nivel += 1
    return times
#result
result = solve()
print(result)