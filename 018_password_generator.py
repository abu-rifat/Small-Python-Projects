import random,os

os.system('clear')

symbols = ['!','#','$','%','&','(',')','*','+']
letters ="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
print("Welcome to Password Generator:\n\n")
count = [0,0,0]
count[0] = int(input("How many English letters you want in the password?\n"))
count[1] = int(input("How many numbers you want in the password?\n"))
count[2] = int(input("How many symbols you want in the password?\n"))

total_len = sum(count)

password = ""

for i in range(0,total_len):
    k=0
    while True:
        k = random.randint(0, 2)
        if count[k] > 0:
            break
    
    if k == 0:
        idx=random.randint(0,51)
        password += letters[idx]
    elif k == 1:
        num=random.randint(0, 9)
        password += str(num)
    else:
        idx=random.randint(0, 8)
        password += symbols[idx]
    count[k] -= 1

password = list(password) #String to List
random.shuffle(password) #Suffle the List
password = ''.join(password) #List to String

print(f"\nPassword Size: {len(password)}")
print(f"Passowrd: {password}")
