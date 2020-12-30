#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def abbreviation(a, b):
    match_string = []
    original_string = []
    match_string[:0] = b
    original_string[:0] = a
    coincidence = 0
    last_character = ''
    i = 0
    while len(original_string) > 0:
        if len(match_string) == 0:
            break
        elif coincidence == len(b) and (original_string[0].isupper() == False or last_character.upper() == original_string[0].upper()):
            original_string.pop(0)
        elif coincidence == len(b) and original_string[0].isupper() == True:
            i = i+1
            coincidence = 0
            match_string = []
            match_string[:0] = b
        elif original_string[0].upper() == match_string[0]:
            coincidence += 1
            last_character = original_string.pop(0)
            match_string.pop(0)
        else:
            if i >= len(original_string):
                break
            elif (original_string[i] != original_string[i].upper() or last_character.upper() == original_string[i].upper()):
                original_string.pop(i)
            else:
                i = i+1
                coincidence = 0
                match_string = []
                match_string[:0] = b

    return "YES" if coincidence == len(b) else "NO"

print(abbreviation("abcdefghijklmnopqrstuvwxyzabaBababababababababaBababababababababababababAbabababAbabababababababababAbabababababababAbababababaBabababababababababababaBabababAbababababababababababababababababAbababababababababababababAbabaBababababababababababAbAbabababababAbababababababAbababaBabaBabaBabABababAbababAbabababababababababAbAbabababAbAbabababababaBababababababAbababABabAbabAbababababaBabababababababababababababababababababababAbababababababAbabababababababababababaBabaBabababababababaBababababaBababAbababaBabaBabababababababababababaBababababababababaBababababababababAbAbabaBabababAbabAbabababababaBababababababAbababababAbabababababaBabababababaBAbababAbabababababAbabababababababababababababababababababababababababaBababababAbababababababababababAbabababababAbAbabababababababABabababababababaBababababababaBabababababababababababAbababababababababababAbabaBabababAbabababababAbabababAbabababababababAbabababababababababababaBabAbababababABCDEFGHIJKLMNOPQRSTUVWXYZ","ABCDEFGHIJKLMNOPQRSTUVWXYZAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBAABBABCDEFGHIJKLMNOPQRSTUVWXYZ"))
