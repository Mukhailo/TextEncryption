offset = int(input('Offset '))
    str = input('String ')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    ln = len(alphabet)
    n = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '
    for l in str:
        if not l in n:
            res.append(alphabet[(alphabet.find(l)+offset)%ln])
        else:
            res.append(l)
    print(''.join(res))