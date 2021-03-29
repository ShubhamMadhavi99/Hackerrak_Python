import textwrap

def wrap(string, max_width):
    x = len(string)
    i = 0
    a = ""
    while i < x:
        y = string[i:i+max_width]
        i = i + max_width
        print(y)

    return a

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)