
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
from typing import Tuple, List
from random import randint
from math import gcd, sqrt

def read_text(FILENAME):
    f = open(FILENAME, 'r', encoding='windows-1251')
    ot = f.read()
    f.close()
    return ot

def read_text_list(filename):
    text = []
    with open(filename, 'r') as f:
        text.append(f.readline())
    return text
    

def get_prime_numbers_in_range(start: int, finish: int) -> List[int]:
    # ������� ��� ������� ����� �� �������� ����������
    #
    # ������ ������� ����� �� ���������
    primes = []
    # ������ � ������� True - ����� �������, False - ����� ���������
    is_prime = [True] * (finish + 1)
    # 0 � 1 �� �������
    is_prime[0] = is_prime[1] = False
    # ������ ���������� i - �����, is_prime_i - ������� ��� ���
    for i, is_prime_i in enumerate(is_prime):
        if is_prime_i:
            # ��������� ������� ����� � ������, ���� ��� � ���������
            if i >= start:
                primes.append(i)
            # ��� ����� �� i * i �� finish � ����� i ������ i
            for j in range(i * i, finish + 1, i):
                is_prime[j] = False
    return primes


def get_prime_number_in_range(start: int, finish: int) -> int:
    # ������� ������� ����o �� ���������� [start, finish]
    #
    res = get_prime_numbers_in_range(start, finish)
    return res[randint(2, len(res) - 1)]


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    # ������������ �������� �������
    #
    a0 = a
    b0 = b
    t0 = 0
    t = 1
    s0 = 1
    s = 0
    q = a0 // b0
    r = a0 - q * b0
    while r > 0:
        temp = t0 - q * t
        t0 = t
        t = temp
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = a0 // b0
        r = a0 - q * b0
    r = b0
    return r, s, t


def binary_pow(a: int, b: int, p: int) -> int:
    # �������� ��������� ���������� � �������
    # ���� ������� ����� 0, �� ��������� ����� 1
    if b == 0:
        return 1
    # ������������� d � �������� �������
    # ������� bin() ���������� ������ ���� '0b1010'
    # ������� ������������� � �������� ������� ���������� �� 2 �������
    d = bin(b)[2:]
    r = len(d) - 1
    # �������� ������ a_i
    a_ = [0] * (r + 1)
    # ������� a_0 = a
    a_[0] = a
    # ��������� a_i ��� i = 1,...,r, r = len(d) - 1
    for i in range(1, r + 1):
        # ��������� a_i
        a_[i] = (a_[i - 1] ** 2) * (a ** int(d[i]))
        # ����� ������� �� ������
        a_[i] %= p
    # ���������� a_r �� ������ ��� ������� ����� d = 1
    return a_[r] % p


def modular_inv(number: int, mod: int) -> int:
    # ������� �������� ����� �� ������ ��� �����
    #
    # ������� ��� ������ � ����� � ������������ ����������� ����
    # ��������� ����������� �������� �������.
    t, x, y = extended_gcd(number, mod)
    # ���� ��� �� ����� 1, �� ��������� ����� ���
    if t != 1:
        raise ValueError('----')
    # ��� ������������� ����� ����� ��������� ������
    return (x % mod + mod) % mod


def get_coprime_in_range(
        start: int, finish: int, number: int) -> int:
    # ������� ����� �� ���������� [start, finish] ������� ������� � number
    #
    for i in range(start, finish):
        if gcd(number, i) == 1:
            return i
    return i


def is_prime(n: int) -> bool:
    # ���������, �������� �� ����� �������.
    #
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def check_values(a: int, b: int, p: int) -> bool:
    # ��������� �������� ���������� ���������
    #
    return gcd(a, p) == 1 and gcd(b, p) == 1 and p != 2 and is_prime(p)


def get_values(number_of_runs: int) -> List[Tuple[int, int, int]]:
    # ������� ���������� �������� ��� �������� ������� ����������.
    # �������� ����������� ��� ������������ �������� �������.
    values = []
    for _ in range(number_of_runs):
        a, b, p = 0, 0, 0
        # ���� ����� �� ������������� �������� ������
        # ���������� ����� ��������
        while not check_values(a, b, p):
            a, b, p = randint(1, 1000), randint(1, 1000), randint(1, 1000)
        values.append((a, b, p))
    return values