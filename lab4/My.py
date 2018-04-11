# encode block
def encode(text, step):
    text = list(text)
    output = ''
    index = 0
    step -= 1
    
    while text:
        L = len(text)
        for _ in range(step):
            if L == 1:
                index = 0
                break
            elif index in [L-1, L]:
                index = index-L+1
            else:
                index += 1
        
        output += text[index]
        del text[index]
    
    return output


# decode block
def decode(text, step):
    text = list(text)
    output = [None for _ in range(len(text))]
    index = -1
    while text:
        for _ in range(step):
            index = __getNextDecodeIndex(index, output)

        output[index] = text[0]
        del text[0]

    return ''.join(output)

def __getNextDecodeIndex(index, output):
    while True:
        if index == len(output)-1:
            index = 0
        else:
            index += 1
        
        if not output[index]:
            break

    return index
