import random as r
random_num = r.randint(0 , 100)
count = 1
while count < 6:
    print(f"{6 - count} tries remaining")
    guessing_num = int(input("Guess the Number:"))
    if guessing_num < random_num:
        print("You're Guessing Low.")
    elif guessing_num > random_num:
        print("You're Guessing High.")
    else:
        print(f"Congrats! You guessed it in {count} tries.")
        break
    count += 1
if count == 6:
    print("Better Luck Next Time!")
    print("The Correct Answer is:" , random_num)
