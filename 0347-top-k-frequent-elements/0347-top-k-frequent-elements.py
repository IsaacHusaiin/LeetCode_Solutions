class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        most_frequent = Counter(nums)
        most_k_num= most_frequent.most_common(k)
        return [num for num, count in most_k_num]