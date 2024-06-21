def print_formatted(number):
    p=bin(number)
    p=len(p)-1
    for i in range(number):
        a=i+1
        b=oct(a)
        c=hex(a)
        d=bin(a)
        A=str(a)
        B=str(b)[2:]
        C=str(c)[2:].upper()
        D=str(d)[2:]
        print((A).rjust(p-1)+(B).rjust(p)+(C).rjust(p)+(D).rjust(p))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)