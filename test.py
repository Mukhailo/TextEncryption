def decrypt():
    ciphertext = input('Please enter your Encrypted sentence here: ')
    shift = int(input('Please enter its shift value: '))
    space = []

    # creat a list of encrypted words.
    ciphertext = ciphertext.split()

    # creat a list to hold decrypted words.
    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o + shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)

    # join each word in the sentence list back together by a space.
    sentence = ' '.join(sentence)
    print('Your encrypted sentence is:', sentence)

decrypt()