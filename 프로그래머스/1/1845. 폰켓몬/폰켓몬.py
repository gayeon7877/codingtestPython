def solution(nums):
    if len(set(nums))<(len(nums)//2):
        return len(set(nums))
    return len(nums)//2