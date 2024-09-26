import random

roll_count = 0  # Initialize roll count

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        num_dice = int(input('How many dice do you want to roll? '))
        rolls = [random.randint(1, 6) for _ in range(num_dice)]
        roll_count += 1  # Increment the roll count
        print(f'Roll results: {rolls}')
        print(f'Total rolls this session: {roll_count}')
    elif choice == 'n':
        print('Thanks for playing!')
        print(f'You rolled the dice a total of {roll_count} times.')
        break
    else:
        print('Invalid choice!')
