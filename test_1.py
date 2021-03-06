def crypt():
    text = input('Enter text: ')
    values = int(input('Enter value: '))

    text = text.split()
    res = []
    n = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '

    
    for word in text:
        if not word in n:
            text_ords = [ord(i) for i in text]
            values_words = [j + values for j in text_ords]
            text_char = [chr(x) for x in values_words]
            text_res = ''.join(text)
            res.append(text_res)
        else:
            res.append(word)


            res = ''.join(res)
            print(res)
crypt()