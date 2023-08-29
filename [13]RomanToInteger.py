class Solution:
    # M
    def romanToInt(self, s: str) -> int:
        sum = 0
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s)):
            numeral = s[i]
            if i + 1 < len(s) and roman_numerals[numeral] < roman_numerals[s[i+1]]:
                sum -= roman_numerals[numeral]
            else:
                sum += roman_numerals[numeral]

        return sum


a = Solution()
print(a.romanToInt('IV'))