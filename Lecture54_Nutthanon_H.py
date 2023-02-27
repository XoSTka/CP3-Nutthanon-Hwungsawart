def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input("Which Choices :"))
    if userSelected ==1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()
    else:
        return menuSelect()

def vatCalculator():
    totalPrice = float(input("Total Price : "))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return price1 + price2

#*TODO Login => Showmenu => Menuselect => VAT or Price
print(login())