class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            
        while k > 0:
            k -= 1
            x = max(freq.values())
            for num in freq:
                if freq[num] == x:
                    ans.append(num)
                    del freq[num]
                    break

        return ans