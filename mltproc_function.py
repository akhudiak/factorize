from multiprocessing import Pool
from time import time


def get_divisors(divided) -> list[int]:
    divisors = [divisor for divisor in range(1, divided + 1) if not divided % divisor]
    return divisors


def factorize(*number) -> list[list[int]]:

    with Pool(processes=4) as pool:
        function_result = pool.map(get_divisors, number)

    return function_result


def func_time(start_time):
    return time() - start_time


if __name__ == "__main__":

    start_time = time()
    
    factorize(123456789, 84248932, 705784658, 10651060)

    print(f"Function time: {func_time(start_time)}")
