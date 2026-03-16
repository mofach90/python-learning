
"""
Multiprocessing — True Parallelism
===================================
Two heavy CPU tasks run in separate processes.
Each process has its own memory and its own GIL.
They truly run at the same time on different CPU cores.

Compare the time: parallel should be ~2x faster than sequential.
"""

import multiprocessing
import time


def heavy_compute(name):
    """Simulate heavy CPU work"""
    print(f"  [{time.strftime('%H:%M:%S')}] {name} START")
    total = sum(range(50_000_000))
    print(f"  [{time.strftime('%H:%M:%S')}] {name} END (result: {total:,})")


if __name__ == "__main__":

    # --- Sequential (one after another) ---
    print("=== Sequential ===")
    start = time.time()
    heavy_compute("Task 1")
    heavy_compute("Task 2")
    seq_time = time.time() - start
    print(f"Sequential time: {seq_time:.2f}s\n")

    # --- Parallel (true parallelism) ---
    print("=== Parallel (multiprocessing) ===")
    start = time.time()

    p1 = multiprocessing.Process(target=heavy_compute, args=("Process 1",))
    p2 = multiprocessing.Process(target=heavy_compute, args=("Process 2",))

    p1.start()    # launches a NEW Python process
    p2.start()    # launches ANOTHER Python process

    p1.join()     # wait for p1 to finish
    p2.join()     # wait for p2 to finish

    par_time = time.time() - start
    print(f"Parallel time: {par_time:.2f}s")
    print(f"Speedup: {seq_time / par_time:.1f}x faster!")