class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        items = defaultdict(int)

        for i in nums:
            items[i] = items[i] + 1

        output = [key for key,val in sorted(items.items(), reverse=True, key=lambda item: item [1])[:k]]

        return output
        