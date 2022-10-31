from myerrors import MyError
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"



def cezar_cipher(text, size, decipher=False):
    try:
        size = int(size)
        if size < 1 or size > 25:
            raise MyError
    except ValueError: 
        return ValueError
    except MyError:
        return MyError
    text = text.upper()
    if decipher:
        size *= (-1)
    result = ''
    for i in text:
        place = alphabet.find(i)
        new_letter = place + size
        if i in alphabet:
            result += alphabet[new_letter]
        else:
            result += i
    return result
    


if __name__ == "__main__":
    text = 'CIPHER'
    size = 3
    # print(cezar_cipher(text, 'size'))
    a = cezar_cipher(text, 26)
    if a == MyError:
        print('error')
    text = 'ABC'
    print(cezar_cipher(text, 1, decipher=True))