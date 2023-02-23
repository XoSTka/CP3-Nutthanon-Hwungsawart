item1, item2, item3, item4, item5 = "Salad", "Granola", "Bread", "Fruits", "Croissant"
Salad, Granola, Bread, Fruits, Croissant = 200, 70, 50, 100, 105
Username = input("Username : ")
Password = input("Password : ")
if Username == "Pp" and Password == "1234":
    print("-----------------------------")
    print("Welcome to Pp Supermarket")
    print("-----------------------------")
    print("Select Product You Want")
    print("-----------------------------")
    print("1.Salad      200 THB")
    print("2.Granola     70 THB")
    print("3.Bread       50 THB")
    print("4.Fruits     100 THB")
    print("5.Croissant  105 THB")
    print("-----------------------------")
    print("A:Yes, B:No")
    choice1 = input("Do you want to buy Salad :")
    if choice1 == "A":
        amount1 = int(input("How many Salad do you want :"))
    elif choice1 == "B":
        amount1 = 0
    choice2 = input("Do you want to buy Granola :")
    if choice2 == "A":
        amount2 = int(input("How many Granola do you want :"))
    elif choice2 == "B":
        amount2 = 0
    choice3 = input("Do you want to buy Bread :")
    if choice3 == "A":
        amount3 = int(input("How many Bread do you want :"))
    elif choice3 == "B":
        amount3 = 0
    choice4 = input("Do you want to buy Fruits :")
    if choice4 == "A":
        amount4 = int(input("How many Fruits do you want :"))
    elif choice4 == "B":
        amount4 = 0
    choice5 = input("Do you want to buy Croissant :")
    if choice5 == "A":
        amount5 = int(input("How many Croissant do you want :"))
    elif choice5 == "B":
        amount5 = 0
    else:
        print("Error")
    
    print("---------VAT Invoice---------")
    if amount1 != 0:
        print("Salad","        ","X",amount1,":",Salad*amount1,"THB")
    if amount2 != 0:
        print("Granola","      ","X",amount2,":",Granola*amount2,"THB")
    if amount3 !=0:
        print("Bread","        ","X",amount3,":",Bread*amount3,"THB")
    if amount4!= 0:
        print("Fruits","       ","X",amount4,":",Fruits*amount4,"THB")
    if amount5!= 0:
        print("Croissant","    ","X",amount5,":",Croissant*amount5,"THB")
        print("-----------------------------")
        print("Total","\t\t",":",(Salad*amount1)+(Granola*amount2)+(Bread*amount3)+(Fruits*amount4)+(Croissant*amount5),"THB")  
    
else:
    print("Incorrect Username or Password")