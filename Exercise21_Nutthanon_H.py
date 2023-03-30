from tkinter import *
import math
mainWindow = Tk()

def lefclickbutton(event):
    BMI = (float(textbox_Weight.get()))/(math.pow(float(textbox_Height.get())/100,2))
    BMI = round(BMI,2)
    print("Your BMI is : ",BMI)
    label_BMI.configure(text=BMI)
#Todo Show Results
    if BMI >30:
        label_Results.configure(text="Extremely Overweight")
    elif BMI>25 and BMI<29.9:
        label_Results.configure(text="Overweight")
    elif BMI>23 and BMI<24.9:
        label_Results.configure(text="Overweight(Mild)")
    elif BMI>18.6 and BMI<22.9:
        label_Results.configure(text="Normal")
    else:
        label_Results.configure(text="Underweight")
    

#! ถ้าใส่ .grid() ต่อจาก textbox_Height หริอ textbox_Weight ไปเลย จะไม่สามารถนำข้อมูลออกมาใช้ได้ => ต้องไปเขียนแยกบรรทัด(บรรทัดที่9) ถึงจะเอาข้อมูลไปใช้ต่อได้

#Todo Create Height Data Label 
label_hieght = Label(mainWindow,text="Height").grid(row=0,column=0)
textbox_Height = Entry(mainWindow)
textbox_Height.grid(row=0,column=1)
label_cm = Label(mainWindow,text="cm"
).grid(row=0,column=2)

#Todo Create Weight Data Label 
label_weight = Label(mainWindow,text="Weight").grid(row=1,column=0)
textbox_Weight = Entry(mainWindow)
label_kg = Label(mainWindow,text="kg"
).grid(row=1,column=2)
textbox_Weight.grid(row=1,column=1)

#Todo Create Calculation Button
calculationButton = Button(mainWindow,text=" Calculate")
calculationButton.grid(row=2)

#Todo Event-Driven Pragramming 
calculationButton.bind("<Button-1>",lefclickbutton)

#Todo Create Label BMI and Results
label_BMI = Label(mainWindow,text="")
label_BMI.grid(row=2,column=1)
label_Results = Label(mainWindow,text="")
label_Results.grid(row=2,column=2)

#Todo Show the Program
mainWindow.mainloop()