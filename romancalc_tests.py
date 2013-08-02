import unittest

class RomanNumeralsCalculatorTests(unittest.TestCase):

    def test_I_I(self):
        result = self.add("I", "I")
        self.assertEqual(result, "II")

    def test_I_II(self):
        result = self.add("I", "II")
        self.assertEqual(result, "III")

    def test_II_II(self):
        result = self.add("II", "II")
        self.assertEqual(result, "IV")
        
    def test_II_III(self):
        result = self.add("II", "III")
        self.assertEqual(result, "V")

    def test_III_III(self):
        result = self.add("III", "III")
        self.assertEqual(result, "VI")

    def test_IV_I(self):
        result = self.add("IV", "I")
        self.assertEqual(result, "V")

    def test_IX_I(self):
        result = self.add("IX", "I")
        self.assertEqual(result, "X")
        
    def test_XXIV_IX(self):
        result = self.add("XXIV", "IX")
        self.assertEqual(result, "XXXIII")

    def test_XIV_LX(self):
        result = self.add("XIV", "LX")
        self.assertEqual(result, "LXXIV")
        
    def test_CCCLXIX_DCCCXLV(self):
        result = self.add("CCCLXIX", "DCCCXLV")
        self.assertEqual(result, "MCCXIV")

    def test_MCCLIX_CMLXXXVI(self):
        result = self.add("MCCLIX", "CMLXXXVI")
        self.assertEqual(result, "MMCCXLV")        
        
    def add(self, x, y):
        uncompacted = self.explodeSubstractions(x) + self.explodeSubstractions(y)
        uncompacted = list(uncompacted)
        uncompacted.sort(key=self.sortRomanNumerals)
        
        result = self.compact(''.join(uncompacted))

        return result

    def explodeSubstractions(self, value):
        value = value.replace("CM", "DCCCC")
        value = value.replace("XL", "XXXX")
        value = value.replace("IX", "VIV")
        value = value.replace("IV", "IIII")
        return value

    def compact(self, value):
        value = value.replace("IIIII", "V")
        value = value.replace("IIII", "IV")
        value = value.replace("VV", "X")
        value = value.replace("XXXXX", "L")
        value = value.replace("XXXX", "XL")
        value = value.replace("LL", "C")
        value = value.replace("CCCCC", "D")
        value = value.replace("DD", "M")
        return value
            
    def sortRomanNumerals(self, word):
       romanAlphabet = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
                
       numbers = []
       for letter in word:
          numbers.append(romanAlphabet.index(letter))

       return numbers

if __name__ == '__main__':
    unittest.main(verbosity=2)

