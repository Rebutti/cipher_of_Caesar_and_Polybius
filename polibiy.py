alphabet = {
    'p': 'AA',
    'h': 'AB',
    'q': 'AC',
    'g': 'AD',
    'm': 'AE',
    'e': 'BA',
    'a': 'BB',
    'y': 'BC',
    'l': 'BD',
    'n': 'BE',
    'o': 'CA',
    'f': 'CB',
    'd': 'CC',
    'x': 'CD',
    'k': 'CE',
    'r': 'DA',
    'c': 'DB',
    'v': 'DC',
    's': 'DD',
    'z': 'DE',
    'w': 'EA',
    'b': 'EB',
    'u': 'EC',
    't': 'ED',
    'i': 'EE',

}
def polibiy_cipher(text):
    result = ''
    text = text.lower().replace('j', 'i')
    for i in text:
        result += alphabet[i.lower()]
        result += ' '
    return result

def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

def polibiy_decipher(text):
    result = ''
    text = text.split(' ')
    for i in text:
        result += get_key(alphabet, i)
    return result.upper()

if __name__ == "__main__":
    text = 'HABRAHABRJI'
    print(polibiy_cipher(text))
    text = 'AB BB EB DA BB AB BB EB DA EE EE'
    print(polibiy_decipher(text))