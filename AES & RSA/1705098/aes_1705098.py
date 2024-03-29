# -*- coding: utf-8 -*-
"""BitVectorDemo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NoLVEBqkvrHwoYoEuxX0BeJvaJ5MtVrA
"""

#!pip install BitVector


"""Tables"""

from BitVector import *
import time 

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

Rcon = (
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)

class AES:

    Nk = 4
    Nb = 4
    Nr = 10
    mode = 128
    key_expansion_time = 0
    pad_amount = 0

    def __init__(self, key, mode=128):
        if mode == 192:
            self.Nk = 6
            self.Nr = 12
            self.mode = 192
            self.key = self.text2matrix(key , 24)
        elif mode == 256:
            self.Nk = 8
            self.Nr = 14
            self.mode = 256
            self.key = self.text2matrix(key, 32)
        else:
            self.key = self.text2matrix(key)

        start_time = time.time()
        self.key_expansion(self.key)
        self.key_expansion_time = (time.time() - start_time)

    def text2matrix(self, text, len=16):
        """
        converts a txt to state array
        """
        state = []

        for i in range(len):
            # two hex characters == 1 byte
            byte = int(text[i*2:i*2+2], 16)
            if i % 4 == 0:
                # first byte of the column
                state.append([byte])
            else:
                # Append byte to the row i/4 
                state[i // 4].append(byte) 
     
        return state

    def matrix2text(self, s, len=16):
        """
        convert state array to txt
        """
        text = ""
        for i in range(len // 4):
            for j in range(4):
                text += format(s[i][j], '02x')

        return text

    def sub_bytes(self, s):
        
        for i in range(self.Nb):
            for j in range(4):
                s[i][j] = Sbox[s[i][j]]
    
    def inv_sub_bytes(self, s):
        
        for i in range(self.Nb):
            for j in range(4):
                s[i][j] = InvSbox[s[i][j]]

    def shift_rows(self, s):
        
        s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]

    def inv_shift_rows(self, s):

        s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]
   
   
    def mix_col(self , state_array ):

        tmp = []

        modulus = BitVector(bitstring="100011011")

        for i in range(len(Mixer)):
            l=[]
            for j in range(len(state_array[0])):

                bb = BitVector(intVal = 0, size=8)    

                for k in range(len(state_array)):

                    a = Mixer[j][k]
                    b = BitVector(intVal=state_array[i][k],size=8)
                    ss = a.gf_multiply_modular(b,modulus,8)
                    bb = bb ^ ss

                l.append(bb.intValue())

            tmp.append(l)

        self.state = tmp

    def inv_mix_col(self , matrix):

        tmp = []
       
        modulus = BitVector(bitstring="100011011")

        for i in range(len(InvMixer)):
            l = []
            for j in range(len(matrix[0])):
                
                bb = BitVector(intVal = 0, size=8)
                
                for k in range(len(matrix)):
                    a = InvMixer[j][k]
                    b = BitVector(intVal=matrix[i][k],size=8)
                    ss = a.gf_multiply_modular(b,modulus,8)
                    bb = bb ^ ss
                
                l.append(bb.intValue())

            tmp.append(l)
        
        self.state =  tmp


    def add_round_key(self, s, k):
        
        for i in range(self.Nb):
            for j in range(4):
                s[i][j] ^= k[i][j]

    def sub_word(self, w):

        for i in range(len(w)):
            w[i] = Sbox[w[i]]


    def rotate_word(self, w):

        w[0], w[1], w[2], w[3] = w[1], w[2], w[3], w[0]

    def key_expansion(self, key):

        self.round_keys = self.key

        for i in range(self.Nk, self.Nb * (self.Nr + 1)):
            self.round_keys.append([0, 0, 0, 0])
            temp = self.round_keys[i - 1][:]
            
            if i % self.Nk == 0:
                self.rotate_word(temp)
                self.sub_word(temp)
                temp[0] = temp[0] ^ Rcon[i // self.Nk]
            elif self.Nk > 6 and i % self.Nk == 4:
                self.sub_word(temp)

            for j in range(4):
                self.round_keys[i][j] = self.round_keys[i - self.Nk][j] ^ temp[j]

    
    def cipher(self, text):

        self.state = self.text2matrix(text , (self.mode//8))
        self.add_round_key(self.state, self.round_keys[:4])

        for i in range(1, self.Nr):
            self.sub_bytes(self.state)
            self.shift_rows(self.state)
            self.mix_col(self.state)
            self.add_round_key(self.state, self.round_keys[self.Nb * i : self.Nb * (i + 1)])

        self.sub_bytes(self.state)
        self.shift_rows(self.state)
        self.add_round_key(self.state, self.round_keys[len(self.round_keys) - 4:])

        return self.matrix2text(self.state)

    def decipher(self, text):

        self.state = self.text2matrix(text , (self.mode//8))
        self.add_round_key(self.state, self.round_keys[len(self.round_keys) - 4:])
       

        for i in range(self.Nr - 1, 0, -1):
            self.inv_shift_rows(self.state)
            self.inv_sub_bytes(self.state)
            self.add_round_key(self.state, self.round_keys[self.Nb * i : self.Nb * (i + 1)])
            self.inv_mix_col(self.state)
           
        self.inv_shift_rows(self.state)
        self.inv_sub_bytes(self.state)
        self.add_round_key(self.state, self.round_keys[:4])

        return self.matrix2text(self.state)

def pad(str):
    
    n = len(str)
    if n == 16:
        return str 
    elif n < 16:
        for _ in range(n , 16):
            str += '0'
        return str 
    else:
        nearest_multiple = 16*(1 + int(n/16))
        for _ in range(n , nearest_multiple):
            str += '0'
        return str 

def pad_key(str):
    n = len(str)
    if n == 16:
        return str 
    elif n < 16:
        for _ in range(n , 16):
            str += '0'
        return str 
    else:
        return str[:16]
    

if __name__ == "__main__":
        
    key = input("Enter AES key : ")
    key = pad_key(key)
    
    k=""
    for c in key:
        k += format(ord(c), "x")

    aes = AES(k)

    text =input("Enter msg to cipher : ")
    text_to_cipher = pad(text)
    aes.pad_amount = len(text_to_cipher) - len(text)

    k=""
    for c in text_to_cipher:
        k += format(ord(c), "x")

    orig_msg = ""
    cipher_txt = ""
    enc_time = 0
    dec_time = 0

    for i in range(0 , len(k) , 32):

        start_time = time.time()
        cipher = aes.cipher(k[i:i+32])
        enc_time += (time.time() - start_time)

        cipher_txt += cipher

        start_time = time.time()
        text = aes.decipher(cipher)
        dec_time += (time.time() - start_time)

        orig_msg += bytearray.fromhex(text).decode()

    print("Cipher (Hex) : " + cipher)
    
    #print orig msg
    n = len(orig_msg)
    orig_msg = orig_msg[:n-aes.pad_amount]
    print("Original msg : " + orig_msg)


    print("Key scheduing time : " + str(aes.key_expansion_time) + "s")
    print("Encryption time : " + str(enc_time) + "s")
    print("Decryption time : " + str(dec_time) + "s")

