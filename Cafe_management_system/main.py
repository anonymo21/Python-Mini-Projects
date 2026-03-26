# Cafe management system

menu_card = {"Tea":49, 
             "Coffee":99, 
             "Burger":99, 
             "Pizza":199, 
             "Salad": 79, 
             "Cock":49,
             "Pepsi":49}

def showMenu():
    for item,price in menu_card.items():
        print(f"{item}: Rs.{price}")

costumber_order = []
def takeOrder():
    order = input("Enter your first item you want to order : ").capitalize()
    costumber_order.append(order)
    while True:
        choice = input("Do you want to order anyything else? (Yes/No): ").capitalize()
        if choice == "Yes":
            another_order = input("Enter item you want to order : ").capitalize()
            costumber_order.append(another_order)
        elif choice == "No":
            break
        else:
            print("Please enter a valid item")
    print("Your order excuted!")

def showBill():
    bill = 0
    num = 1
    for item in costumber_order:
        print(f"{num}. {item} : Rs.{menu_card[item]}")
        price = menu_card[item]
        bill += price
        num +=1
    print("========================================")
    print(f"Your Bill is : Rs.{bill}")
 

def main():
    print("*******************************************************")
    print("""\033[32m╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╔═╗╦ ╦╦═╗  ╔═╗╔═╗╔═╗╔═╗
║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║  ║ ║║ ║╠╦╝  ║  ╠═╣╠╣ ║╣ 
╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝  ╚═╝╚═╝╩╚═  ╚═╝╩ ╩╚  ╚═╝\033[0m""")
    print("*****************Github-anonymo21**********************")

    showMenu()
    takeOrder()
    showBill()
    print("Thank You for visit our Cafe.")



if __name__ == "__main__":
    main()