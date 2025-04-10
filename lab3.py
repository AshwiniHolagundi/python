import math
num=[]
n=int(input("Enter the number of element: "))

print("enter "+str(n)+" elements")
for i in range(n):
  el=int(input())
  num.append(el)

sum=0
for i in num:
 sum+=i

mean=sum/n

sum=0

for i in num:
 sum+=(i-mean)**2

var=sum/n

std=math.sqrt(var)

print("Entered list: "+str(num))
print("Sum: "+str(mean*n))
print("Mean: "+str(mean))
print("Variance: "+str(var))
print("Standard Deviation: "+str(std))


