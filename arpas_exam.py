#read the input
n = int(input())
#solving the problem
def solve():
    last_number = [6, 8, 4, 2]
    if n == 0:
        return 1
    else:
        pos = n % 4
        return last_number[pos]
#result
result = solve()
print(result)