class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        def median(nums):
            n = len(nums)
            return (nums[int((n - 1) / 2)] + nums[int(n / 2)]) / 2
            
        if n1 == 0:
            return median(nums2)
        if n2 == 0:
            return median(nums1)
        
        def lessThan(nums, target):
            # return number of elements in nums which is less than target
            if target <= nums[0]:
                return 0
            elif target > nums[-1]:
                return len(nums)
            else:
                left = 0
                right = len(nums) - 1
                while left < right:
                    mid = int((left + right + 1) / 2)
                    if nums[mid] < target:
                        left = mid
                    else:
                        right = mid - 1
                return right + 1
            
        def largerThan(nums, target):
            # return number of elements in nums which is larger than target
            if target < nums[0]:
                return len(nums)
            elif target >= nums[-1]:
                return 0
            else:
                left = 0
                right = len(nums) - 1
                
                while left < right:
                    mid = int((left + right) / 2)
                    if nums[mid] <= target:
                        left = mid + 1
                    else:
                        right = mid
                return len(nums) - right
            
        def helper(nums1, nums2, smaller, larger):
            left = min(nums1[0], nums2[0])
            right = max(nums1[-1], nums2[-1])
            n = len(nums1) + len(nums2)
            while left < right:
                mid = int((left + right) / 2)
                a = lessThan(nums1, mid) + lessThan(nums2, mid)
                b = largerThan(nums1, mid) + largerThan(nums2, mid)
                a = n - a    # >= target
                b = n - b    # <= target
                if b < smaller:
                    left = mid + 1
                elif a < larger:
                    right = mid - 1
                else:
                    return mid
            return left
        
        k = int((n1 + n2) / 2)
        if (n1 + n2) % 2 == 0:
            a1 = helper(nums1, nums2, k, k+1)
            a2 = helper(nums1, nums2, k+1, k)
            return (a1 + a2) / 2
        else:
            return helper(nums1, nums2, k+1, k+1)