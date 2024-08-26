op = '1'
result = int()

while(op != '='):
    if(op == '1'):
        v = int(input("\nEnter Number : "))
        result+=v
        op = input("\nOperations.....\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \nSelect Operation : ")

    elif(op == '2'):
        v = int(input("\nEnter Number : "))
        result-=v
        op = input("\nOperations.....\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \nSelect Operation : ")

    elif(op == '3'):
        v = int(input("\nEnter Number : "))
        result*=v
        op = input("\nOperations.....\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \nSelect Operation : ")

    elif(op == '4'):
        v = int(input("\nEnter Number : "))
        result/=v
        op = input("\nOperations.....\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \nSelect Operation : ")

print(f"\nResult : {result}\n")
