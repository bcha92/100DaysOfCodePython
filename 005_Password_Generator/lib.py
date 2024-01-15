# Library Module for PyPassword Generator
lettersL = list("abcdefghijklmnopqrstuvwxyz")
lettersU = list("".join(lettersL).upper())
numbers = list("0123456789")
symbols = list("!@#$%^&*-_+=/?")

use = {
    "lower": True,
    "upper": True,
    "numbers": True,
    "symbols": False,
}