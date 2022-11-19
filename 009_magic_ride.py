print("Welcome to Magic ride!")
height = int(input("Enter your height (cm): "))
age = int(input("Enter your age (years): "))
want_photo = input("Want to take photos? Y or N? ")

bill = 0

if height < 120:
    print("You can't ride.")
else:
    if age >= 45 and age <=55:
        print("You can ride for free!")
    else:
        if age < 12:
            bill += 5
        elif age >= 12 and age <= 18:
            bill += 7
        else:
            bill += 12

        if want_photo == 'Y':
            bill += 3

        print(f"The total bill is ${bill}.")