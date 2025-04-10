alpha="abcdefghijklmnopqrstuvwxyz"

def encrypt():
  a = list(input("Enter your text: "))
  k = int(input("Enter your key:" ))
  res=""
  for i in a:
    if i != " ":
     n=a.index(i)
     res=res+str(alpha[(alpha.index(i)+k)%26])
    else:
     res+=" "
  return res


def decrypt():
  a = list(input("Enter your text: "))
  k = int(input("Enter your key:" ))
  res=""
  for i in a:
    if i != " ":
     n=a.index(i)
     res=res+str(alpha[(alpha.index(i)-k)%26])
    else:
     res+=" "
  return res


def start():
  k = 1
  while k==1:
   print("1. Encrypt   2. Decrypt  3. End")
   i = int(input("Enter your choice: "))
   print("------------------------------------")
   if i == 1:
    print(encrypt())
    print("***********************************")
   elif i==2:
    print(decrypt())
    print("***********************************")
   elif i==3:
    k=0
   else:
    print("Enter correct choice")


start()
