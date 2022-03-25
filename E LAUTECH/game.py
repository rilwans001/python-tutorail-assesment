import random
username = input("Enter username:")
print(f'okay,{username},i have guessed a number,can you guess it correctly?')
random_num = random.randint(1 , 10)
number_of_tries = 1
while number_of_tries < 4:
    user_num = int(input("Guess a number: "))
    if user_num == random_num:
        print("Guess  is correct")
        print(f'wow {username}, you guess correctly')
        print(f'you guess it right at the {number_of_tries} attempt')
        break
    elif user_num > random_num:
        print("Number is high")
        print(f'{username} you are a dullard')
    elif user_num < random_num:
        print("Number is low")
        print(f'{username} you are a dullard')

    else:
        print("invalid number")     
    number_of_tries += 1            