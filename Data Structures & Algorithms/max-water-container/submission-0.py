class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = abs(right - left)
            height = min(heights[left], heights[right])
            area = width * height
            max_area = max(max_area, area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_area