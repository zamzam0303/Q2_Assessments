secret_number = 17
valid_attempts = 0
max_attempts = 5

while valid_attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    # Condition: If the player enters a negative number, ignore it without deducting an attempt
    if guess < 0:
        continue

    # A valid attempt has been made
    valid_attempts += 1

    # Condition: If the player guesses correctly, immediately terminate the loop
    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break
else:
    # Condition: If the player uses all five valid attempts, display "Game Over!"
    print("Game Over!")
