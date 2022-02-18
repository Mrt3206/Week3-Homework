def perfect_number(n,m):
    """Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

The smallest perfect number is 6, which is the sum of 1, 2, and 3.

Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.

Write a function that finds perfect numbers between 1 and 1000. 
Check perfect numbers between 1 and 1000 and find the sum of 
the perfect numbers using reduce and filter functions."""

    maxnum=[x for x in range(n,m+1)]
    maxnumhalf=[x for x in range(1,(m+1)//2+1)]
    perfectnum=[]
    divisor=[]
  
    for i in maxnum :
        for j in maxnumhalf:
            if  i%j==0 and i!=j:
                divisor.append(j) 
        if sum(divisor)==i:
            perfectnum.append(i)
        divisor.clear()
    print(sum(perfectnum))
    return perfectnum
        
        
 #Test Case       
n=int(input("Begin :"))
m=int(input("End: "))
print(perfect_number(n,m))
