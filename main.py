print("Welcome to  the  US Rollercoaster !")
height = int(input("What is your height (in cm) ?"))

if height > 120:
    print("You can ride the Rollercoaster!")

    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Your ticket bill is $5")

    elif age >= 44 and age <= 56:
        print("Everything is going to be ok . Have a free ride on us!")


    elif age >= 18:
        bill = 12
        print("Your ticket bill is $12")


    else:
        bill = 8
        print("Your ticket bill is $8")

    want_photo = input("Do you want a photo taken? Y or N?")
    if want_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry,you have to grow taller before you can ride!")

