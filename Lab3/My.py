import operator

start = ord('a')
end = ord('z') + 1
ALPHA = "".join(map(chr, range(start, end)))

def encode(text, key):
    trans = str.maketrans(ALPHA, convert(ALPHA, key))
    return text.translate(trans)

def decode(text, key):
    trans = str.maketrans(convert(ALPHA, key), ALPHA)
    return text.translate(trans)


def convert(alph, key):
    length = len(alph)
    temp_dict = {}
    output = ''

    for i, j in enumerate(alph):
        temp_dict[j] = int((i**3*key+length*key+i*(length*(i**4)-key))%1000)
    temp_dict = sorted(temp_dict.items(), key=operator.itemgetter(1))
    for i in temp_dict:
        output += i[0]
    
    return output
