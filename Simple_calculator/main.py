# Simple Calculator : Build a command line calculator that can perform basic arithmetic operations(Add, Subtract, Multiply, Devide)

print("""
    ╔═╗╦╔╦╗╔═╗╦  ╔═╗  ╔═╗╔═╗╦  ╔═╗╦ ╦╦  ╔═╗╔╦╗╔═╗╦═╗
    ╚═╗║║║║╠═╝║  ║╣   ║  ╠═╣║  ║  ║ ║║  ╠═╣ ║ ║ ║╠╦╝
    ╚═╝╩╩ ╩╩  ╩═╝╚═╝  ╚═╝╩ ╩╩═╝╚═╝╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═""")




while True:
    print("**********************************************************")
    first_num = int(input("Enter first number : "))
    secont_num = int(input("Enter second number : "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Devide")
    print("5. Exit")

    choice = int(input("Choose operation : "))

    if choice == 1:
        print("Answer is :",first_num + secont_num)
    elif choice == 2:
        print("Answer is :",first_num - secont_num)
    elif choice == 3:
        print("Answer is :",first_num * secont_num)
    elif choice == 4:
        print("Answer is :",first_num / secont_num)
    elif choice == 5:
        break
    else:
        print("Choose a valid option")