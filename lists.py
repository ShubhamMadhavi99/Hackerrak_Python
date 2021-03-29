n = int(input())

lst = []
output = []

for i in range(0,n):
    x = input().split()
    lst.append(x)


for i in lst:
    for j in i:
        if j == "insert":
            a = i[1]
            b = i[2]
            output.insert(int(a),int(b))
            
        
        elif j == "print":
            print(output)

        elif j == "remove":
            c = i[1]
            output.remove(int(c))
            
        
        elif j == "append":
            d = i[1]
            output.append(int(d))
            
        
        elif j == "sort":
            output.sort()
            
        
        elif j == "pop":
            output.pop()
            
        
        elif j == "reverse":
            output.sort(reverse=True )
        else:
            continue
