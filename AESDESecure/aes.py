import os

def permute(table, text, n):
    new_text = ""
    for i in range(n):
        new_text += text[table[i] - 1]
    return new_text

def getText(str_list, index):
    text = ""
    for i in str_list[index]:
        text += '{:0>8}'.format(bin(ord(i))[2:])
    return text

def xor(str1, str2):
    res = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            res += '0'
        else:
            res += '1'
    return res

s_box = [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
        [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
        [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
        [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
        [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
        [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
        [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
        [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
        [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
        [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
        [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
        [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
        [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
        [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
        [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
        [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]

inv_sbox = [[0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
        [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
        [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
        [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
        [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
        [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
        [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
        [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
        [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
        [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
        [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
        [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
        [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
        [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
        [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
        [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]]

def aes_key_encryption(key):
    
    # get set of 4 words
    words = []
    counter = 0
    for i in range(4):
        words.append(key[counter: counter+32])
        counter += 32

    round_constants = [0x1, 0x2, 0x4, 0x8, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
    round_keys = [key]

    for round in range(10):
        # Find g(w3)
        shift_word = words[3][8:] + words[3][:8]

        # sbox on shift_word
        sboxed = []
        counter = 0
        while counter < len(shift_word):
            row = int(shift_word[counter:counter+4], 2)
            col = int(shift_word[counter+4:counter+8], 2)
            val = s_box[row][col]
            sboxed.append('{:0>8}'.format(bin(val)[2:]))
            counter += 8

        # Add round constant to sboxed
        new_word = ''.join(i for i in sboxed)
        g_w3 = xor(new_word[:8], '{:0>8}'.format(bin(round_constants[round])[2:])) + new_word[8:]

        # Create words of next key
        new_words = [None, None, None, None]
        new_words[0] = xor(g_w3, words[0])
        for i in range(1, 4):
            new_words[i] = xor(new_words[i-1], words[i])

        next_key = ""
        for i in range(4):
            next_key += new_words[i]

        words = new_words
        round_keys.append(next_key)

    return round_keys

def aes_encrypt(plaintext, round_keys):

    state = [[None]*4 for i in range(4)]

    # xor plaintext with key 0
    counter = 0
    
    for x in range(4):
        for y in range(4):
            state[y][x] = xor(plaintext[counter: counter+8], round_keys[0][counter: counter+8])
            counter += 8

    for round in range(10):
        # Substitution Bytes - sbox
        for x in range(4):
            for y in range(4):
                row = int(state[x][y][:4], 2)
                col = int(state[x][y][4:], 2)
                val = s_box[row][col]
                state[x][y] = '{:0>8}'.format(bin(val)[2:])

        # Shift Row
        for i in range(4):
            state[i] = state[i][i:] + state[i][:i]

        # Mix Columns

        if round != 9:
            col_mixer = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]

            new_state = [['00000000']*4 for i in range(4)]
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        if(col_mixer[i][k] == 1):
                            new_state[i][j] = xor(new_state[i][j], state[k][j])
                        elif(col_mixer[i][k] == 2):
                            if(state[k][j][0] == '1'):
                                temp = state[k][j][1:] + '0'
                                new_state[i][j] = xor(new_state[i][j], xor(temp, '00011011')) # XOR with 1B
                            else:
                                new_state[i][j] = xor(new_state[i][j], state[k][j][1:] + '0')
                        elif(col_mixer[i][k] == 3):
                            if(state[k][j][0] == '1'):
                                temp = state[k][j][1:] + '0'
                                new_state[i][j] = xor(new_state[i][j], xor(temp, '00011011')) # XOR with 1B
                            else:
                                new_state[i][j] = xor(new_state[i][j], state[k][j][1:] + '0')
                            new_state[i][j] = xor(new_state[i][j], state[k][j])
            state = new_state

        # Add Roundkey
        counter = 0
        for i in range(4):
            for j in range(4):
                # print(hex(int(round_keys[round+1][counter: counter+8], 2)))
                state[j][i] = xor(state[j][i], round_keys[round+1][counter: counter + 8])
                counter += 8

    ciphertext = ""
    for x in range(4):
        for y in range(4):
            ciphertext += state[y][x]
    return ciphertext

def aes_decrypt(ciphertext, round_keys):
    state = [[None]*4 for i in range(4)]

    # xor ciphertext with key 0
    counter = 0
    
    for x in range(4):
        for y in range(4):
            state[y][x] = xor(ciphertext[counter: counter+8], round_keys[0][counter: counter+8])
            counter += 8

    for round in range(10):

        # Mix Columns
        # M^4 = I => M inverse = M^3
        if round != 0:
            col_mixer = [[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]]

            result = state
            for loop in range(3):
                new_state = [['00000000']*4 for i in range(4)]
                for i in range(4):
                    for j in range(4):
                        for k in range(4):
                            if(col_mixer[i][k] == 1):
                                new_state[i][j] = xor(new_state[i][j], result[k][j])
                            elif(col_mixer[i][k] == 2):
                                if(result[k][j][0] == '1'):
                                    temp = result[k][j][1:] + '0'
                                    new_state[i][j] = xor(new_state[i][j], xor(temp, '00011011')) # XOR with 1B
                                else:
                                    new_state[i][j] = xor(new_state[i][j], result[k][j][1:] + '0')
                            elif(col_mixer[i][k] == 3):
                                if(result[k][j][0] == '1'):
                                    temp = result[k][j][1:] + '0'
                                    new_state[i][j] = xor(new_state[i][j], xor(temp, '00011011')) # XOR with 1B
                                else:
                                    new_state[i][j] = xor(new_state[i][j], result[k][j][1:] + '0')
                                new_state[i][j] = xor(new_state[i][j], result[k][j])
                result = new_state

            state = new_state

        # Shift Row
        for i in range(4):
            state[i] = state[i][4-i:] + state[i][:4-i]

        # Substitution Bytes - sbox
        for x in range(4):
            for y in range(4):
                row = int(state[x][y][:4], 2)
                col = int(state[x][y][4:], 2)
                val = inv_sbox[row][col]
                state[x][y] = '{:0>8}'.format(bin(val)[2:])

        
        # Add Roundkey
        counter = 0

        for i in range(4):
            for j in range(4):
                # print(hex(int(round_keys[round+1][counter: counter+8], 2)))
                state[j][i] = xor(state[j][i], round_keys[round+1][counter: counter + 8])
                counter += 8

    plaintext = ""
    for x in range(4):
        for y in range(4):
            plaintext += state[y][x]
    return plaintext

def aes(plaintext, key):
    plaintext = bin(int(plaintext, 16))[2:].zfill(128)
    key = bin(int(key, 16))[2:].zfill(128)

    round_keys = aes_key_encryption(key)

    print("Round Keys:")
    for i in round_keys:
        print(hex(int(i, 2)))
    rev_round_keys = []
    for i in reversed(round_keys):
        rev_round_keys.append(i)

    ciphertext = aes_encrypt(plaintext, round_keys)
    return ciphertext
