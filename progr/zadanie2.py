#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    dictionary = {1: "Tool", 2: "is", 3: "a", 4: "great", 5: "band" }

    rev_dict = {v: k for k, v in dictionary.items()}

    print("Исходный словарь:", dictionary)
    print('Обратный словарь:', rev_dict)
