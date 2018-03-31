import string

def alphabet_position(letter):
    if (letter.isupper()):
        return string.ascii_uppercase.index(letter)
    else:
        return string.ascii_lowercase.index(letter)

def rotate_character(char, rot):
    if (char.isupper()):
        return string.ascii_uppercase[(alphabet_position(char) + rot) % 26]
    else:
        return string.ascii_lowercase[(alphabet_position(char) + rot) % 26]