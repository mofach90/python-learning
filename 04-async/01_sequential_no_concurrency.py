import asyncio
import time


# 1. Regular sync function
def sync_compute():
    print(f"[{time.strftime('%H:%M:%S')}] sync_compute START")
    total = sum(range(10_000_000))
    print(f"[{time.strftime('%H:%M:%S')}] sync_compute END")


# 2. Async function with compute + HTTP + compute
async def async_function_2():
    print(f"\n[{time.strftime('%H:%M:%S')}] async_function_2 START")

    # compute before HTTP
    print(f"[{time.strftime('%H:%M:%S')}]   compute before HTTP...")
    total = sum(range(5_000_000))

    # simulate an HTTP request that takes 2 seconds
    # asyncio.sleep() behaves EXACTLY like a real await:
    # it yields control back to the event loop
    print(f"[{time.strftime('%H:%M:%S')}]   awaiting HTTP request (simulated 2s)...")
    await asyncio.sleep(2)
    print(f"[{time.strftime('%H:%M:%S')}]   HTTP response received!")

    # compute after HTTP
    print(f"[{time.strftime('%H:%M:%S')}]   compute after HTTP...")
    total = sum(range(5_000_000))

    print(f"[{time.strftime('%H:%M:%S')}] async_function_2 END")


# 3. Regular compute in between
def middle_compute():
    print(f"\n[{time.strftime('%H:%M:%S')}] middle_compute START")
    total = sum(range(10_000_000))
    print(f"[{time.strftime('%H:%M:%S')}] middle_compute END")


# 4. Another async function (same pattern)
async def async_function_3():
    print(f"\n[{time.strftime('%H:%M:%S')}] async_function_3 START")

    print(f"[{time.strftime('%H:%M:%S')}]   compute before HTTP...")
    total = sum(range(5_000_000))

    print(f"[{time.strftime('%H:%M:%S')}]   awaiting HTTP request (simulated 2s)...")
    await asyncio.sleep(2)
    print(f"[{time.strftime('%H:%M:%S')}]   HTTP response received!")

    print(f"[{time.strftime('%H:%M:%S')}]   compute after HTTP...")
    total = sum(range(5_000_000))

    print(f"[{time.strftime('%H:%M:%S')}] async_function_3 END")
 

# Main orchestrator
async def main():
    start = time.time()

    # Step 1: sync compute
    sync_compute()

    # Step 2: await async function 2 (sequential - no concurrency!)
    await async_function_2()

    # Step 3: middle compute
    middle_compute()

    # Step 4: await async function 3 (sequential - no concurrency!)
    await async_function_3()

    elapsed = time.time() - start
    print(f"\n{'='*50}")
    print(f"Total time: {elapsed:.2f} seconds")
    print("Notice: everything ran sequentially!")
    print("The two 2-second waits added up (~4s total wait)")


asyncio.run(main())
