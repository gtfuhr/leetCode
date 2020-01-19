from math import floor

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = []
        
        total_len = len(nums1) + len(nums2)
        i ,num_1, num_2 = 0, 0, 0
        
        while(i < total_len):
            i += 1
            try:
                num_1 = nums1[0]
            except:
                l.append(nums2.pop(0))
                continue
            try:
                num_2 = nums2[0]
            except:
                l.append(nums1.pop(0))            
                continue
                
            if(num_1 < num_2):
                l.append(nums1.pop(0))
            else:
                l.append(nums2.pop(0))
    
        
        if(total_len % 2 == 0):
            return (l[total_len/2] + l[total_len/2 -1])/2
        return float(l[floor(total_len/2)])
