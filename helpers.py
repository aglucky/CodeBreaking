from collections import Counter
import string

def prettyPrint(text, columns=10):
    for i, let in enumerate(text.split(' ')):
        if i % columns == 0:
            print()
        print(let, end=" ")
        
def keywordReplace(keyword):
    mapping = {}
    curLet = 'a'
    for let in keyword:
        upper = let.upper()
        if upper not in mapping:
            mapping[upper] = curLet
            curLet = chr(ord(curLet) + 1)
    
    endLet = 'A'
    for i in range(26):
        if endLet not in mapping:
            mapping[endLet] = curLet
            curLet = chr(ord(curLet) + 1)
        endLet = chr(ord(endLet) + 1)
        
    return mapping

def replaceLetter(letter, mappings, hide=False):
    if letter not in mappings:
        return letter if (not hide or letter in set([' ', ' \n'])) else '_'
    return mappings[letter]

def getSequences(text, seqLen=3, minFreq=1):
    rawCipher = text.replace(" ", "")
    repeats = []
    seqLen=seqLen-1

    for i in range(len(rawCipher) - seqLen):
        repeats.append(rawCipher[i:i+seqLen+1])

    freq = Counter(repeats)
    return {k: count for k, count in freq.items() if count > minFreq}

def getConsecutive(text,minFreq=1):
    rawCipher = text.replace(" ", "")
    repeats=[]
    for doubleLen in range(2,6):
        for i in range(len(rawCipher) - doubleLen):
            if all([rawCipher[i] == rawCipher[i+j] for j in range(1, doubleLen)]):
                repeats.append(rawCipher[i:i+doubleLen])
    freq = Counter(repeats)
    return {k: count for k, count in freq.items() if count > minFreq}


def decrypt(text, mapping, hide=False):
    return "".join(list(map(lambda x: replaceLetter(x, mapping, hide=hide), text)))

class Mapping:
    def __init__(self, mapping={}):
        self.map = mapping
        
    def addLetter(self, cipherLetter, letter):
        self.map[cipherLetter.upper()] = letter.lower()
    
    def addWord(self, cipherWord, word):
        for cipherLetter, letter in zip(cipherWord, word):
            self.addLetter(cipherLetter, letter)
    
    def getRemaining(self):
        return set(string.ascii_lowercase) - set(self.map.values())
        
    def getKey(self):
        return sorted(self.map.items(), key=lambda x: x[1])
    
    def decrypt(self, text, hide=False, pretty=True):
        if pretty:
            prettyPrint(decrypt(text, self.map, hide=hide))
        return decrypt(text, self.map, hide=hide)