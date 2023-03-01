# This Python file uses the following encoding: windows-1251

import string


def knapSack_loop(W, S, result):
    n = len(W)
    if n == 0 or S < 0:
        result[0] = 1
        return result
    if S == 0:
        result[0] = 0
        return result
    if (W[n-1] <= S):
        result[n-1]=1
        S = S - W[n-1] 
    else:
        result[n-1]=0
    w = []
    for i in range(n-1):
        w.append(W[i]) 
    return knapSack_loop(w, S, result)


def knapSack(W, S):
    n = len(W)
    result = [0 for i in range(n)]
    return knapSack_loop(W, S, result)


def knapSack_loop_out(W, S, result, text):
    n = len(W)
    if n == 0:
        text.append(f'Решение: {result}\n')
        res = "".join(text)
        return res
    if (W[n-1] <= S):
        result[n-1]=1
        S = S - W[n-1] 
        text.append(f'w_{n-1} = {W[n-1]} <= S = {S}\n')
    else:
        result[n-1]=0
        text.append(f'w_{n-1} = {W[n-1]} > S = {S}\n')
    text.append(f'x_{n-1} = {result[n-1]}\n')
    w = []
    for i in range(n-1):
        w.append(W[i]) 
    return knapSack_loop_out(w, S, result, text)


def knapSack_out(W, S):
    text = []
    n = len(W)
    result = [0 for i in range(n)]
    return knapSack_loop_out(W, S, result, text)


# W = [1,2,4,8,16,32,64]
# S = 47
# print(knapSack_out(W, S))


def ks_encrypt(v,m,w,text):
    text = text.translate(str.maketrans({key: None for key in string.punctuation}))
    text = ''.join(text.split()).upper()
    bitalph = {"A": "00000", "B": "00001", "C": "00010", "D": "00011", "E": "00100"
             , "F": "00101", "G": "00110", "H": "00111", "I": "01000", "J": "01001"
             , "K": "01010", "L": "01011", "M": "01100", "N": "01101", "O": "01110"
             , "P": "01111", "Q": "10000", "R": "10001", "S": "10010", "T": "10011"
             , "V": "10100", "U": "10101", "W": "10110", "X": "10111", "Y": "11000", "Z": "11001"}
    text = [i for i in ''.join([bitalph[i] for i in text])]
    for i in range(len(text)%len(v)): text.append('1')
    temp_text = [''.join([text[i+j] for j in range(len(v))]) for i in range(0,len(text),len(v))]
    numb = [(i*w) % m for i in v]
    crypt = []
    for i in temp_text:
        sum = 0
        for k in range(len(v)):
            sum += int(i[k])*numb[k]
        crypt.append(sum)
    return crypt


# ks_encrypt([6, 8, 15, 31], 65, 12,'on sale.')


