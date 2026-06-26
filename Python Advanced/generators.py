# Here we are returning the amswer in form of result which is a list

def square(nums):
    result=[]
    for i in nums:
        result.append(i*i)

    return result

square_nums=square([1,2,3,4])

print(square_nums)


# Here we are using the keyword 'yield' to Access the Generators
def square_num(nums):
    for i in nums:
        yield(i*i)

squarenum=square_num([1,2,3,4,5])

# To print the results we can use two methods

# By using the next keymord sufficient number of times
# If it exceeds compiler will throw StopIteration Error
print(next(squarenum))
print(next(squarenum))
print(next(squarenum))
print(next(squarenum))
print(next(squarenum))

#Using the for Loop which stops before the error of StopIteration
for nums in squarenum:
    print(nums)

# Other way to COde to get list of Squares : 
numsquare=[x*x for x in [1,2,3,4,5]]
print(numsquare)

# To Convert to Generator : 
numsquare=(x*x for x in [1,2,3,4,5])
print(numsquare)

for i in numsquare:
    print (i)

# You can convert it to List by just using "list(numsquare)"
 
# Advantage of Generators over List
# 1. Readablity of the Code Increaes
# 2. As Generators do not store the Data this gives us Edge over Perfomance

import memory_profiler
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print(f'Memory (Before): {memory_profiler.memory_usage()[0]:.2f}MB')

def people_list(num_people):
    result = []
    for i in range(num_people): 
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person 

# --- TEST 1: The List Approach (Uncomment to test memory spike) ---
t1 = time.perf_counter() 
people = people_list(1000000)
t2 = time.perf_counter()

# --- TEST 2: The Generator Approach ---
# t1 = time.perf_counter()
# people = people_generator(1000000)
# t2 = time.perf_counter()

print(f'Memory (After) : {memory_profiler.memory_usage()[0]:.2f}MB')
print(f'Took {t2-t1:.6f} Seconds')


