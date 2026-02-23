import asyncio
import time


# 1. Regular sync function
def sync_compute():
    print(f"[{time.strftime('%H:%M:%S')}] sync_compute START")
    total = sum(range(10_000_000))
    print(f"[{time.strftime('%H:%M:%S')}] sync_compute END")


# 2. Async function with compute + await + compute
async def async_function_2():
    print(f"[{time.strftime('%H:%M:%S')}]   func_2: compute before HTTP...")
    total = sum(range(5_000_000))

    print(f"[{time.strftime('%H:%M:%S')}]   func_2: awaiting HTTP (2s)...")
    await asyncio.sleep(2)  # <-- yields control to event loop
    print(f"[{time.strftime('%H:%M:%S')}]   func_2: HTTP response received!")

    print(f"[{time.strftime('%H:%M:%S')}]   func_2: compute after HTTP...")
    total = sum(range(5_000_000))
    print(f"[{time.strftime('%H:%M:%S')}]   func_2: DONE")


# 3. Another async function (same pattern)
async def async_function_3():
    print(f"[{time.strftime('%H:%M:%S')}]   func_3: compute before HTTP...")
    total = sum(range(5_000_000))

    print(f"[{time.strftime('%H:%M:%S')}]   func_3: awaiting HTTP (2s)...")
    await asyncio.sleep(2)  # <-- yields control to event loop
    print(f"[{time.strftime('%H:%M:%S')}]   func_3: HTTP response received!")

    print(f"[{time.strftime('%H:%M:%S')}]   func_3: compute after HTTP...")
    total = sum(range(5_000_000))
    print(f"[{time.strftime('%H:%M:%S')}]   func_3: DONE")


# 4. Regular compute
def middle_compute():
    print(f"\n[{time.strftime('%H:%M:%S')}] middle_compute START")
    total = sum(range(10_000_000))
    print(f"[{time.strftime('%H:%M:%S')}] middle_compute END")


async def main():
    start = time.time()

    # Step 1: sync compute (runs first, nothing special)
    sync_compute()

    # Step 2: run BOTH async functions concurrently!
    # gather() puts both on the event loop's task board
    # so when func_2 hits "await", func_3 can start running
    print(f"\n[{time.strftime('%H:%M:%S')}] Starting BOTH async functions concurrently...")
    await asyncio.gather(
        async_function_2(),
        async_function_3()
    )

    # Step 3: runs AFTER both async functions are done
    middle_compute()

    elapsed = time.time() - start
    print(f"\n{'='*50}")
    print(f"Total time: {elapsed:.2f} seconds")
    print("Notice: the two 2-second waits OVERLAPPED!")
    print("We saved ~2 seconds compared to sequential version!")


asyncio.run(main())