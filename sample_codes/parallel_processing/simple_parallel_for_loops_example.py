#https://blog.dominodatalab.com/simple-parallelization/

from joblib import Parallel, delayed
import multiprocessing

# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(10)


def processInput(i,b):
    return i * i, b


num_cores = multiprocessing.cpu_count()

results = Parallel(n_jobs=num_cores)(delayed(processInput)(i, True) for i in inputs)
print(results)