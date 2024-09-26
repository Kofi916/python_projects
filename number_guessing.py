import random

number_to_guess = random.randint(1, 100)
max_attempts = 10
attempts = 0

print("Welcome to the Number Guessing Game!")
print(f"You have {max_attempts} attempts to guess the number between 1 and 100.")

while attempts < max_attempts:
    try:
        guess = int(input('Guess the number: '))
        attempts += 1
        
        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print(f'Congratulations! You guessed the number {attempts} attempts.')
            break
        
        if attempts == max_attempts - 1:
            hint = "You're getting close!" if abs(guess - number_to_guess) <= 10 else "You're quite far off!"
            print(hint)
        
    except ValueError:
        print('Please enter a valid number')

if attempts == max_attempts:
    print(f'Sorry, you\'ve used all your attempts. The number was {number_to_guess}.')
