from itertools import count

nums=[0, 1, 0, 12, 3]
i=0
while i <nums.count(0):
    nums.remove(0)
    nums.append(0)
    print(nums)
    i=i+1






