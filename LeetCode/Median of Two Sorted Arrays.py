class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # import numpy as np
        # L = np.array(nums1+nums2)
#         L = len(nums1+nums2)
#         Kth = L//2
#         if L%2 == 1:
#             #Kth : K0 means the 1st number; K1 means the 2nd number...... 
#             return self.FindKthSmallestNumber(nums1, nums2, Kth) 
#         else:
#             return (self.FindKthSmallestNumber(nums1, nums2, Kth-1) + self.FindKthSmallestNumber(nums1, nums2, Kth))/2
#             #if there is 6 numbers, we are looking the third and fourth smallest numbers which are K2, K3
#     def FindKthSmallestNumber(self, l1, l2,k):
#         if not l1:
#             return l2[k]
#         #if l1 is empty, then find the kth element in l2 which will be the median
#         if not l2:
#             return l1[k]
#         medianIndexOfl1, medianIndexOfl2 = len(l1)//2, len(l2)//2
#         medianOfl1, medianOfl2 = l1[medianIndexOfl1], l2[medianIndexOfl2]
#         #medianIndexOfl1 and medianIndexOfl2 also mean how many number smaller than median
#         if medianIndexOfl1+medianIndexOfl2<k:
#             # the sum can help us get rid of first X smallest number
#             if medianOfl1 > medianOfl2:
#                 startPositionOfNewList = medianIndexOfl2+1
#                 return self.FindKthSmallestNumber(l1, l2[startPositionOfNewList:], k-startPositionOfNewList)#we found first Y smallest number
#             else:
#                 startPositionOfNewList = medianIndexOfl1+1
#                 return self.FindKthSmallestNumber(l1[startPositionOfNewList:], l2, k-startPositionOfNewList)
                
#         else:
#             #if the the number of smaller numbers are greater than Kth we have to get rid of bigger number, the median will not be in set of greater numbers
#             if medianOfl1 > medianOfl2:
#                 startPositionOfNewList = medianIndexOfl1
#                 return self.FindKthSmallestNumber(l1[:startPositionOfNewList], l2, k)
#             else:
#                 startPositionOfNewList = medianIndexOfl2
#                 return self.FindKthSmallestNumber(l1, l2[:startPositionOfNewList], k)
            
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)