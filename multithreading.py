import time

start = time.perf_counter()

def do_something(): # Preferably I/O bound which will benefit from multithreading
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')
