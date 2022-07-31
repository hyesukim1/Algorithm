# -*- coding: utf-8 -*-
from __future__ import print_function
# 알파벳 찾기

string = input()
alphabet = list(range(97, 123))

for i in range(alphabet):
    if i in string:
        print(string.index(i), end= ' ')
    else:
        print(-1, end= ' ')