stri = input('Enter text: ')
offset = input('Enter values: ')
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