"""
Race Condition Example
======================
Two threads increment the same variable 1,000,000 times each.
Expected result: 2,000,000
Actual result: less than 2,000,000 (run it multiple times to see it vary!)
"""

import threading

x = 0

def increment():
    global x
    for _ in range(1_000_000):
        x += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Expected: 2,000,000")
print(f"Got:      {x:,}")
print(f"Lost:     {2_000_000 - x:,} increments!")
