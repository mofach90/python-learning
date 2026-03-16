"""
Race Condition FIXED with Lock
==============================
Same scenario as 03_race_condition.py but now using a Lock.
The lock ensures only one thread can increment at a time.
Result: always exactly 2,000,000.

Remember: GIL protects Python's internals, Lock protects YOUR data.
"""

import threading

x = 0
lock = threading.Lock()

def increment():
    global x
    for _ in range(1_000_000):
        with lock:      # only one thread can enter this block
            x += 1      # LOAD, ADD, STORE happen without interruption

# Launch two threads doing the same thing
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Expected: 2,000,000")
print(f"Got:      {x:,}")
print(f"Lock works! No lost increments.")
