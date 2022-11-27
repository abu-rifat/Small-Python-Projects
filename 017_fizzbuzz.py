print("FizzBuzz from 1 to 100:")
fizbuzz = []

for num in range(1,101):
    if num%15 == 0:
        fizbuzz.append("FizzBuzz")
    elif num%3 == 0:
        fizbuzz.append("Fizz")
    elif num%5 == 0:
        fizbuzz.append("Buzz")
    else:
        fizbuzz.append(num)

print(fizbuzz)