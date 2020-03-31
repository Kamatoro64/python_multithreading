import threading
import time

start = time.perf_counter()


def do_something():  # Preferably I/O bound which will benefit from multithreading
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


# Create a list to store thread objects so we can loop through them
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')
