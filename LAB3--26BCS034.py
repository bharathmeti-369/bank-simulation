##---26BCS034---Bharath meti----##

#----------------------------QUESTION 1---------------------------------------------

#Variables are (N,C,M)
N=eval(input("Enter the amount that Little Bob had in his pocket:"))
C=eval(input("Enter the amount of that chocolate:"))
M=eval(input("The number of Wrappers that to get a extra one chocolate:"))
#The number of chocolate that he get from his amount is N//C
A=N//C
print(f"-------------------The no of chocolates from his amount: {A}")
#The number of free/Extra chocolate he get from wrappers(M) is A//M
B=A//M
Total_no_of_Chocolate_that_Bob_gets_here_is=A+B
print(f"-------------------The Total no of Chocolte That Bob gets is: {A+B}")
#Answer--Enter the amount that Little Bob had in his pocket:5678
#Enter the amount of that chocolate:45
#The number of Wrappers that to get a extra one chocolate:7
#----****************The no of chocolates from his amount: 126
#----****************The Total no of Chocolte That Bob gets is: 144




#-------------------------------QUESTION 2--------------------------------------------


#The given information is:Basicpay,DA=80%of Basic pay ,HRA=30%of basic pay and PF is =12% of basic pay
Basic_pay=eval(input("Enter amount of salary paid as a Basic pay for an emloyee:"))
DA=0.8*Basic_pay
HRA=0.3*Basic_pay
PF=0.12*Basic_pay
Actual_amount_in_his_hand=Basic_pay+DA+HRA-PF
print(f"Basic_pay {Basic_pay}")
print(f"Dearness Allowence {DA}")
print(f"HRA {HRA}")
print(f"PF {PF}")
print(f"The actual amount that empolyee get in his hand is: {Actual_amount_in_his_hand}")
#Answeer--
#--Enter amount of salary paid as a Basic pay for an emloyee:67000
#--Basic_pay 67000
#--Dearness Allowence 53600.0
#--HRA 20100.0
#--PF 8040.0
#--The actual amount that empolyee get in his hand is: 132660.0

#++++++++++++++++++------ASSIGNMENT 2 of 3rd LAB----------+++++++++++++++++++++++++++++++


#EXPERIMENT 1------
Name=eval(input("Enter your name:"))
Department=eval(input("Enter your Department:"))
College=eval(input("Enter your college name:"))
print(f"Name: {Name}\n Department: {Departmnet}]\n College:{College}")



# EXPERIMENT 2-------
name=input("Enter your name:")
print("Your name is ",name)
#Enter your name:Bharath
#Your name is Bharath


#EXPERIMENT 3---------
a=input("Enter a value:")
print("The value is:",a)
print("The type is:",type(a))
#Answer==10
#3.14
#Bharath
#Type(a) showing is string


#EXPERIMENT 4--------------
a=input("Enter first number:")
b=input("Enter second number:")
c=a+b
print("Result:",c)
#answer==Enter first number:10
#Enter second number:20
#1020
# The output is 1020 because they both are string values


#experiment 5------------------
a=eval(input("Enter the first number:"))
b=eval(input("Enter the second number:"))
c=a+b
print("Result:",c)
#Enter the first number:12
#Enter the second number:34
#46
#Enter the first number:12.5
#Enter the second number:34
#46.5


#EXPERIMENT 6
a=eval(input("Enter the first number:"))
b=eval(input("Enter the second number:"))
print("sum:",a+b)
print("Difference=",a-b)
print("Product=",a*b)
print("Division=",a/b)
#Enter the first number:12
#Enter the second number:4
#Sum:16
#Difference=8
#Product=48
#Division=3.0



#Experiment 7:
a=eval(input("Enter the first number:"))
b=eval(input("Enter the second number:"))
print(" the sum is :",a+b)
#Enter the first number:12
#Enter the second number:4
#the sum is :16


#EXPERIMENT 8-----------------
name=input("Enter your name:")
age=eval(input("Enter your age:"))
print(name,"is",age,"years old")
#Bharath meti is 10 years old


#EXPERIMENT 9---------
length=eval(input("Enter length:"))
breadth=eval(input("Enter breadth"))
area=length*breadth
print("Area of recatangle =",area)
#Enter length:4
#Enter breadth5
#Area of recatangle =20


#EXPERIMENT 10:
p = eval(input("Enter principal amount: "))
r = eval(input("Enter rate of interest: "))
t = eval(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)
#Enter principal amount:1000
#Enter rate of interest:4
#Enter time:1 
#Simple Interest =40

#EXPERIMENT 11-
a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = eval(input("Enter third number: "))
average = (a + b + c) / 3
print("Average =", average)
#Enter the first number:12
#Enter the second number:4
#Enter the third number:2
#Average=7.0


##EXPERIMENT 12-----
name = input("Enter your name: ")
age = eval(input("Enter your age: "))
print("Name:", name, "Age:", age)
#Enter your name:Bharath meti
#Enter your age:34
#Name:Bharath meti Age:34


#EXPERIMENT 12-----
name = input("Enter your name: ")
age = eval(input("Enter your age: "))
print("My name is {name} and I am {age} years old.")
#Enter your name:Bharath meti
#Enter your age:34
#My name is Bharath meti and I am 34 years old.













