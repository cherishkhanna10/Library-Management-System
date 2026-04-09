Hotel_rooms={'A01':"Available",'A02':"Available",'A03':"Available",'A04':"Available",'A05':"Available",'B01':"Available",'B02':"Available",'B03':"Available",'B04':"Available",'B05':"Available",'C01':"Available",'C02':"Available",'C03':"Available",'C04':"Available",'C05':"Available"}
def welcome():
  print("Welcome to Cherish hotels")
welcome()
def fuct():
  print("1, Book room")
  print("2, checkout room")
  print("3, show rooms")
  print("4, exit")
def book_room():

def check_room():
def show_room():
while True:
  fuct()
  choice=input("Enter number alternative to the fuction to be performed(1(Book room)),(2(Checkout room)),(3(Show room)),(4(Exit)) ::")
  if choice=="1":
    book_room()
  elif choice=="2":
    check_out()
  elif choice=="3":
    show_room()
  elif choice=="4":
    print("exit from the program")
  else:
    print("Entered wrong value please try again")
  choice_con=input("Do you want to continue ??(yes/no)::")
  if choice_con=="yes":
    continue
  else:
    print("Thank you visit our hotel")
    break
    
    break



