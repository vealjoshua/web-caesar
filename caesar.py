from helpers import rotate_character

def encrypt(message, rotation):
    encryption = ""
    for char in message:
        if(char.isalpha()):
            encryption += rotate_character(char, int(rotation))
        else:
            encryption += char
    return encryption

def main():
    from sys import argv, exit
    if(len(argv) == 2):
        rotation = argv[1]
        if (rotation.isdigit() == False):
            print("usage: python caesar.py n")
            exit()
        message = input('Type a message:\n')
        print(encrypt(message, rotation))
    elif(len(argv) == 1):
        message = input('Type a message:\n')
        rotation = input('Rotate by:\n')
        if (rotation.isdigit() == False):
            print("usage: python caesar.py n")
            exit()
        print(encrypt(message, rotation))
    else:
        print("usage: python caesar.py n")
        exit()
    
if __name__ == '__main__':
    main()
