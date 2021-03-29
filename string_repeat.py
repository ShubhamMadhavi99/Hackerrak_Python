def count_substring(string, sub_string):
    list1 = string 
    list2 = sub_string 
    k=0 
    for i in range(0,len(list1)): 
        if list1[i:i+len(list2)]==list2: 
            k=k+1
    return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)