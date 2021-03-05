from colorama import *
init()
# logo
def logo():
    print(f"""{Fore.GREEN}
        ████████╗███████╗██╗░░██╗████████╗███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
        ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
        ░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░█████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
        ░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
        ░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
        ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░
        """)
    print("""
        1.Encrypt
        2.Decrypt
        """)
# logo output
logo()

def values():
    global stri, offset
    stri = input("Enter text: ")
    offset = int(input("Enter offset: "))


def caesar_eng(offset, stri):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    ln = len(alphabet)
    n = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '
    for i in stri:
        if not i in n:
            res.append(alphabet[(alphabet.find(i) + offset) % ln])
        else:
            res.append(i)
    print(''.join(res))

def decrypt_caesar(stri, offset):
    # creat a list of encrypted words.
    stri = stri.split()
    # creat a list to hold decrypted words.
    res = []

    for word in stri:
        cipher_ords = [ord(x) for x in stri]
        text = [cipher_ords - c for c in offset]
        text_chars = [chr(i) for i in text]
        li = ''.join(text_chars)
        res.append(li)

    res = ''.join(res)
    print(res)

namber = input('Enter namber: ')

if namber == 1:
    values()
    print(caesar_eng(offset, stri))
elif namber == 2:
    values()
    print(decrypt_caesar(offset, stri))









