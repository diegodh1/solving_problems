
def jumps(n, values):
    max_value = 0
    memoize = [0] * n
    for i in range(n):
        pos = i
        temp = 0
        while pos < n:
            temp += values[pos]
            if memoize[pos] > temp:
                break
            else:
                memoize[pos] = temp
                pos += values[pos]
        max_value = max(max_value, temp)
    return max_value


times = int(input())
for i in range(times):
    n = int(input())
    values = input().split(" ")
    values = [int(i) for i in values]
    print(jumps(n, values))
