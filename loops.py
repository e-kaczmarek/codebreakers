word = 'cryptography'

def letters(word):
    for c in word:
        print(c)
def backwards(word):
    ret = ''
    for c in word:
        ret = c+ret
    print( ret)
def secret(word):
    ret = ''
    for c in word:
        ret += 'x'
    return ret
