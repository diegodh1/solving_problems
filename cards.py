#w = size card 1, h = size card 2 and n = number friends

def count(w, h, n, total):
    if total >= n:
        return total
    if w % 2 != 0 and h % 2 != 0:
        return total
    elif w % 2 != 0:
        total += 2
        return count(w, h / 2, n, total)
    else:
        total += 2
        return count(w / 2, h, n, total)

times = int(input())
for i in range(times):
    values = input().split(" ")
    values = [int(i) for i in values]
    result = count(values[0], values[1], values[2], 0)
    result = 1 if result == 0 else result
    response = "YES" if result >= values[2] else "NO"
    print(response)
