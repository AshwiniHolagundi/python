students=[]
class Student:
   def __init__(self,name,marks):
      self.name=name
      self.marks=marks
      self.total=sum(marks)
      self.percentage=self.total/x
   def display(self):
      print("Name:",self.name)
      print("Marks:",self.marks)
      print("total:",self.total)
      print("Percentage:",self.percentage,"%")
a = int(input("Enter the no of students:"))
for i in range(a):
   name=input("Enter Name:")
   x=int(input("Enter the total no of subject:"))
   marks=[]
   for j in range(x):
      m=int(input("Enter the marks for subject"+str(j+1)+":"))
      marks.append(m)
   s=Student(name,marks)
   students.append(s)
print("----STUDENT DETAILS----")
for s in students:
   s.display()
