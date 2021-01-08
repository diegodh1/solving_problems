#link of the problem https://codeforces.com/problemset/problem/1472/D

def even_odd_game(n, values):
    turn = True
    #split the even numbers from the odd numbers
    odd = []
    even = []
    sort_array = sorted(values)
    for i in range(n):
        if sort_array[i] % 2 == 0:
            even.append(sort_array[i])
        else:
            odd.append(sort_array[i])
    turn = True
    alice = 0
    bob = 0
    while len(odd) != 0 or len(even) != 0:
        if turn:
            if len(even) == 0:
                odd.pop()
            elif len(odd) == 0 or even[-1] > odd[-1]:
                alice += even.pop()
            else:
                odd.pop()
            turn = False
        else:
            if len(odd) == 0:
                even.pop()
            elif len(even) == 0 or odd[-1] > even[-1]:
                bob += odd.pop()
            else:
                even.pop()
            turn = True
    if alice == bob:
        return "Tie"

    return "Alice" if alice > bob else "Bob"




times = int(input())
for i in range(times):
    n = int(input())
    values = input().split(" ")
    values = [int(i) for i in values]
    print(even_odd_game(n, values))