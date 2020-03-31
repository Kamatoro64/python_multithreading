import threading
import time

start = time.perf_counter()


def do_something():  # Preferably I/O bound which will benefit from multithreading
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

# Without join, the thread will begin execution and the script will proceed, stopping the clock before the threads
# have finished executing

t1.join()
t2.join()


finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')
