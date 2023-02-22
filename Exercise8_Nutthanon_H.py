'''
เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ

หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด
'''
Username = input("Username : ")
Password = input("Password : ")
if Username == "Pp" and Password == "1234":
    print("-----------------------------")
    print("Welcome to Pp Supermarket")
    print("-----------------------------")
    print("Select Product You Want")
    print("-----------------------------")
    print("1.Yummy Salad       200 THB")
    print("2.Granola Cereal     70 THB")
    print("3.Ham-Cheese Bread   50 THB")
    print("4.Fresh Fruits Set  100 THB")
    print("5.Croissant         105 THB")
    Yummy, Granola, Bread, Fruits, Croissant = 200, 70, 50, 100, 105
    select = int(input("Which one do you prefer(number) :"))
    if select == 1:
        amount1 = int(input("How many Yummy Salad :"))
    elif select == 2:
        amount2 = int(input("How many Granola Cereal :"))
    elif select == 3:
        amount3 = int(input("How many Ham-Cheese Bread :"))
    elif select == 4:
        amount4 = int(input("How many Fresh Fruits Set:"))
    elif select == 5:
        amount5 = int(input("How many Croissant :"))
    else:
        print("Invalid Input")
    print("A: Continue Buying")
    print("B: Check Out My Cart")
    choice = input("Waht do you want to do next :")
    
    
