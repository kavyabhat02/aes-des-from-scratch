from .aes import aes
from .des import des, triple_des
# from .aes_modes import aes_modes
# from .des_modes import des_modes

def bin2text(s): 
    return "".join([chr(int(s[i:i+16],2)) for i in range(0,len(s),16)])

def testPatternPreservation(plaintext, pattern, ciphertext):
    count_plaintext = plaintext.count(pattern)
    count_ciphertext = ciphertext.count(pattern)

    print(f"{pattern} occurs {count_plaintext} times in {plaintext}")
    print(f"{pattern} occurs {count_ciphertext} times in {ciphertext}")

def testErrorPropagation(plaintext):
    index = int(input(('Enter bit position: ')))
    new_text = plaintext[0: index] + chr(48 + 1 - (ord(plaintext[index]) - 48)) + plaintext[index+1:]
    return new_text