# # def isPal(num):
# #     num=str(num)
# #     is_it=True
# #     start=0
# #     last=len(num)-1
# #
# #     while start < last:
# #         if num[start] == num [last]:
# #             start+=1
# #             last-=1
# #         else:
# #             is_it=False
# #             break
# #     return is_it
# #
# # print(isPal(1321))
#
# def Roma(s):
#     ds = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     count = 0
#
#     for i in range(len(s)):
#         if s[i]=="I" and s[i+1]=="V":
#             count+=ds["V"]-ds["I"]
#             i+=2
#         elif s[i]=="I" and s[i+1]=="X":
#             count+=ds["X"]-ds["I"]
#             i+=2
#         elif s[i]=="X" and s[i+1]=="L":
#             count+=ds["L"]-ds["X"]
#             i+=2
#         elif s[i]=="X" and s[i+1]=="C":
#             count+=ds["C"]-ds["X"]
#             i+=2
#         elif s[i]=="C" and s[i+1]=="D":
#             count+=ds["D"]-ds["C"]
#             i+=2
#         elif s[i]=="C" and s[i+1]=="M":
#             count+=ds["M"]-ds["C"]
#             i+=2
#         else:
#             st=s[i]
#             count+=ds[st]
#     return count
# s = "III"
# print(Roma(s))
#
from django.db.models.expressions import result
from numpy.ma.core import max_val

prices = [7,6,4,3,1]
min_idx=min(prices)
va=prices.index(min_idx)

price=prices[va:]

max_val=max(price)

result=max_val-prices[va]
print(min_idx)
print(va)
print(price)
print(result)