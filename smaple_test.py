def fizzbuzz(n):
    for i in range(1,n+1,1):
        if i % 3 == 0:
            print ("FizzBuzz")
            if i % 5 == 0:
                print("Fizz")
            else:
                continue
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)



n = int(input())
fizzbuzz(n)