#number
values = input().split(" ")
#convert values to int
values = [int(i) for i in values]
#number to print
number = 0
mid = int(values[0] / 2) + int(values[0] % 2)
#if the search number is even
if values[1] > mid:
    number = 2 * (values[1] - mid)
#else is odd
else:
    number = 2 * (values[1] - 1) + 1

#print the number
print(number)