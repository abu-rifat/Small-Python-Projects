numbers = [1]

for number in numbers:
    if number != 12:
        numbers.append(number+1)

print(f"The numbers: {numbers}")

LEN = len(numbers)
SUM = sum(numbers)
MAX = max(numbers)
MIN = min(numbers)

average = SUM/LEN
print(f"Sum of Numbers = {SUM}")
print(f"Length of Numbers = {LEN}")
print(f"Average of Numbers = {average}")
print(f"Max of Numbers = {MAX}")
print(f"Min of Numbers = {MIN}")

numbers2 = []
sum2 = 0
len2 = 0
max2 = 0
min2 = 0
ck = False
for number in range(1,12): #excluding 12
    numbers2.append(number)
    len2 = len2+1
    sum2 = sum2 + number
    if ck == False:
        ck = True
        max2 = number
        min2 = number
    else:
        if number > max2:
            max2 = number
        if number < min2:
            min2 =number

average2 = sum2 / len2

print(f"\nThe numbers2: {numbers2}")
print(f"Sum2 of Numbers = {sum2}")
print(f"Length2 of Numbers = {len2}")
print(f"Average2 of Numbers = {average2}")
print(f"Max2 of Numbers = {max2}")
print(f"Min2 of Numbers = {min2}")

numbers3 = []
for number in range(1,12,3): #step length 3
    numbers3.append(number)

print(f"\nThe numbers3 in [1,11] with step len 3: {numbers3}")

numbers4 = [*range(2,11,2)]
sumeven=0
for number in range(2,12,2):
    sumeven += number

print(f"\nThe numbers4: {numbers4}")
print(f"Sum of Even numbers4: {sumeven}")
