class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if((len(s) != len(t)) or (len(set(s)) != len(set(t)))):
            return False
        else:
            dic1 = {}
            dic2 = {}
            for x in s:
                if x in dic1.keys():
                    dic1[x] = dic1[x] + 1
                else:
                    dic1[x] = 1

            for x in t:
                if x in dic2.keys():
                    dic2[x] = dic2[x] + 1
                else:
                    dic2[x] = 1
            
            for x in dic1.keys():
                if x not in dic2.keys():
                    return False
                if dic1[x] != dic2[x]:
                    return False

            return True   

        