n=int(input("Enter length: "))
ser=[0,1]
print("Fibonacci series")

def fib():
 if n==0:
  print("Enter a valid length")
  return 0
 elif n==1:
   print(0)
   return 0
 elif n==2:
   print("0,1")
   return 0
 elif n>2:
   t=n
   l=len(ser)
   while l!=t:
    ser.append(ser[l-1]+ser[l-2])
    l=len(ser)
 for i in ser:
  print(i,end=" ")

 print()
 return 0

fib()
