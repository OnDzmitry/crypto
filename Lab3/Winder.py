start = ord('a')
end = ord('z') + 1
ALPHA = "".join(map(chr, range(start, end)))

def encode(text, key):
    key *= len(text) // len(key) + 1
    return ''.join([chr(((ord(j) + ALPHA.find(key[i])) - start) % (end - start) + start) for i, j in enumerate(text)])

def decode(text, key):
    key *= len(text) // len(key) + 1
    return ''.join([chr(((ord(j) - ALPHA.find(key[i])) - start) % (end - start) + start) for i, j in enumerate(text)])
