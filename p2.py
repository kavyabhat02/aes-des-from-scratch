import os
from des_modes import des_modes
from aes_modes import aes_modes

def bin2text(s): 
    return "".join([chr(int(s[i:i+16],2)) for i in range(0,len(s),16)])

def getText(Kavya_201CS225_str_list, Kavya_201CS225_index):
    text = ""
    for i in Kavya_201CS225_str_list[Kavya_201CS225_index]:
        text += '{:0>8}'.format(bin(ord(i))[2:])
    return text

def testPatternPreservation(Kavya_201CS225_plaintext, Kavya_201CS225_pattern, Kavya_201CS225_ciphertext):
    count_plaintext = Kavya_201CS225_plaintext.count(Kavya_201CS225_pattern)
    count_ciphertext = Kavya_201CS225_ciphertext.count(Kavya_201CS225_pattern)

    print(f"{Kavya_201CS225_pattern} occurs {count_plaintext} times in {Kavya_201CS225_plaintext}")
    print(f"{Kavya_201CS225_pattern} occurs {count_ciphertext} times in {Kavya_201CS225_ciphertext}")

def testErrorPropagation(Kavya_201CS225_plaintext):
    index = int(input(('Enter bit position: ')))
    new_text = Kavya_201CS225_plaintext[0: index] + chr(48 + 1 - (ord(Kavya_201CS225_plaintext[index]) - 48)) + Kavya_201CS225_plaintext[index+1:]
    return new_text

def main():
    Kavya_201CS225_plaintext_file = input('Enter name of file to be encrypted: ')
    Kavya_201CS225_ciphertext_file = input('Enter file to store the cryptogram: ')
    choice = int(input('Enter choice:\n1. DES\n2. AES\n'))

    Kavya_201CS225_read_file = open(os.getcwd()+'/'+Kavya_201CS225_plaintext_file, 'r').read().split('\n')
    Kavya_201CS225_plaintext = getText(Kavya_201CS225_read_file, 0)
    Kavya_201CS225_key = getText(Kavya_201CS225_read_file, 1)

    ciphertext = ""

    Kavya_201CS225_error_cipher = ""
    Kavya_201CS225_error_plain = ""
    errorProp = input("Test error propagation? (y/n): ")
    if errorProp == "y":
        Kavya_201CS225_error_plain = testErrorPropagation(Kavya_201CS225_plaintext)
        
    if choice == 1:
        ciphertext = des_modes(Kavya_201CS225_plaintext, Kavya_201CS225_key)
        if errorProp == "y":
            error_cipher = des_modes(Kavya_201CS225_error_plain, Kavya_201CS225_key)

    elif choice == 2:
        ciphertext = aes_modes(Kavya_201CS225_plaintext, Kavya_201CS225_key)
        if errorProp == "y":
            error_cipher = aes_modes(Kavya_201CS225_error_plain, Kavya_201CS225_key)

    else:
        print("Invalid option!")

    ascii_ciphertext = bin2text(ciphertext)
    ascii_err_ciphertext = bin2text(error_cipher)
    
    patternPres = input("Test pattern preservation? (y/n): ")
    if patternPres == "y":
        pattern = input('Enter pattern: ')
        testPatternPreservation(Kavya_201CS225_plaintext, pattern, ciphertext)

    with open(Kavya_201CS225_ciphertext_file, 'w') as w:
        w.write(hex(int(ciphertext, 2)))
        w.write("\n")
        w.write(ascii_ciphertext)
        w.write("\n")

        if(errorProp == "y"):
            w.write(hex(int(error_cipher, 2)))
            w.write("\n")
            w.write(ascii_err_ciphertext)

if __name__ == '__main__':
    main()