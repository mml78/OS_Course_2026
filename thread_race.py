import threading
import time

# Shared global variable
counter = 0

# Number of increments per thread
INCREMENTS = 5000
THREADS = 4


# Race Condition
 
def increment_without_lock():
    global counter
    for _ in range(INCREMENTS):
        temp = counter
        temp += 1
        time.sleep(0.000001)  # FORCE context switch
        counter = temp


def run_without_lock():
    global counter
    counter = 0

    threads = []

    print("\n--- PART 1: WITHOUT LOCK (Race Condition) ---")
    print(f"Expected result: {INCREMENTS * THREADS}")

    # Create threads
    for _ in range(THREADS):
        t = threading.Thread(target=increment_without_lock)
        threads.append(t)
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    print(f"Actual result:   {counter}")


# Synchronization

lock = threading.Lock()


def increment_with_lock():
    global counter
    for _ in range(INCREMENTS):
        with lock:
            temp = counter
            temp += 1
            counter = temp


def run_with_lock():
    global counter
    counter = 0

    threads = []

    print("\n--- PART 2: WITH LOCK (Fixed Race Condition) ---")
    print(f"Expected result: {INCREMENTS * THREADS}")

    # Create threads
    for _ in range(THREADS):
        t = threading.Thread(target=increment_with_lock)
        threads.append(t)
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    print(f"Actual result:   {counter}")


# MAIN
 
if __name__ == "__main__":
    run_without_lock()
    run_with_lock()
