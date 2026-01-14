import sys
import cProfile

# List comprehension is faster than generator expressions 
# But generator expressions waste less memory

doubles_lc = [num*2 for num in range(1,5000)]
doubles_ge = (num*2 for num in range(1,5000))

print(sys.getsizeof(doubles_lc))
print(sys.getsizeof(doubles_ge))

print(cProfile.run("max([num*2 for num in range(1,100000)])"))
print(cProfile.run("max((num*2 for num in range(1,100000)))"))