
def selection_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        
        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp
        
nums = [1, 8, 7, 9, 5, 4]
selection_sort(nums)
print(nums) 
