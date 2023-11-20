from time import time


def factorize(*number) -> list[list[int]]:

    function_result = []
    
    for divided in number:
        number_result = [divisor for divisor in range(1, divided + 1) if not divided % divisor]
        function_result.append(number_result)

    return function_result


def func_time(start_time):
    return time() - start_time


if __name__ == "__main__":

    start_time = time()
    
    factorize(123456789, 84248932, 705784658, 10651060)

    print(f"Function time: {func_time(start_time)}")
