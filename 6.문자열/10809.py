# -*- coding: utf-8 -*-
from __future__ import print_function
# 알파벳 찾기

s = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(s.find(chr(i)), end=' ')