print("Welcome to Bill Calculator(with Tip).")

bill = input("What was the total bill? $")
bill = float(bill)

tip = input("What percentage of tip would you like to give [0 to 100]? ")
tip = float(tip)

tip = 0 if tip < 0 else tip
tip = 100 if tip > 100 else tip

total = bill + (bill * tip / float(100))

person = input("How many people to split the bill? ")
person = float(person)

per_person_bill = total / person
per_person_bill = round(per_person_bill, 2)

print(f"Each person should pay: ${per_person_bill}")