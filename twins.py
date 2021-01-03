#README CODEFORCE PROBLEM LINK: https://codeforces.com/problemset/problem/160/A


#number coins
number_coins = int(input())
#money values
coins = input().split(" ")
coins = [int(i) for i in coins]
#sort money
def sort_money(money):
    n = len(money)
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if money[j] > money[j+1]:
                temp = money[j]
                money[j] = money[j+1]
                money[j+1] = temp
    return money

#get the minimun number of coins
coins = sort_money(coins)
total_money = sum(coins) / 2
actual_money = 0
number_coins = 0
while True:
    if len(coins) == 0:
        break
    else:
        if actual_money > total_money:
            break
        else:
            actual_money += coins.pop()
            number_coins += 1


print(number_coins)

