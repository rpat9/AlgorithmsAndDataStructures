# [P-3.57]: Perform experimental analysis to test the hypothesis that Python’s sorted method runs in O(n log n) time on average. 

import random
import time
import matplotlib.pyplot as plt
import math

# Lists to hold list sizes and corresponding sorting times
list_sizes_x = []
time_taken_y = []
nlogn_y = []

for n in range(2, 1501):
    random_list = [random.randint(0, 10000) for _ in range(n)]
    
    # Time the sorting operation
    start_time = time.time()
    sorted_list = sorted(random_list)
    end_time = time.time()
    
    # Record the time taken and the list size
    time_taken_y.append(end_time - start_time)
    list_sizes_x.append(n)
    
    # Calculate the theoretical O(n log n) for comparison
    nlogn_y.append(n * math.log(n))

# Scale using a ratio. Played around with values to make the graph look good
ratio = max(time_taken_y) / max(nlogn_y)
nlogn_y_scaled = [t * ratio for t in nlogn_y]

if __name__ == '__main__':
    
    plt.figure()
    plt.plot(list_sizes_x, time_taken_y, label='Observed Sort Time')
    plt.plot(list_sizes_x, nlogn_y_scaled, label='O(n log n)', linestyle='--')

    plt.xlabel("List Size")
    plt.ylabel("Time taken (seconds)")
    plt.title("Time Complexity of Python's sorted()")
    plt.legend()
    plt.show()