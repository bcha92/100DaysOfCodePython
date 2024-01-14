# Library assets for Caesar Cipher, including Functions
alpha = list("abcdefghijklmnopqrstuvwxyz")

logo = '''
**************************************************
  ___     ___     ____    ____     ___     ____
 / __\   / _ \   |  __|  / ___\   / _ \   |  _ \\
| |     / |_| \  | |_    \ \__   / |_| \  | |_| |
| |    |   _   | |  _|    \__ \ |   _   | |  _  |
| |__  |  | |  | | |__    __/ / |  | |  | | | \ \\
 \___/ |__| |__| |____|  \___/  |__| |__| |_|  \_\\
***************************************************
'''

def welcome_message():
    print(logo, "\nWelcome to the Python Caesar Cipher!\n")

def set_value(prompt: str, val: type, escape_words: list):
    response = ""
    while response == "" or type(response) is not val:
        try:
            response = val(input(prompt))
            if val == str and len(escape_words) > 0 and response.lower() not in escape_words:
                print("Error! Please enter a valid prompt:", ", ".join(escape_words))
                response = ""
            elif val == str and len(escape_words) > 0 and response.lower() in escape_words: return response.lower()
            elif val == str and len(response) > 0: return response
            elif val == int: return response
            else:
                print("Error! Please enter a response!")
                response = ""
        except ValueError or UnboundLocalError: print(f"Invalid response type of integer.")

def caesar_cipher(protocol: str, text: str, shift_amount):
    output_text = ""
    for char in text:
        try:
            if protocol == "encode": new_position = alpha.index(char.lower()) + shift_amount
            elif protocol == "decode": new_position =  alpha.index(char.lower()) - shift_amount
            else: new_position = alpha.index(char.lower())
            
            if new_position < 0: new_position = new_position % len(alpha)
            else: new_position = new_position % len(alpha)
            
            if char.isupper(): output_text += alpha[new_position].upper()
            else: output_text += alpha[new_position]
        except ValueError: output_text += char
    print(new_position)
    return output_text