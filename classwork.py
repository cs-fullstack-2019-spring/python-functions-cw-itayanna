def main():
    # prob1()
    # prob2()
    # prob3()
    # prob4()





# this funtion counts to thnumber provided by the user

def prob1():
    uI= int(input("enter a number to count to"))
    for x in range(uI+1):
        print(x)


# this function loops untill the user enetrs q

def prob2():
    usIn= ''
    while usIn!="q":
        usIn= input("tell me something good")

# this fucntion gets 2 numbers from the user and does variout math operations with them

def prob3():
    num1= int(input("pick a number"))
    num2= int(input("pick another"))

    def add(num1,num2):
        print(num1+num2)

    def mutiply(num1,num2):
        print(num1*num2)

    def subtract(num1,num2):
        print(num1-num2)

    def divide(num1,num2):
        print(num1/num2)

    add(num1,num2)
    mutiply(num1,num2)
    subtract(num1,num2)
    divide(num1,num2)

# this function lets the user decide witch operation to perferm rather than doing all of them

def prob4():
    num1= int(input("pick a number"))
    num2= int(input("pick another"))
    operation= input("Do you want to add, subtract, multiply, or divide?")

    def add(num1,num2):
        return (num1+num2)

    def mutiply(num1,num2):
        return (num1*num2)

    def subtract(num1,num2):
        return (num1-num2)

    def divide(num1,num2):
        return (num1/num2)

    if operation=='add':
        print(num1,"+",num2,"=",add(num1,num2))


    if operation=='subtract':
        print(num1,"-",num2,"=",subtract(num1,num2))

    if operation=='multiply':
        print(num1,"*",num2,"=",mutiply(num1,num2))

    if operation=='divide':
        print(num1,"/",num2,"=",divide(num1,num2))






















if __name__ == '__main__':
    main()
