def addition(no1,no2):
    return  int(no1)+int(no2)

def subtraction(no1,no2):
    return int(no1)-int(no2)

def multiplication(no1,no2):
    return int(no1)*int(no2)

def division(no1,no2):
    if(int(no2) == 0):
        print("Cant divide by 0")
    else:
         return int(no1)/int(no2)

no1 = input("Please enter the first number: ")
no2 = input("Please enter the second number: ")

operation = input("Please enter the operation to be performed: ")

if(operation == "A"):
    iret = addition(no1,no2)
    print("The addition is "+ str(iret))

elif(operation == "S"):
    iret = subtraction(no1,no2)
    print("The subtraction is "+ str(iret))

elif(operation == "M"):
    iret = multiplication(no1,no2)
    print("The multiplication is "+str(iret))

elif(operation == "D"):
    iret = division(no1,no2)
    print("The Division is "+str(iret))

else:
    print("Please enter a valid operation")
