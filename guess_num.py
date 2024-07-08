import random

def get_guess():
  
  while True:
    try:
      guess = int(input("Guess a number between 1 and 100: "))
      if 1 <= guess <= 100:
        return guess
      else:
        print("Please enter a number between 1 and 100.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def give_hint(guess, secret_number):
  
  
  hint_distance = guess - secret_number
  if hint_distance<0:
        if hint_distance <= -5:
            return "higher ! You're very close."
        elif hint_distance <= -10:
            return "higher ! Getting closer."
        elif hint_distance <= -15:
            return "higher ! Keep guessing."
        elif hint_distance <= -20:
            return "higher ! You're on the right track."
        else:
            return "Try a higher number."
  else:
        if hint_distance <= -5:
            return "lower ! You're very close."
        elif hint_distance <= -10:
            return "lower ! Getting closer."
        elif hint_distance <= -15:
            return "lower ! Keep guessing."
        elif hint_distance <= -20:
            return "lower ! You're on the right track."
        else:
            return "Try a lower number."
        


def play_game():
  
  secret_number = random.randint(1, 100)
  guesses = 0

  print("Welcome to the Number Guessing Game!")

  while True:
    guess = get_guess()
    guesses += 1

    if guess == secret_number:
      print(f"Congratulations! You guessed the number in {guesses} attempts.")
      break
    else:
      print(give_hint(guess, secret_number))

if __name__ == "__main__":
  play_game()
