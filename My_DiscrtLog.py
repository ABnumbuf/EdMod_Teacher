# This Python file uses the following encoding: windows-1251
from math import sqrt, ceil
from functools import reduce
from typing import List
from util import binary_pow, get_prime_numbers_in_range, modular_inv


def factorize(number: int) -> List[int]:
    # ������������� ����� �� ��������� ���� p1^a1, p2 ^a2 ....
    #
    # ������� ������� �� number
    primes = get_prime_numbers_in_range(1, number)
    # ������ ����������
    factors = []
    # �������� �� ���� ������� ������
    for prime in primes:
        # ���� ������� �� ������� �� ������� ����� �� ����� ����, �� ���������
        # � ���������� �������� �����
        if number % prime != 0:
            continue
        factor = 1
        # ����� ����� �� ������� �����
        while number % prime == 0:
            number //= prime
            factor *= prime
        # ��������� ��������� � ������
        factors.append(factor)
    return factors


def chineese_remainder_theorem(a: int, m: int) -> int:
    # ��������� ������� �� ��������
    #
    result = 0
    # ������� ������������ ���� �������
    M = reduce(lambda x, y: x * y, m)
    for a_i, m_i in zip(a, m):
        M_i = M // m_i
        result += a_i * modular_inv(M_i, m_i) * M_i
    return result % M


def my_ord(a: int, mod: int) -> int:
    # ��������� ������� ����� a �� ������ mod
    #
    for p in range(1, mod):
        if binary_pow(a, p, mod) == 1:
            return p


def coherence_method(a: int, b: int, n: int) -> int:
    # ����� ������������
    #
    # ������� ������� ����� a �� ������ n
    ord_na = my_ord(a, n)
    # ������� h, �������� �� �������� ������ ������ �� n
    h = ceil(sqrt(ord_na))
    # ������� ������ ��� �������� �������� b*a^t (mod n), t = 0, ..., h - 1
    tList = [(b * binary_pow(a, t, n)) % n for t in range(h)]
    # ��������� �������� �������� (a^h)^l (mod n), l = 1, ..., h �
    # ���������� � ���������� � ������
    for l in range(1, h + 1):
        temp = binary_pow(a, h * l, n)
        for t in range(h):
            # ���� �������� �����, �� ���������� x = h * l - t
            if temp == tList[t]:
                return h * l - t


def coherence_method_output(a: int, b: int, n: int) -> str:
    # ����� ������� ������ ������������
    #
    output1 = []
    # ������� ������� ����� a �� ������ n
    ord_na = my_ord(a, n)
    output1.append(f'ord({a}) = {ord_na}\n')
    # ������� h, �������� �� �������� ������ ������ �� n
    h = ceil(sqrt(ord_na))
    output1.append(f'h({n}) = {h}\n')
    # ������� ������ ��� �������� �������� b*a^t (mod n), t = 0, ..., h - 1
    tList = [(b * binary_pow(a, t, n)) % n for t in range(h)]
    t = 0
    for i in tList:
        output1.append(f'{b}*{a}^{t} (mod {n}) = {i}\n')
        t += 1
    # ��������� �������� �������� (a^h)^l (mod n), l = 1, ..., h �
    # ���������� � ���������� � ������
    for l in range(1, h + 1):
        temp = binary_pow(a, h * l, n)
        output1.append(f'{a}^{h}^{l} (mod {n}) = {l}\n')
        for t in range(h):
            # ���� �������� �����, �� ���������� x = h * l - t
            if temp == tList[t]:
                output1.append(f'{temp} = {tList[t]}\n')
                output1.append(f'x = {h}*{l} - {t} = {h * l - t}\n')
                res = "".join(output1)
                return res


def sylvester_pohlig_hellman_method(a: int, b: int, p: int) -> int:
    # ����� ����������-������-��������
    #
    # ������� ������� ����� � �� ������ p
    ord_pa = my_ord(a, p)
    # ������� p_i^alpha_i
    factors = factorize(ord_pa)
    # ������� mu_i = ord(a, p) / p_i^alpha_i
    mu = [ord_pa // factor for factor in factors]
    # ������� x_i
    x = [coherence_method(binary_pow(a, mu_i, p),
                          binary_pow(b, mu_i, p), p) for mu_i in mu]
    # ���� ����� ������������ �� ��� �������, �� ���������� None
    if None in x:
        return None
    # ������� x ��������� ��������� ������� �� ��������
    return chineese_remainder_theorem(x, factors)


def sylvester_pohlig_hellman_method_output(
        a: int, b: int, p: int) -> str:
    # ����� ������� ������ ����������-������-��������
    #
    output2 = []
    # ������� ������� ����� � �� ������ p
    ord_pa = my_ord(a, p)
    output2.append(f'h({p}) = {ord_pa}\n')
    # ������� p_i^alpha_i
    factors = factorize(ord_pa)
    output2.append(f'{p}  = {factors}\n')
    # ������� mu_i = ord(a, p) / p_i^alpha_i
    mu = [ord_pa // factor for factor in factors]
    for i in factors:
        output2.append(
            f'mu_{factors.index(i)} = {ord_pa} / {i}  = {mu[factors.index(i)]}\n')
    # ������� x_i
    x = [coherence_method(binary_pow(a, mu_i, p),
                          binary_pow(b, mu_i, p), p) for mu_i in mu]
    for j in mu:
        output2.append(
            f'x_{mu.index(j)} = log{binary_pow(a, j, p)} ({binary_pow(b, j, p)}) = {x[mu.index(j)]}\n')
    # ������� x ��������� ��������� ������� �� ��������
    x = chineese_remainder_theorem(x, factors)
    output2.append(f'x = {x}\n')
    res = "".join(output2)
    return res