# this part was coded by Sky (Dylan) Boes
def encode(password):
  encoded_password = ""
  for digit in password:
    encoded_password += str(int(digit) + 3)[-1]
  return encoded_password

def decode(encoded_password):
  pass

# this part was coded by Sky (Dylan) Boes
if __name__ == '__main__':
  stored_password = ''
  while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    user_input = input("Please enter an option: ")
    if user_input == "1":
      stored_password = encode(input("Please enter your password to encode: "))
      print("Your password has been encoded and stored!\n")
    if user_input == "2":
      print(f'The encoded password is {stored_password}, and the original password is {decode(stored_password)}.\n')
    if user_input == "3":
      break
