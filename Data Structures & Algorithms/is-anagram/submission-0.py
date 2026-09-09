class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        achar = {}
        bchar = {}
        for i in s: 
            if i not in achar: 
                achar[i] = 1
            else:
                achar[i] += 1

        for i in t:
            if i not in bchar: 
                bchar[i] = 1
            else:
                bchar[i] += 1
        
        return achar == bchar 