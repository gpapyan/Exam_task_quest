# def value(r):
#     if r == 'I':
#         return 1
#     if r == 'V':
#         return 5
#     if r == 'X':
#         return 10
#     if r == 'L':
#         return 50
#     if r == 'C':
#         return 100
#     if r == 'D':
#         return 500
#     if r == 'M':
#         return 1000
#     return -1
#
#
# def number_conv(rom):
#     res = 0
#     i = 0
#
#     while i < len(rom):
#         s1 = value(rom[i])
#
#         if i + 1 < len(rom):
#             s2 = value(rom[i + 1])
#             if s1 >= s2:
#                 res = res + s1
#                 i = i + 1
#             else:
#                 res = res + s2 - s1
#                 i = i + 2
#         else:
#             res = res + s1
#             i = i + 1
#     return res
#
#
# a = "XXIV"
#
# print(f"Number Convert form Roman Numeral is {number_conv(a)}")


class Exam:
    def roman_to_num(self, s):

        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in roman:
                num += roman[s[i:i + 2]]
                i += 2
            else:
                num += roman[s[i]]
                i += 1
        return num


ob1 = Exam()
print(ob1.roman_to_num("CDXLIII"))
print(ob1.roman_to_num("XXIVI"))
