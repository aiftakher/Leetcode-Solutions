def numSubseq(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    nums = list(nums)
    mod = 1000000007

    pre = [0]*100001
    pre[0] = 1
    for i in range(1, 100001):
        pre[i] = (pre[i-1] * 2) % mod

    nums.sort()

    # sorted(arr) returns a copy of the sorted elements of the original array. Does not change the original array
    # arr.sort() does not return anything. Sorts the original array
    

    n = len(nums)
    j = n - 1
    ans = 0
    for i in range(n):
        while j >=0 and nums[i] + nums[j] > target:
            j = j - 1
        if(j>=i):
            ans = (ans + pre[j-i]) % mod
    return print(ans)



#    print(pre[5])



numSubseq([7,10,7,3,7,5,4], 12)