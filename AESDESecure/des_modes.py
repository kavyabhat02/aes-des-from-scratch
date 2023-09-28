# ECB, CBC, CFB, OFB, and CTR.
from des import des
import random

def xor(str1, str2):
    res = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            res += '0'
        else:
            res += '1'
    return res

def add_padding(plaintext):
    l = len(plaintext)
    if l%64 != 0:
        padding_len = (l//64 + 1) * 64 - l
        plaintext += ('0' * padding_len)
    return plaintext

def ecb(plaintext, key):
    add_padding(plaintext)
    i = 0
    ciphertext = ""
    while i < len(plaintext):
        ciphertext += des(plaintext[i: i+64], key)
        i += 64

    return ciphertext

def cbc(plaintext, key):

    add_padding(plaintext)
    
    # Create initialization vector, should actually be random
    # For simplicity, using key[30:64] + key[:30]
    iv = key[30:64] + key[:30]

    i = 0
    ciphertext = ""
    while i < len(plaintext):
        shuffle = ""
        if i == 0:
            shuffle = xor(plaintext[i: i+64], iv)
        else:
            shuffle = xor(plaintext[i: i+64], ciphertext[i-64: i])
        ciphertext += des(shuffle, key)
        i += 64

    return ciphertext

def cfb(plaintext, key):
    add_padding(plaintext)

    # Create initialization vector, should actually be random
    # For simplicity, using key[30:64] + key[:30]
    iv = key[30:64] + key[:30]

    # s = 8
    s = 8
    i = 0
    ciphertext = ""
    while i < len(plaintext):
        iv = des(iv, key)

        # select left s bits
        to_xor = iv[:s]
        iv = iv[s:] + xor(plaintext[i: i+s], to_xor)
        ciphertext += xor(plaintext[i: i+s], to_xor)
        i += s

    return ciphertext

def ofb(plaintext, key):
    add_padding(plaintext)

    # Create initialization vector, should actually be random
    # For simplicity, using key[30:64] + key[:30]
    iv = key[30:64] + key[:30]

    i = 0
    ciphertext = ""
    while i < len(plaintext):
        iv = des(iv, key)
        ciphertext += xor(plaintext[i: i+64], iv)
        i += 64

    return ciphertext

def ctr(plaintext, key):
    add_padding(plaintext)

    i = 0
    ciphertext = ""

    while i < len(plaintext):
        ctr = '{:0>64}'.format(bin(i)[2:])
        ctr = des(ctr, key)
        ciphertext += xor(plaintext[i: i+64], ctr)
        i += 64

    return ciphertext

def des_modes(plaintext, key):
    print("Enter option:\n1. ECB\n2. CBC\n3. CFB\n4. OFB\n5. CTR\n")
    choice = int(input())

    if choice == 1:
        return ecb(plaintext, key)
    elif choice == 2:
        return cbc(plaintext, key)
    elif choice == 3:
        return cfb(plaintext, key)
    elif choice == 4:
        return ofb(plaintext, key)
    elif choice == 5:
        return ctr(plaintext, key)

