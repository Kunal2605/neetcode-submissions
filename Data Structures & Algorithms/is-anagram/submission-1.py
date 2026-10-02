class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = dict()
        dict2 = dict()
        for letter in s:
            if letter in dict1:
                dict1[letter] = dict1[letter]+1
            else:
                dict1[letter] = 1

        for letter in t:
            if letter in dict2:
                dict2[letter] = dict2[letter]+1
            else:
                dict2[letter] = 1

        for key in  dict1:
            if key not in dict2 or dict1[key] != dict2[key]:
                return False

        for key in  dict2:
            if key not in dict1 or dict1[key] != dict2[key]:
                return False
        
        return True
        