print("Welcome to love calculator!")
your_name = input("Enter Your name: ").lower()
your_love = input("Enter your love's name: ").lower()

love_count = 0
true_count = 0

love_count += (your_name.count('l')+your_name.count('o')+your_name.count('v')+your_name.count('e'))
love_count += (your_love.count('l')+your_love.count('o')+your_love.count('v')+your_love.count('e'))

true_count += (your_name.count('t')+your_name.count('r')+your_name.count('u')+your_name.count('e'))
true_count += (your_love.count('t')+your_love.count('r')+your_love.count('u')+your_love.count('e'))

score = str(true_count)+str(love_count)
score = int(score)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <=50:
    print(f"Your score is {score}, you are already together.")
else:
    print(f"Your score is {score}.")
