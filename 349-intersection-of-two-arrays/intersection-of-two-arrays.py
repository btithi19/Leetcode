class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []

        for i in nums1:
            if i in nums2 and i not in answer:
                answer.append(i)

        return answer