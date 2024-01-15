# Caesar Cipher
from lib import alpha, logo, set_value, caesar_cipher, welcome_message

welcome_message()
protocol = set_value("Would you like to 'Encode' (E) or 'Decode' (D) a phrase? ", str, ["e", "encode", "decode", "d"])
message = set_value("Type your message: ", str, [])
shift = set_value("Type the shift number: ", int, [])

# Shall we add numbers to the mix?
addNums = set_value("Would you like to add numbers to the cipher mix? (Yes/No) ", str, ["y", "n", "yes", "no"])
if addNums == 'y' or addNums == 'yes': alpha.extend(list("0123456789"))

if protocol == 'e': protocol = "encode"
elif protocol == 'd': protocol = "decode"
print(caesar_cipher(protocol, message, shift))
