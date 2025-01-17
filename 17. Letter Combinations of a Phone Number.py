# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         new = [("2", "abc"), ("3", "def"), ("4", "ghi"),
#        ("5", "jkl"), ("6", "mno"), ("7", "pqrs"),
#        ("8", "tuv"), ("9", "wxyz")]
#         newDict=dict(new)
#         v=digits
#         if(len(v)>=4):
#             li = []
#             [li.append(list(newDict[i])) for i in v]
#             lj = []
#             # print(li)
#             for k in range(len(li)-3):
#                 for i in li[k]:
#                     for j in li[k+1]:
#                         for n in li[k+2]:
#                             for g in li[k+3]:
#                                 lj.append(str(i + j + n + g))
#             return(lj)
#         elif(len(v)>=3):
#             li = []
#             [li.append(list(newDict[i])) for i in v]
#             lj = []
#             # print(li)
#             for k in range(len(li)-2):
#                 for i in li[k]:
#                     for j in li[k+1]:
#                         for n in li[k+2]:
#                             lj.append(str(i + j + n))
#             return(lj)
#         elif(len(v)==2):
#             li=[]
#             [li.append(list(newDict[i])) for i in v]
#             lj=[]
#             # print(li)
#             for k in range(len(li)-1):
#                 for i in li[k]:
#                     for j in li[k+1]:
#                         lj.append(str(i+j))

#             return(lj)
#         elif(len(v)==1):
#             return(list(newDict[v]))
#         else:
#             return([])
                
from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        letter_lists = [digit_to_letters[d] for d in digits]
        
        return ["".join(comb) for comb in product(*letter_lists)]
