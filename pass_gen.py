import secrets
import string

def generate_password(length):

  all_chars = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(secrets.choice(all_chars) for i in range(length))
  return password

def main():
  
  while True:
    try:
      num_passwords = int(input("Enter the number of passwords you need: "))
      password_length = int(input("Enter the desired password length (minimum 8 characters): "))
      if password_length < 8:
        print("Password length should be at least 8 characters. Please try again.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter integers for number of passwords and length.")

  print("\nYour generated passwords:")
  for _ in range(num_passwords):
    password = generate_password(password_length)
    print(password)

if __name__ == "__main__":
  main()
