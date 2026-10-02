class Student:
    def __init__(self,roll_no,name):
        self.roll_no=roll_no
        self.name=name
        self.__marks={}
    def get_marks(self):
        return self.__marks #we can write self__marks outside class by doing these
    def add_marks(self,subject,marks):
        self.__marks[subject]=marks
    def calculate_avg(self):
        total=0
        for mark in self.__marks.values():
            total+=mark
        average=total/len(self.__marks)
        print(f" {self.name}'s Average: {average}")
        return average
        
    def is_passed(self):
    #   has_failed=any(mark<35 for mark in self.__marks.values())  #any checks true or false and give answer true if correct,flase if wrong
        #it creates a list like [100,45,23,10]=[False,False,true,true]
        #or
        has_passed=all(mark>=35 for mark in self.__marks.values())
        if has_passed:
            print(f"{self.name} is passed")
        else:
            print(f"{self.name} is failed")
    def calculate_grade(self):
        print("Grade:",end="")
        percentage=self.calculate_avg() #TODO fix this not working properly(LEARNT TODO)first*100 was did
        if percentage>=90:
            print("A")
        elif percentage>=85:
            print("B")
        else:
            print("C")
class report_card:
    def generate(self,student=Student):
        student_marks=student.get_marks()
        print(f"{student.name}\t Roll no.{student.roll_no}")
        print("---Marks---")
        #for subject,marks in self.__marks it is aprivate we cannot access so we again made a get_marks def function and again we did it below line see
        for subject,marks in student_marks.items():
            print(f"{subject}-{marks}")
        print("________________________________")
        print(f"Average: {student.calculate_avg()}")
        student.is_passed()
        student.calculate_grade()
class classroom:
    def __init__(self,grade,section):
        self.grade=grade
        self.section=section
        self.__students=[]
    def add_student(self,student):
        self.__students.append(student)
    def calculate_class_average(self):
        pass
    def get_students_list(self):
        for i,student in enumerate(self.__students):
            print(f"{i+1}. {student.name}")

A=Student(1,"Bharath")
B=Student(2,"Savitri")
A.add_marks("Mathematics",97)
A.add_marks("Science",34)

#rc=report_card
#or
rc=report_card()
c=classroom("10","B")
rc.generate(A)
c.add_student(A)
c.add_student(B)
c.get_students_list()
       
#or in 57 line we can modify like this also see next line dude
#for student in self.__students:#also you can give a sorted for this (self.__students)
    #print(f"{student.roll_no}.{student.name}")