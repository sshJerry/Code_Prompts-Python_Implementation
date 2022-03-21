"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV.
 Because the one is before the five we subtract it making four. The same
 principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

"""




class Solution(object):
    def romanToInt(self, s):
        ans = 0
        symbol = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
                  'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        counter = {'IV': 0, 'IX': 0, 'XL': 0, 'XC': 0, 'CD': 0, 'CM': 0,
                   'I': 0, 'V': 0, 'X': 0, 'L': 0, 'C': 0, 'D': 0, 'M': 0}
        for x in symbol.keys():
            counter[x] += s.count(x)
            s = s.replace(x,'0')
            ans += symbol[x] * counter[x]
        return ans


s = Solution()
#Test Case 1
print(s.romanToInt('III'))
#Test Case 2
print(s.romanToInt('MCMXCIV'))
