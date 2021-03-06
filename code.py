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

namber = int(input('Enter namber: '))

def values():
    global offset, stri
    stri = (input('Enter text: '))
    offset = int(input('Enter value: '))



def encrypt(offset, stri):
# creat a list of encrypted words.
    stri = stri.split()

    # creat a list to hold decrypted words.
    res = []
    for word in stri:   
            cipher_ords = [ord(x) for x in word]
            plaintext_ords = [o + offset for o in cipher_ords]
            plaintext_chars = [chr(i) for i in plaintext_ords]
            plaintext = ''.join(plaintext_chars)
            res.append(plaintext)
    # join each word in the sentence list back together by a space.
    sentence = ' '.join(res)
    print(sentence)


def decrypt(offset, stri):
# creat a list of encrypted words.
    stri = stri.split()
    # creat a list to hold decrypted words.
    res = []
    for word in stri:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - offset for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        res.append(plaintext)
    # join each word in the sentence list back together by a space.
    sentence = ' '.join(res)
    print(sentence)
# Choise encrypt or decrypt
if namber == 1:
    values()
    encrypt(offset,stri)
elif namber == 2:
    values()
    decrypt(offset, stri)



