import os 

def permute(table, text, n):
    new_text = ""
    for i in range(n):
        new_text += text[table[i] - 1]
    return new_text

def shift_key(key, shift):
    new_key = key[shift:] + key[0:shift]
    return new_key

def xor(str1, str2):
    res = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            res += '0'
        else:
            res += '1'
    return res

def des_encrypt(plaintext, round_keys):
    initial_perm_table = [ 58, 50, 42, 34, 26, 18, 10, 2,  60, 52, 44,
                           36, 28, 20, 12, 4,  62, 54, 46, 38, 30, 22,
                           14, 6,  64, 56, 48, 40, 32, 24, 16, 8,  57,
                           49, 41, 33, 25, 17, 9,  1,  59, 51, 43, 35,
                           27, 19, 11, 3,  61, 53, 45, 37, 29, 21, 13,
                           5,  63, 55, 47, 39, 31, 23, 15, 7 ]

    # Perform Initial Permutation
    plaintext = permute(initial_perm_table, plaintext, 64)
    # print(f"Plaintext after permutation: {hex(int(plaintext, 2))}")

    left_pt = plaintext[0:32]
    right_pt = plaintext[32:]

    # Expansion of right_pt to 48 bits - D Box
    exp_d = [ 32, 1,  2,  3,  4,  5,  4,  5,  6,  7,  8,  9,
              8,  9,  10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
              16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 
              24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1 ]

    s_box = [
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]], 

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], 
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]], 
        
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]], 
        
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], 
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9,  8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]], 
        
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]], 
        
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], 
         [13, 0, 11, 7, 4,  9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]], 
        
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    # Straight Permutation table
    per = [ 16, 7, 20, 21, 29, 12, 28, 17, 
            1, 15, 23, 26, 5, 18, 31, 10, 
            2,  8,  24, 14, 32, 27, 3, 9, 
            19, 13, 30, 6, 22, 11, 4, 25 ]

    for round in range(16):
        right_exp = permute(exp_d, right_pt, 48)
        x = xor(right_exp, round_keys[round])

        # Use S-boxes
        output = ""
        i = 0
        while i < 48:
            map_val = {'1': 1, '0': 0}
            row = map_val[x[i]] * 2 + map_val[x[i+5]]
            col = map_val[x[i+1]]*8 + map_val[x[i+2]]*4 + map_val[x[i+3]]*2 + map_val[x[i+4]]
            val = s_box[i//6][row][col]

            output += chr(val // 8 + 48)
            val %= 8
            output += chr(val // 4 + 48)
            val %= 4
            output += chr(val // 2 + 48)
            val %= 2
            output += chr(val + 48)

            i += 6

        output = permute(per, output, 32)
        x = xor(left_pt, output)

        left_pt = x
        if round != 15:
            temp = left_pt
            left_pt = right_pt
            right_pt = temp

    combined = left_pt + right_pt
    final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32, 
                   39, 7, 47, 15, 55, 23, 63, 31, 
                   38, 6, 46, 14, 54, 22, 62, 30, 
                   37, 5, 45, 13, 53, 21, 61, 29, 
                   36, 4, 44, 12, 52, 20, 60, 28, 
                   35, 3, 43, 11, 51, 19, 59, 27, 
                   34, 2, 42, 10, 50, 18, 58, 26, 
                   33, 1, 41, 9, 49, 17, 57, 25 ]

    cipher = permute(final_perm, combined, 64)
    return cipher

def des_key_encryption(key):
    # Convert 64 bit key to 56 bit
    key_reduction = [ 57, 49, 41, 33, 25, 17, 9,  1,  58, 50, 42, 34,
                      26, 18, 10, 2,  59, 51, 43, 35, 27, 19, 11, 3,
                      60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7,
                      62, 54, 46, 38, 30, 22, 14, 6,  61, 53, 45, 37,
                      29, 21, 13, 5,  28, 20, 12, 4 ]

    key_comp = [ 14, 17, 11, 24, 1,  5,  3,  28,
                 15, 6,  21, 10, 23, 19, 12, 4,
                 26, 8,  16, 7,  27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55, 30, 40,
                 51, 45, 33, 48, 44, 49, 39, 56,
                 34, 53, 46, 42, 50, 36, 29, 32 ]  

    key = permute(key_reduction, key, 56)
    left_key = key[:28]
    right_key = key[28:]

    shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    round_keys = []
    for round in range(16):
        shift = shift_table[round]
        
        # Perform left shift on both halves of the key
        left_key = shift_key(left_key, shift)
        right_key = shift_key(right_key, shift)

        combined_key = left_key + right_key       # combine after shift

        # Compress the 56 bit key to 48 bits
        round_keys.append(permute(key_comp, combined_key, 48))

    return round_keys

def des(plaintext, key):
    round_keys = des_key_encryption(key)

    for i in round_keys:
        print(hex(int(i, 2)))
    ciphertext = des_encrypt(plaintext, round_keys)
    return ciphertext


def triple_des(plaintext, key1, key2):
    round_keys1 = des_key_encryption(key1)
    round_keys2 = des_key_encryption(key2)

    cipher1 = des_encrypt(plaintext, round_keys1)
    cipher2 = des_encrypt(cipher1, round_keys2)
    cipher3 = des_encrypt(cipher2, round_keys1)
    return cipher3
