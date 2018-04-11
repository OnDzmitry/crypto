start = ord('a')
end = ord('z') + 1
ALPHA = "".join(map(chr, range(start, end)))

def encode(text, step):
    text = text.lower()
    trans = str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step])
    return text.translate(trans)
 
def decode(text, step):
    text = text.lower()
    trans = str.maketrans(ALPHA[step:] + ALPHA[:step], ALPHA)
    return text.translate(trans)
