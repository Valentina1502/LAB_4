#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

#7. среди всех 2значных чисел  определить те, которые
# делятся на на сумму своих цифр
#

if __name__ == '__main__':
    for x in range(10, 100):
        if (x % ((x // 10) + (x % 10)) == 0):
            print(f"{x}; ", end="")