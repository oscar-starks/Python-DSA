


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def encrypt(user_string, shift_amount):
    letters = ""
    for char in user_string:
        if char == " ":
            letters += " "

        elif (alphabet.index(char) + int(shift_amount)) <= (len(alphabet) - 1):
            letters += alphabet[alphabet.index(char) + int(shift_amount) ]
            
        elif (alphabet.index(char) + int(shift_amount)) > (len(alphabet) - 1):
            letters += alphabet[(len(alphabet) - 2) - alphabet.index(char) + int(shift_amount) ]
    print(f"Your encrypted text is {letters}")
    #return letters

def decrypt(user_string, shift_amount):
    letters = ""
    for char in user_string:
        if char == " ":
            letters += " "
        else:
            letters += alphabet[alphabet.index(char) - int(shift_amount) ]
    print(f"Your decrypted text is {letters}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

        
if direction == "encode":
    encrypt(text, shift)

elif direction == "decode":
    decrypt(text, shift)



