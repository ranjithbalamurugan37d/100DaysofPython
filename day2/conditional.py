print("Welcome to the Rollercoaster!")
height = int(input("what is your hegiht?"))

total_bill =0

if height >120:
    print("You can ride in the rollercoaster")
    age  = int(input("what is your age?"))
    if age <= 12:
        print("You need to pay $5")
        total_bill+=12
    elif age>=18:
        if age >=45 and age <=55:
            total_bill =0
            print("You need to pay $0")
        else :
            total_bill+=7
            print("You need to pay $7 ")
    else:
        total_bill+=5
        print("You need to pay $12")
    wants_photo =str(input("If you want take a photo? Y or N."))
    if wants_photo.lower()=="y" :
        total_bill+=5
        print("You need to pay $3")
else :
    print("They can't ride.")

print(f"You need to pay total bill of{total_bill}")