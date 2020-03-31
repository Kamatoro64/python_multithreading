import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):  # Preferably I/O bound which will benefit from multi threading
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...' # Return instead of printing


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # The submit method schedules a function to be executed and returns a futures object
    # However, instead of doing this 1 by 1, we use a loop above to spawn multiple threads

    # Manual method
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)

    # print(f1.result())
    # print(f2.result())


finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')
