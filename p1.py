import os
from aes import aes
from des import des, triple_des

def getText(Kavya_201CS225_str_list, Kavya_201CS225_index):
    text = ""
    for i in Kavya_201CS225_str_list[Kavya_201CS225_index]:
        text += '{:0>8}'.format(bin(ord(i))[2:])
    return text
    
def main():
    Kavya_201CS225_plaintext_file = input('Enter name of file to be encrypted: ')
    Kavya_201CS225_ciphertext_file = input('Enter file to store the cryptogram: ')
    Kavya_201CS225_algorithm = int(input('Enter choice:\n1. DES\n2. Triple DES\n3. AES\n'))
    
    Kavya_201CS225_read_file = open(os.getcwd()+'/'+Kavya_201CS225_plaintext_file, 'r').read().split('\n')

    plaintext = Kavya_201CS225_read_file[0]
    #plaintext = getText(Kavya_201CS225_read_file, 0)

    ciphertext = ""
    if Kavya_201CS225_algorithm == 1:
        key = Kavya_201CS225_read_file[1]
        ciphertext = des(plaintext, key)
    elif Kavya_201CS225_algorithm == 2:
        key1 = getText(Kavya_201CS225_read_file, 1)
        key2 = getText(Kavya_201CS225_read_file, 2)
        ciphertext = triple_des(plaintext, key1, key2)
    elif Kavya_201CS225_algorithm == 3:
        key = getText(Kavya_201CS225_read_file, 1)
        ciphertext = aes(plaintext, key)
    else:
        print("Invalid input!")

    with open(Kavya_201CS225_ciphertext_file, 'w') as w:
        w.write(hex(int(ciphertext, 2)))

if __name__ == '__main__':
    main()
