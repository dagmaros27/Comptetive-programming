"""
You are given two non-increasing 0-indexed integer arrays nums1 and nums2

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. 
The distance of the pair is j - i.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.
Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2

i = 0
j = 0
nums1[i] <= nums2[j] -> 55 < 100 -> distance = j - i = 0

i = 2
j = 4
nums1[i] <= nums2[j] -> 5 <= 5 -> distance = j - i = 2

Constraints
1 <= len(nums) <= 10^5
1 <= nums[i] <= 10^5 for all 0 <= i < nums.length

"""

"""
Solution
-> Brute force
we can choose every i, j pair

i = 0, -> j = 0, j = 1, j = 2, j = 3, ... 
i = 1, -> j = 0, j = 1, j = 2, j = 3, ...
"""

# Brute force
"""
ans = 0
for i in range(N1):
    for j in range(i, N2):
        if nums1[i] <= nums2[j]:
            ans = max(ans, j - i)
"""

"""
condition -> nums1[i] <= nums2[j]
distance -> j - i

[55,30,5,4,2]
    i
[100,20,10,10,5]
     j

at (i, j) = (0, 1), it is invalid
we also won't find an answer for i = 0 and j = 1, 2, 3, 4
then move i and see
"""

def get_distance(nums1, nums2):
    N1 = len(nums1)
    N2 = len(nums2)
    
    i = 0
    ans = 0
    for j in range(N2):
        if nums1[i] <= nums2[j]:
            ans = max(ans, j - i)
        else:
            i += 1
            if i == N1:
                break
    
    """
    Time Complexity = O(max(N1, N2))
    Space complexity = O(1)
    """
    
    return ans


nums1 = [55]
nums2 = [100,20,10,10,5]
ans = get_distance(nums1, nums2)
print(ans)
