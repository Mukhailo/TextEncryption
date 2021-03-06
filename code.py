from colorama import *
init()

def what1():
    print(f"""{Fore.CYAN}
        1.Encrypt
        2.Decrypt
        """)

def what2():
    print(f"""{Fore.CYAN}
        1.Caesar
        2.Gronsfeld
    """)

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

def values():
    global offset, stri
    stri = (input('Enter text: '))
    offset = int(input('Enter value: '))

def Caesar_encrypt(offset, stri):
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

def Caesar_decrypt(offset, stri):
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

def Gronsfeld_encrypt(stri, offset):
    # creat a list of encrypted words.
    stri = stri.split()
    # creat a list to hold decrypted words.
    res = []
    for word in stri:
        cipher_ords = [ord(x) for x in word]
        for r in offset:
            c = int(r)
        plaintext_ords = [o - c for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        res.append(plaintext)
    # join each word in the sentence list back together by a space.
    sentence = ' '.join(res)
    print(sentence)

def Gronsfeld_decrypt(stri, offset):
    # creat a list of encrypted words.
    stri = stri.split()
    # creat a list to hold decrypted words.
    res = []

    for word in stri:
        cipher_ords = [ord(x) for x in word]
        for r in offset:
            c = int(r)
            plaintext_ords = [o - c for o in cipher_ords]
    plaintext_chars = [chr(i) for i in plaintext_ords]
    plaintext = ''.join(plaintext_chars)
    res.append(plaintext)
    # join each word in the sentence list back together by a space.
    sentence = ' '.join(res)
    print(sentence)

def text_encrypt():
    logo()
    what2()
    namber = int(input('Enter namber: '))
    if namber == 1:
        values()
        Caesar_encrypt(offset,stri)
    elif namber == 2:
        values()
        Gronsfeld_encrypt(offset,stri)

def text_decrypt():
    logo()
    what2()
    namber = int(input('Enter namber: '))
    if namber == 1:
        values()
        Caesar_decrypt(offset,stri)
    elif namber == 2:
        values()
        Gronsfeld_decrypt(offset,stri)

logo()
what1()
namber = int(input('Enter namber: '))

if namber == 1:
    text_encrypt()
elif namber == 2:
    text_decrypt()



