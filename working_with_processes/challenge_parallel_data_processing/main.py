import numpy as np
from multiprocessing import Process, Queue

def worker(segment, queue):
    # Compute the square of each number in segment and put the result in the queue
    for index, seg in segment.items():
        result = []
        for num in seg:
            result.append(int(num * num))
        segment = {}
        segment[index] = result
        queue.put(segment)
            

def parallel_square(numbers, num_processes):
    # Implement splitting, process creation, result collection, and combining here
    queue = Queue()
    processes = []
    segments = np.array_split(numbers, num_processes)
    i = 0
    for seg in segments:
        segment = {}
        segment[i] = seg
        i += 1
        p = Process(target=worker, args=(segment, queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = {}
    while not queue.empty():
        result_segment = queue.get()
        results.update(result_segment)

    result = []
    for index, seg in sorted(results.items()):
        for num in seg:
            result.append(num)
    
    #print(result)
    return result
        

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    num_processes = 3
    squared = parallel_square(numbers, num_processes)
    print(squared)
