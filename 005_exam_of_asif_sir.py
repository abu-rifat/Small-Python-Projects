print(
    "\nWelcome to Asif sir's mid test!\n\n"
    "Sir have prepared 2 sets of ques for all the students. "
    "If your roll is odd, you will get set-1, else you will get set-2.\n"
    "For making things simple, you have to say only last 2 digits of your classroll, which is used to be a 2 digit integer.\n"
    "Example: if your classroll is '17CSE006', then you will say your roll as '06'\n"
)

roll = int(input("Enter your roll number (last 2 digits): "))
set = 0
if roll%2 == 0:
    set = 2
else:
    set = 1

print(f"\nYou will get ques set-{set}. Best of luck!")