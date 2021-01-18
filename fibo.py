import random
def fibo(x):
    if x==1 or x==2:
        return 1
    elif x==0:
        return 0
    elif x>2:
        return fibo(x-1)+fibo(x-2)
    elif x<1:
        return -1

x1=input("Give me a term of the  fibonacci sequence:  ")
x1=int(x1)
y=fibo(x1)
print("The fibo number is: ",y)

if y==0 or y==1:
    print("The fibonacci number of",x1,"is not prime.")
else:
  s=0
  for i in range(20):
     a=random.randrange(1,y)
     if pow(a,y,y)==a:
       s+=1
  if s==20:
     print("The fibonacci number of ",x1," is prime!")
  else:
     print("The fibonacci number of ",x1," is not prime!")
