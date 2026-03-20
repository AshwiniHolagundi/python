class Student:
  name="x"
  subjects=0
  marks=[]
  total=0
  per=0

  def __init__(self,n,t):
    self.name=n
    self.subjects=t
    self.enter_marks()

  def enter_marks(self):
    print("------------------------------")
    print("Enter "+self.name + "'s marks")
    self.marks = [int(input("Enter marks of subject "+str(_+1)+": ")) for _ in range(self.subjects)]
    self.calculate()

  def calculate(self):
   self.total=sum(self.marks)
   self.per=self.total/self.subjects
   self.display()

  def display(self):
   print("---------"+self.name+"'s Result----------")
   print("Name: "+self.name)
   print("Total: "+str(self.total)+"   Percentage: "+str(self.per))
   print("Total subjects: "+str(self.subjects))
   print("Marks: "+str(self.marks))

def main():
 n=int(input("Total number of students: "))
 s=[]
 for i in range(n):
   name=input("Student "+str(i+1)+"'s name: ")
   tot=int(input("Student "+str(i+1)+"'s total subjects: "))
   s.append({"name": name, "sub": tot})

 for all in s:
  A = Student(all["name"], all["sub"])

main()

