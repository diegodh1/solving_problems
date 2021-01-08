
def count(n, values):
    odds = 0
    total = 0
    for i in range(n):
        if values[i] % 2 != 0:
            odds += 1
        total += values[i]
    mid = total / 2
    if mid % 2 == 0:
        return "YES"
    elif mid % 2 != 0 and odds > 0 and odds % 2 == 0:
        return "YES"
    else:
        return "NO"


times = int(input())
for i in range(times):
    n = int(input())
    values = input().split(" ")
    values = [int(i) for i in values]
    print(count(n, values))
