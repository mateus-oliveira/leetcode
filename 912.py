class Solution:
    MAX_QUICK_SORT_LENGTH = 15 # arbitrary size to use quicksort
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
    
    def quick_sort(self, nums):
        """
        Quick Sort algorithm
        """
        if len(nums) <= 1:
            return nums

        pivot = nums.pop(len(nums)//2) # pivot from the middle

        left = []
        right = []

        for n in nums:
            if n >= pivot:
                right.append(n)
                continue
            left.append(n)

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def merge_sort(self, nums):
        """
        Merge Sort algorithm
        """
        if len(nums) <= 1:
            return nums

        if len(nums) <= self.MAX_QUICK_SORT_LENGTH:
            return self.quick_sort(nums)
        
        middle = len(nums)//2
        left = self.merge_sort(nums[:middle])
        right = self.merge_sort(nums[middle:])
        
        return self.merge(left, right)

    def merge(self, left, right):
        sorted_array = []
        left_index = 0
        right_index = 0
        
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                sorted_array.append(left[left_index])
                left_index += 1
            else:
                sorted_array.append(right[right_index])
                right_index += 1
        
        sorted_array.extend(left[left_index:])
        sorted_array.extend(right[right_index:])
        
        return sorted_array
