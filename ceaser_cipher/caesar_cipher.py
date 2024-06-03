#Importing logo and printing it out in the program
from art import logo
print(logo)
#Welcome message
print("Welcome to the Caeser Cipher Program")

#alphabets to be ciphered
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    print('DECRIPTION MODE SELECTED')
    shift_amount *= -1
  else:
    print('ENCRIPTION MODE SELECTED')
   #using modulus to check when user enters shift number greater than the total number of alphabets
  if shift_amount >=26:
    shift_amount = shift %26
  for letter in start_text:
    if letter in alphabet:
       position = alphabet.index(letter)
       new_position = position + shift_amount
       end_text += alphabet[new_position]
#maintaining a character to be encripted or decripted when it is a symbol/space or number without encripting it
    else:
       end_text += letter
  print(f"Here's the {cipher_direction}d result: {end_text}")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#calling function
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# Restarting the program for the user to continually decrypt until he no longer wants to
while True:
      user = input('Do you want to restart the program: yes or no\n').capitalize()
      if user == 'Yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
      else:
        print('Goodbye Champ')
        break


 

