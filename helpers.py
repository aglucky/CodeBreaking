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
