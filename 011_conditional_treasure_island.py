print("Welcome to Treasure Island!\nYour mission is to find the treasure.")
result = "Game Over."
move = input("Left or Right? ").lower()
if move == "left":
    move = input("Swim or Wait? ").lower()
    if move == "wait":
        move = input("Which door? Red, Yellow, or Blue? ").lower()
        if move == 'yellow':
            result = "You Win!"

print(result)
