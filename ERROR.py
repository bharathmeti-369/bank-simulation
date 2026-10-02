a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
try:
    print(a/b)
except Exception as e:
    
    print(f"Error:{e}")
else:
    print("Enu error barlilla")
finally:
    print("Program ended! I dont care error barli barde irli")