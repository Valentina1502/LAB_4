#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    n = int(input("Введите номер месяца: "))

    if n == 1 or n == 2 or n == 12:
        print("Это ЗИМА")
    elif n == 3 or n == 4 or n == 5:
        print("Это ВЕСНА")
    elif n == 6 or n == 7 or n == 8:
        print("Это ЛЕТО")
    elif n == 9 or n == 10 or n == 11:
        print("Это ОСЕНЬ")
    else:
        print("Ошибка", file=sys.stderr)
        exit(1)