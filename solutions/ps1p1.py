# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

import unittest
s = 'zcrnuexzleowufibkewodnuj'  # comment this string before copy-past.


def vowels(st):
    count = 0
    for ch in st:
        if ch in 'aeiou':
            count += 1
    return count


class TestProblem1(unittest.TestCase):
    def test_vowels(self):
        self.assertEqual(vowels('satake'), 3)
        self.assertEqual(vowels('rwuclaviekcneygw'), 5)
        self.assertEqual(vowels('riqnbbifzctqaiauo'), 7)
        self.assertEqual(vowels('ufaeuvaenzfvrmaofvwejd'), 9)


print("Number of vowels:", vowels(s))

# if __name__ == '__main__':
#     unittest.main()

