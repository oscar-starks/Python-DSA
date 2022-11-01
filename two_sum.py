def twoSum(nums, target):
    index_1 = 0
    index_2 = 0
    for num_1 in nums:
        for num_2 in nums:
            val = num_1 + num_2
            if (val == target):
                break
            index_2 += 1
        if (val == target):
            break
        index_1 += 1
    print(index_1, index_2)
    print(val)
            
twoSum([2,7,11,15], 9)