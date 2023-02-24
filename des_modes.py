# ECB, CBC, CFB, OFB, and CTR.
from des import des
import random

def xor(Kavya_201CS225_str1, Kavya_201CS225_str2):
    Kavya_201CS225_res = ""
    for i in range(len(Kavya_201CS225_str1)):
        if Kavya_201CS225_str1[i] == Kavya_201CS225_str2[i]:
            Kavya_201CS225_res += '0'
        else:
            Kavya_201CS225_res += '1'
    return Kavya_201CS225_res

def add_padding(Kavya_201CS225_plaintext):
    l = len(Kavya_201CS225_plaintext)
    if l%64 != 0:
        padding_len = (l//64 + 1) * 64 - l
        Kavya_201CS225_plaintext += ('0' * padding_len)
    return Kavya_201CS225_plaintext

def ecb(Kavya_201CS225_plaintext, Kavya_201CS225_key):
    add_padding(Kavya_201CS225_plaintext)
    i = 0
    ciphertext = ""
    while i < len(Kavya_201CS225_plaintext):
        ciphertext += des(Kavya_201CS225_plaintext[i: i+64], Kavya_201CS225_key)
        i += 64

    return ciphertext

def cbc(Kavya_201CS225_plaintext, Kavya_201CS225_key):

    add_padding(Kavya_201CS225_plaintext)
    
    # Create initialization vector, should actually be random
    # For simplicity, using key[30:64] + key[:30]
    iv = Kavya_201CS225_key[30:64] + Kavya_201CS225_key[:30]

    i = 0
    ciphertext = ""
    while i < len(Kavya_201CS225_plaintext):
        shuffle = ""
        if i == 0:
            shuffle = xor(Kavya_201CS225_plaintext[i: i+64], iv)
        else:
            shuffle = xor(Kavya_201CS225_plaintext[i: i+64], ciphertext[i-64: i])
        ciphertext += des(shuffle, Kavya_201CS225_key)
        i += 64

    return ciphertext

def cfb(Kavya_201CS225_plaintext, Kavya_201CS225_key):
    add_padding(Kavya_201CS225_plaintext)

    # Create initialization vector, should actually be random
    # For simplicity, using key[30:64] + key[:30]
    iv = Kavya_201CS225_key[30:64] + Kavya_201CS225_key[:30]

    # s = 8
    s = 8
    i = 0
    ciphertext = ""
    while i < len(Kavya_201CS225_plaintext):
        iv = des(iv, Kavya_201CS225_key)

        # select left s bits
        to_xor = iv[:s]
        iv = iv[s:] + xor(Kavya_201CS225_plaintext[i: i+s], to_xor)
        ciphertext += xor(Kavya_201CS225_plaintext[i: i+s], to_xor)
        i += s

    return ciphertext

def ofb(Kavya_201CS225_plaintext, Kavya_201CS225_key):
    add_padding(Kavya_201CS225_plaintext)

    # Create initialization vector, should actually be random
    # For simplicity, using key[30:64] + key[:30]
    iv = Kavya_201CS225_key[30:64] + Kavya_201CS225_key[:30]

    i = 0
    ciphertext = ""
    while i < len(Kavya_201CS225_plaintext):
        iv = des(iv, Kavya_201CS225_key)
        ciphertext += xor(Kavya_201CS225_plaintext[i: i+64], iv)
        i += 64

    return ciphertext

def ctr(Kavya_201CS225_plaintext, Kavya_201CS225_key):
    add_padding(Kavya_201CS225_plaintext)

    i = 0
    ciphertext = ""

    while i < len(Kavya_201CS225_plaintext):
        ctr = '{:0>64}'.format(bin(i)[2:])
        ctr = des(ctr, Kavya_201CS225_key)
        ciphertext += xor(Kavya_201CS225_plaintext[i: i+64], ctr)
        i += 64

    return ciphertext

def des_modes(Kavya_201CS225_plaintext, Kavya_201CS225_key):
    print("Enter option:\n1. ECB\n2. CBC\n3. CFB\n4. OFB\n5. CTR\n")
    choice = int(input())

    if choice == 1:
        return ecb(Kavya_201CS225_plaintext, Kavya_201CS225_key)
    elif choice == 2:
        return cbc(Kavya_201CS225_plaintext, Kavya_201CS225_key)
    elif choice == 3:
        return cfb(Kavya_201CS225_plaintext, Kavya_201CS225_key)
    elif choice == 4:
        return ofb(Kavya_201CS225_plaintext, Kavya_201CS225_key)
    elif choice == 5:
        return ctr(Kavya_201CS225_plaintext, Kavya_201CS225_key)

