x = input()

count = 0

for i in x:
    y = int(i)

    if x[y] == x[y+1]:
        count = count + 1
    else:
        continue
    print(x[y],count)
        

