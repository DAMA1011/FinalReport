from concurrent.futures import ThreadPoolExecutor as tpe
import time

def Multi(num , count):
    if count < 10:
        print(f'{num} * {count} = {num*count}', end="\t")
        Multi(num, count + 1)
        time.sleep(0.01)
    print()

with tpe(max_workers=9) as executor:
    executor.map(Multi, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1] * 9)
