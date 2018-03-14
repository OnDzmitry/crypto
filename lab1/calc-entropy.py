import math
import string


def get_alphabet(source):
    symbols = {}
    for symbol in source:
        symbols[symbol] = {'count': 0, 'frequency': 0}
    return symbols


def delete_punctuation(source):
    for punc in string.punctuation:
        source = source.replace(punc, "")
    return source


def delete_digits(source):
    for digit in string.digits:
        source = source.replace(digit, "")
    return source


def char_range(c1, c2):
    symbols = {}
    for symbol in range(ord(c1), ord(c2) + 1):
        symbols[chr(symbol)] = {'count': 0, 'frequency': 0}
    return symbols


source_text = open("files/source.txt", "r").read()
# source_text = open("files/initials.txt", "r").read()
source_alphabet = open("files/alphabet.txt", "r").read()

source_text = delete_punctuation(source_text)
source_text = delete_digits(source_text)

alphabet = get_alphabet(source_alphabet.split('\n'))
# alphabet = char_range('A', 'Z')
text_len = (len(source_text) - source_text.count(' ') - source_text.count('\n'))

for symbol in list(source_text):
    upper_symbol = symbol.upper()
    if upper_symbol in alphabet.keys():
        alphabet[upper_symbol]['count'] += 1
        alphabet[upper_symbol]['frequency'] = alphabet[upper_symbol]['count'] / text_len
    else:
        if upper_symbol != ' ':
            print(upper_symbol)

entropy = 0
for symbol in alphabet:
    frequency = alphabet[symbol]['frequency']
    if frequency != 0:
        entropy += frequency * math.log(frequency, 2)

summ = 0
for symbol in alphabet:
    summ += alphabet[symbol]['frequency']
    print(symbol + ' count=' + str(alphabet[symbol]['count']) + ' frequency=' + str(alphabet[symbol]['frequency']))

print(summ)
print('Shennon: ' + str(-entropy))
print('Hartli: ' + str(math.log(len(alphabet) ** text_len, 2)))
