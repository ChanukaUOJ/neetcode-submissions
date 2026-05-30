class Solution:

    def strToDic(self, str_val: str) -> Dict:

        store = {}
        for i in str_val:
            if i in store.keys():
                store[i] = store[i] + 1
            else:
                store[i] = 1
        
        return store

    def isAnagram(self, first_str: str, second_str: str) -> bool:
        if len(first_str) != len(second_str):
            return False
        
        store_one = self.strToDic(first_str)
        store_two = self.strToDic(second_str)

        return store_one == store_two

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        values_last = []
        values_remove = []
        for i in range(len(strs)):
            if strs[i] in values_remove:
                continue
            values_middle = []
            values_middle.append(strs[i])
            for j in range(i+1, len(strs)):
                is_an = self.isAnagram(strs[i], strs[j])
                if is_an:
                    values_middle.append(strs[j])
                    values_remove.append(strs[j])
            
            values_last.append(values_middle)
        
        return values_last

