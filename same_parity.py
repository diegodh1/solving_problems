#link to the problem https://codeforces.com/problemset/problem/1352/B

#solve problem with only even numbers
def solve_even(values):
    n = values[0]
    k = values[1]
    sum_value = 0
    list_v = [2] * (k - 1)
    rest = n - 2 * (k - 1)
    if rest % 2 == 0 and rest > 0:
        list_v.append(rest)
        string_ints = [str(int) for int in list_v]
        return "YES", " ".join(string_ints)
    else:
        return "NO", None

#solve problem with only odd numbers
def solve_odd(values):
    n = values[0]
    k = values[1]
    sum_value = 0
    list_v = [1]* (k - 1)
    rest = n - (k - 1)
    if rest % 2 != 0 and rest > 0:
        list_v.append(rest)
        string_ints = [str(int) for int in list_v]
        return "YES", " ".join(string_ints)
    else:
        return "NO", None

#read the input
times = int(input())
#read input n times
for i in range(times):
    values = input().split(" ")
    values = [int(i) for i in values]
    res, arra = solve_even(values)
    if res == "YES":
        print(res)
        print(arra)
    else:
        res, arra = solve_odd(values)
        print(res)
        if res == "YES":
            print(arra)
