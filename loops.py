i=0
while i < 10:
    i+=1
    print("*"*i)
num =12345
fact =1
while num > 0:
    fact *= num%10
    num = num//10
print(fact)


num = 54633
sum=0
while num > 0:
    sum=sum+num%10
    num=num//10
print(sum)


l=[1,2,3,4,5,6,7,8,9,10]
for item in l:
    if item%5 ==0:
        break
        print(items)
    else:
        print("loop exit successfully")