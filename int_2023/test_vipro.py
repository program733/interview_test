print('test_vipro...')
'''

[8:46 PM] Venugopal Balaji
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 
Example 1:
Input: s = "anagram", t = "nagaram"Output: true
Example 2:
Input: s = "rat", t = "car"Output: false
 
Input: s = "anagram", t = "nagaram"Output: true
Input: s = "rat", t = "car"Output: false
'''

def check_anagram(s1,s2):
    temp_list = list(s1)
    for char in s2:
        if char in temp_list:
            temp_list.pop(temp_list.index(char))
        else:
            return False

    #print(temp_list)
    if len(temp_list) ==0:
        return True
    else:
        return False
#
# s = "anagram"
# t = "nagaram"
#
# s1 = "rat"
# t1 = "car"
#
# s2 = "aaaabbc"
# t2 = "abc"
# print(check_anagram(s1,t1))
# print(check_anagram(s,t))
# print(check_anagram(s2,t2))

strs = ["eat","tea","tan","ate","nat","bat"]
'''
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

'''
result = []
count = 1
for tstr in strs:
    tlist = []
    tlist.append(tstr)
    for lstr in strs[count:]:
        if check_anagram(tstr,lstr):
            tlist.append(lstr)
            strs.pop(strs.index(lstr))
    result.append(tlist)
    count+=1

print(result)
