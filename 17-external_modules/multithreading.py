import threading
import time

print_lock = threading.Lock()

#we just simulated a network request over here:
def worker(num):
    with print_lock:
        print(f"Thread {num} : Starting")
    time.sleep(2)
    with print_lock:
        print(f"Thread {num} : Ending")

threads = []
for i in range(1,4):
    thread = threading.Thread(target=worker, args=(i, ))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() #this will wait for all the threads to finish

print("all threads completed...")

#threading allows you to perform multiple I/O tasks concurrently
