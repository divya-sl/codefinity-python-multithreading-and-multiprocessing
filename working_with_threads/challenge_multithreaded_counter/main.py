import threading

class ThreadSafeCounter:
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()

    # Implement increment and get_value methods here
    def increment(self):
        with self.lock:
            self.counter += 1

    def get_value(self):
        with self.lock:
            return self.counter

def worker(counter, num_increments):
    for _ in range(num_increments):
        counter.increment()

counter = ThreadSafeCounter()
threads = []
num_threads = 10
increments_per_thread = 1000

for _ in range(num_threads):
    t = threading.Thread(target=worker, args=(counter, increments_per_thread))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter value: {counter.get_value()}")
