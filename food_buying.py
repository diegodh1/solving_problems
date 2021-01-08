#link for the problem https://codeforces.com/problemset/problem/1296/B

#solve the problem
def solve(n):
    count = 0
    while True:
        if n < 10:
            return n + count
        else:
            k = n // 10
            count += 10 * k
            n = (n - 10 * k) + (n // 10)

#read the input
times = int(input())
for i in range(times):
    n = int(input())
    print(solve(n))