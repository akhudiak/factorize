import mltproc_function
from time import time


def synchronous_factorize(*number) -> list[list[int]]:

    function_result = []

    for divided in number:
        number_result = [divisor for divisor in range(1, divided + 1) if not divided % divisor]
        function_result.append(number_result)

    return function_result


if __name__ == "__main__":

    start_time = time()
    mltproc_result = mltproc_function.factorize(123456789, 84248932, 705784658, 10651060)
    print(f"Multiprocessing function time: {mltproc_function.func_time(start_time)}")

    start_time = time()
    synchronous_result = synchronous_factorize(123456789, 84248932, 705784658, 10651060)
    print(f"Synchronous function time: {mltproc_function.func_time(start_time)}")

    assert mltproc_result == synchronous_result

    