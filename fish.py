n = int(input("Enter a number: "))
d = input("Enter your design charecter")
temp=int(n/2)+1

def gap(x):
 return " "*x


for i in range(int((n)/2)+2):
  print(gap(temp), end="")
  for j in range(i):
    print(d, end="")
  for j in range(i-1):
    print(d, end="")
  print(gap(temp*2), end="")
  for j in range(i):
    print(d, end="")
  print()
  temp=temp-1

temp=1
for i in range(int(n/2),0,-1):
  print(gap(temp), end="")
  for j in range(i):
    print(d, end="")
  for j in range(i-1):
    print(d, end="")
  print(gap(temp)*2, end="")
  for j in range(i):
    print(d, end="")
  print()
  temp=temp+1
print()

