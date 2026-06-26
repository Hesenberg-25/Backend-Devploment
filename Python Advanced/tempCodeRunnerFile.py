import memory_profiler
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# Correct way to pull memory usage in MB
print(f'Memory (Before): {memory_profiler.memory_usage()[0]:.2f}MB')

def people_list(num_people):
    result = []
    for i in range(num_people): # Python 3 uses range, xrange is deprecated
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
        yield person # This 'yield' keyword turns the function into a generator

# --- TEST 1: The List Approach (Uncomment to test memory spike) ---
t1 = time.perf_counter() # time.clock() was removed in Python 3
people = people_list(1000000)
t2 = time.perf_counter()

# --- TEST 2: The Generator Approach ---
# t1 = time.perf_counter()
# people = people_generator(1000000)
# t2 = time.perf_counter()

print(f'Memory (After) : {memory_profiler.memory_usage()[0]:.2f}MB')
print(f'Took {t2-t1:.6f} Seconds')