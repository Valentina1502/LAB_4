#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

# 8. Решить неравенство      корень(а-х)  >  х-2
# где а - действительное число
#

if __name__ == '__main__':
    a = float(input("Введите А (действительное число): "))

    if (4 * a) > 5:
        n = -5 + 4 * a
        x1 = (3 + math.sqrt(n)) / 2
        x2 = (3 - math.sqrt(n)) / 2
    else:
        print("Неверное значение А", file=sys.stderr)
        exit(1)
print(f" При а = {a}: X1 = {x1}, x2 = {x2}")