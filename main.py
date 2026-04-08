def welcome():
    print("Welcome to library management system ")
welcome()
def menu():
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")
list1=["om","elon","hr"]
def add_element():
    while True:
        add=input("enter book to be added ::")
        if add in list1:
            print("Book already exit in library")
        else:
            list1.append(add)
            print("Book added in library ::",list1)
        choice=input("Do you want to continue(yes/no)??::")
        if choice=="yes":
            continue
        else:
            print("Thank you for visit ")
            break          
while True:
    menu()
    choice=input("enter a number as per choice ::")
    if choice == "1":
        add_element()
        print("Add Book selected")

    elif choice == "2":
        print("Issue Book selected")

    elif choice == "3":
        print("Return Book selected")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")


