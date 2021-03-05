from colorama import *
init()

def logo():
    print(f"""{Fore.GREEN}
        ████████╗███████╗██╗░░██╗████████╗███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
        ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
        ░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░█████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
        ░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
        ░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
        ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░
        """)

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


if __name__ == "__main__":
    logo()
    offset = int(input("Enter offset: "))
    stri = input("Enter text: ")