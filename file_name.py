#link of the problem https://codeforces.com/problemset/problem/978/B

#read the input
n = int(input())
sequence = input()
input_seq = []
input_seq[:0] = sequence
#solving the problem
def solve():
    count = 0
    if len(input_seq) < 3:
        return 0
    else:
        x_cons = 0
        for i in range(n):
            if input_seq[i] == 'x' and x_cons >= 2:
                x_cons += 1
                count += 1
            elif input_seq[i] == 'x':
                x_cons += 1
            else:
                x_cons = 0
    return count



#result
result = solve()
print(result)