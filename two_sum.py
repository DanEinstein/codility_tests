# THis is the two sum problem that i will be trying to test in intelij for the first time
#Basically here is the problem. We need two numbers in a set oor array such that when we add them they result to the target which is also part of the array. W e need to find the indices of the numbers
print("This is  the two sum problem feel free to watch")
def check(target,nums):
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if(sum ==target):
                return [i,j]
    return[]
nums = [2,4,5,6,3,8,1,0]
target = 9
print(check(target,nums))



