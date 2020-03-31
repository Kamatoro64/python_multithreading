import threading
import time

start = time.perf_counter()


def do_something(seconds):  # Preferably I/O bound which will benefit from multi threading
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')


# Create a list to store thread objects so we can loop through them
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    # Note that you cannot do t.join() here because the thread would execute and then join before the next thread is
    # started in which case we're essentially executing the threads sequentially
    threads.append(t)

# Wait for all the threads to finish executing before taking the finish timestamp
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')
