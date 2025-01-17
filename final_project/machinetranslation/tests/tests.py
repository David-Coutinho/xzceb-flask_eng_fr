import unittest

import sys
import os
print(os.getcwd())
sys.path.append(os.getcwd())

from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertIsNotNone(englishToFrench(None))

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertIsNotNone(frenchToEnglish(None))

unittest.main()