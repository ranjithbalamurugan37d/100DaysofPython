print("Welcome to the pizz land")
size = input("Which type of pizz do you want?Enter S or M or L.")
isPeperoniAdd = input("Are you want to add paperoni to your pizza? Y or N.")
isExtracheese = input("Do you want to add extra cheese to your pizza? Y or N.")

total_bill = 0

if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
elif size == "L":
    total_bill += 25
if isPeperoniAdd =='Y':
    if size == "S":
        total_bill += 2
    else :
        total_bill += 3
if isExtracheese == "Y":
    total_bill +=1

print(f"Your final bill is: ${total_bill}")