def square(nums):
    result=[]
    for i in nums:
        result.append(i*i)

    return result

square_nums=square([1,2,3,4])

print(square_nums)