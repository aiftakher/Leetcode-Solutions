import sys
sys.stdin = open('Leetcode/input.txt','r')
sys.stdout = open('Leetcode/output.txt','w')

#class Solution(object):
def findDifference(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    distA = []
    distB = []

    for i in range(len(nums1)):
        if nums1[i] in nums2:
            continue
        else:
            distA.append(nums1[i])
    for i in range(len(nums2)):
        if nums2[i] in nums1:
            continue
        else:
            distB.append(nums2[i])
    return [set(distA), set(distB)]

findDifference([1,2,3],[2,4,6])


