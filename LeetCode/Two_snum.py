def twoSum(nums, target):
    for _index, num in enumerate(nums):
        search_num = target - num
        b_list = nums[_index+1:]
        try:
            find_index = b_list.index(search_num) +1 + _index
        except:
            continue
        if find_index:
            return [_index, find_index]

if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9)) # [0,1]
    print(twoSum([2,3,5,4,6], 6)) # [0,1]
    print(twoSum([3, 3], 6)) # [0,1]