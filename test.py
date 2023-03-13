import time
import random
import os.path
import importlib
import pisano_example1

N = 400
M = 6000


def get_samples():
    """ Make a list of N samples chosen from [2, M]
    """
    random.seed(11235)  # Seed will be changed for the final scoring
    samples = random.sample(range(2, M+1), N)
    return sorted(samples)


def do_test(solution, samples, reference):
    """ Execute a function and compare the results with the reference
    """
    t0 = time.perf_counter()
    module = importlib.import_module(solution)
    func = module.get_pisano_numbers
    results = list(func(samples.copy()))
    t1 = time.perf_counter()
    runtime = (t1-t0) * 1000
    file_size = os.path.getsize(module.__file__)
    result = "PASS" if results == reference else "FAIL"
    return result, int(runtime), file_size


if __name__ == '__main__':
    samples = get_samples()
    reference = pisano_example1.get_pisano_numbers(samples)

    print("NAME\t\t\t\tRESULT\t  TIME\t  SIZE\t SCORE")
    for solution in [
            "pisano_example1",
            "pisano_example2",
            # add the name of your own module
    ]:
        result, runtime, file_size = do_test(solution, samples, reference)
        score = runtime + file_size
        print(f"{solution:30s}\t{result}\t{runtime:6d}\t{file_size:6d}\t{score:6d}")
