# This Python file uses the following encoding: windows-1251

from typing import Tuple, List
from random import randint, choice
from math import gcd
from util import binary_pow, get_prime_number_in_range, modular_inv, get_coprime_in_range


def get_random_message(size: int) -> str:
    # Возращает рандомную строку
    #
    m = []
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size):
        m.append(choice(alpha))
    res = ""
    res = res.join(m)
    return res


def get_primitive_root(p: int) -> int:
    #  Находит первообразноый корень по модулю p
    #
    if p == 2:
        return 1
    p1 = 2
    p2 = (p - 1) // p1
    while True:
        g = randint(2, p - 1)
        if not (binary_pow(g, (p - 1) // p1, p) == 1):
            if not binary_pow(g, (p - 1) // p2, p) == 1:
                return g


def my_hash(string: str, p: int) -> int:
    # Находит дайджест строки string
    #
    sum = 1
    for pos in range(len(string)):
        sum = sum + ord(string[pos])
    return sum % p


def get_primitive_roots(modulo: int) -> List[int]:
    # Находит все первообразные корни числа modulo
    #
    roots = []
    required_set = set(
        num for num in range(1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) %
                         modulo for powers in range(1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots


def get_keys_ElGamal(A: int, B: int) -> Tuple[int, int, int, int]:
    # Генерирует открытый и приватный кдючи для ЭЦП Эль-Гамаля
    #
    # Выбор простого числа p
    p = get_prime_number_in_range(A, B)
    # Выбор целое число g - первообразный корень p
    g = get_primitive_root(p)
    # Выбор случайного целого числа x такого, что 1 < x < p-1
    x = get_prime_number_in_range(1, p - 1)
    # y = g^x (mod p)
    y = binary_pow(g, x, p)
    return y, p, g, x


def ds_ElGamal(m: str, p: int, g: int, x: int) -> Tuple[int, int]:
    # Создает ЦП Эль-Гамаля сообщения m
    #
    h = my_hash(m, p)
    k = get_coprime_in_range(1, p - 1, p - 1)
    r = binary_pow(g, k, p)
    u = binary_pow((h - x * r), 1, p - 1)
    k_inv = 9 #modular_inv(k, p - 1)
    s = binary_pow((u * k_inv), 1, p - 1)
    return r, s


def ds_ElGamal_outp(m: str, p: int, g: int, x: int) -> str:
    # Создает ЦП Эль-Гамаля сообщения m
    #
    outp = []
    h = my_hash(m, p)
    outp.append(f'h = h(m) = {h}\n')
    k = get_coprime_in_range(1, p - 1, p - 1)
    outp.append(f'k = {k}\n')
    r = binary_pow(g, k, p)
    outp.append(f'r = g^k (mod p) = {r}\n')
    u = binary_pow((h - x * r), 1, p - 1)
    outp.append(f'u = (h - x * r) (mod p-1) = {u}\n')
    k_inv = 9  # modular_inv(k, p - 1)
    outp.append(f'k^-1 = {k_inv}\n')
    s = binary_pow((u * k_inv), 1, p - 1)
    outp.append(f's = k^-1 * u (mod p-1) = {s}\n')
    outp.append(f"Подпись: <{r},{s}>\n")
    # outp.reverse()
    res = "".join(outp)
    return res


def check_ds_ElGamal(m: str, r: int, s: int, y: int, g: int, p: int) -> bool:
    # Проверяет ЦП Эль-Гамаля сообщения m
    #
    if ((r < 0 or r > p) or (s < 0 or s > p - 1)):
        return False
    h = my_hash(m, p)
    left = binary_pow(binary_pow(y, r, p) * binary_pow(r, s, p), 1, p)
    right = binary_pow(g, h, p)
    if (left == right):
        return True
    else:
        return False


def check_ds_ElGamal_outp(m: str, r: int, s: int,
                          y: int, g: int, p: int) -> str:
    # Проверяет ЦП Эль-Гамаля сообщения m
    #
    outp2 = []
    if (r < 0 or r > p):
        outp2.append(f"Число r = {r} некорректно.\n")
        res = "".join(outp2)
        return res
    elif(s < 0 or s > p - 1):
        outp2.append(f"Число s = {s} некорректно.\n")
        res = "".join(outp2)
        return res

    h = my_hash(m, p)
    outp2.append(f'h = h(m) = {h}\n')
    left = binary_pow(binary_pow(y, r, p) * binary_pow(r, s, p), 1, p)
    outp2.append(f'y^r * r^s = {left} (mod p)\n')
    right = binary_pow(g, h, p)
    outp2.append(f'g^h (mod p) = {right}\n')
    if (left == right):
        outp2.append(f'{left} = {right}\n')
        outp2.append('Подпись подлинна.\n')
        res = "".join(outp2)
        return res
    else:
        outp2.append(f'{left} != {right}\n')
        outp2.append('Подпись подделана.\n')
        res = "".join(outp2)
        return res