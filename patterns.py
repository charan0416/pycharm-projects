def apha(n):
    p=65
    for i in range(n):
        for j in range(i+1):
            ch=chr(p)
            print(ch,end=" ")
        p+=1
        print()
apha(5)


def apha(n):
    p=65
    for i in range(n):
        for j in range(i,n):
            ch=chr(p)
            print(ch,end=" ")
        p+=1
        print()
apha(5)


def apha(n):
    p=65
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print(chr(p),end=" ")
        for j in range(i):
            print(chr(p),end=" ")
        p +=1
        print()
apha(5)

n=5
for i in range(n):
    for j in range (i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range (i):
        print("*",end=" ")
    print()
#
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range (i+1):
        print("*",end=" ")
    print()


n=5
for i in range (n):
    for j in range (i+1):
        print("",end=" ")
    for j in range (i,n):
        print("*",end=" ")
    print()
for i in range (n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range (i):
        print(p,end=" ")
        p+=1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()

n=5
p=5
for i in range (n):
    k=p
    for j in range(i+1):
        print(" ",end=" ")
    for j in range (i,n):
        print(k,end=" ")
        k-=1
    p-=1
    print()


n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
    for j in range(i):
        print(p,end=" ")
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
    for j in range(i+1,n):
        print(p,end=" ")
    p+=1
    print()


n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
    for j in range(i):
        print(p,end=" ")
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
    for j in range(i+1,n):
        print(p,end=" ")
    p-=1
    print()


n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=2
    print()


n=6
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        if i%2==0:
            print("z",end=" ")
        else:
            print("o",end=" ")
    for j in range(i,n-1):
        if i%2==0 :
            print("z",end=" ")
        else:
            print("o",end=" ")
    print()


n=5
for i in range(n):
    p=65
    for j in range (i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()

n=5
p=65
for i in range (n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    for j in range (i+1):
        print(chr(p),end=" ")
        p+=1
    print()


n=5
for i in range (n):
    p=69
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p-=1
    print()


n=5
k=69
for i in range (n):
    p=k
    for j in range(i+n):
        print(" ",end=" ")
    for i in range(i,n):
        print(chr(p),end=" ")
        p-=1
    k-=1
    print()
    p=69
    p-=1


n=5
k=69
for i in range (n):
    p=k
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(p),end=" ")
        p-=1
    k-=1
    print()


n=5
for i in range (n):
    p=65
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(chr(p),end=" ")
        p+=1
    for j in range(i+1):
        print(chr(p), end=" ")
        p-=1
    print()


s="CODER"
n=len(s)
p=0
for i in range(n):
    for j in range(i+1):
        print(s[p],end=" ")
    p+=1
    print()


s="CODER"
n=len(s)
p=n-1
for i in range(n):
    for j in range(i+1):
        print(s[p],end=" ")
    p-=1
    print()

s="CODER"
n=len(s)
for i in range(n):
    p=0
    for j in range(i+1):
        print(s[p],end=" ")
        p+=1
    print()

s="CODER"
n=len(s)
k=n-1
for i in range(n):
    p=k
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(s[p], end=" ")
        p-=1
    print()
    k-=1

