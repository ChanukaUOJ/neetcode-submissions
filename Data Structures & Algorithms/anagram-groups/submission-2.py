class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # first create a default dictionary where it keeps an empty list as the default values for the keys
        store = defaultdict(list)

        for s in strs:
            # sorted(s) returns a list of characters, so join with "" to make a single string in alphabetical character order
            sorted_str = "".join(sorted(s))

            # create a key in the store and append the original string to the value list
            store[sorted_str].append(s)

        return list(store.values())

        

