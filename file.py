
import os
if os.path.exists("bill"):
  f=open("bill","w")
else:
  f=open("bill","xw")


items=[]
price=[]
n=int(input("Enter the number of items: "))
for i in range(n):
 item=input("Enter item "+str(i)+" name: ")
 items.append(item)
 item=int(input("Enter item "+str(i)+" price: "))
 price.append(item)

sum=0
for i in price:
 sum+=i

for i in range(n):
  f.write(items[i]+"  "+str(price[i])+"\n")

f.write("------------------------\n")
f.write("Total: "+str(sum))
f.close()
