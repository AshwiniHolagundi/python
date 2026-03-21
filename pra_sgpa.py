class Result:
  sub=0
  marks=[]
  sgpa=0.0000
  total=0
  per=0.0000
  def __init__(self,n):
    self.sub=n
    self.marks=[[int(input(f"Enetr subject "+str(i+1)+" marks: ")), int(input(f"Enetr subject "+str(i+1)+" credits: "))] for i in range(n)]
    self.calculate()

  def calculate(self):
    grades=0
    credits=0
    for s in range(self.sub):
     m=self.marks[s][0]
     c=self.marks[s][1]
     g=0
     self.total+=m
     if m > 91:
        g=10
     elif m > 81:
        g=9
     elif m > 71:
        g=8
     elif m > 61:
        g=7
     elif m > 51:
        g=6
     elif m > 41:
        g=5
     elif m > 31:
        g=4
     else:
        g=3

     grades+=g*c
     credits+=c
    self.sgpa=grades/credits
    self.per=self.sgpa*10

  def display(self):
    print("Subjectwise marks and credits")
    for i in range(self.sub):
     print(self.marks[i])
    print("Total: "+str(self.total))
    print("SGPA: "+str(self.sgpa))
    print("Percentage: "+str(self.per))

def main():
  subs=[]
  sem=int(input("How many sem sgpa do you want to calculate? :"))
  sems=[]
  for s in range(sem):
    sub=int(input(f"Enter total subjects in sem {s+1}: "))
    subs.append(sub)
  for s in range(sem):
   print("---------------------------")
   print(f"Enter details of sem {s+1}")
   print("---------------------------")
   A = Result(subs[s])
   sems.append(A)

  for s in range(sem):
   print("---------------------------")
   print(f"Result of sem {s+1}")
   print("---------------------------")
   sems[s].display()
main()
