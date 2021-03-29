from collections import Counter

#enter the nummber of shoes
n = int(input())

#shoe sizes in shop
size = list(map(int, input().split()))

#enter the number of customers
x = int(input())

#couting the number of shoe sizes available in the shop
y = Counter(x)
print(y)