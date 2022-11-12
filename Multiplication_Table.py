from concurrent.futures import ProcessPoolExecutor as tpe
import time

def Multi(num , count):
    if count < 10:
        print(f'{num} * {count} = {num*count}', end="\t")
        Multi(num, count + 1)
        time.sleep(0.1)
    print()

if __name__ == "__main__":
    with tpe(max_workers=9) as executor:
        executor.map(Multi, [1, 2, 3, 4, 5, 6, 7, 8, 9], [1] * 9)
