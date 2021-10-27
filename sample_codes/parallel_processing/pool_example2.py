'''
e four methods that are particularly interesting:
Pool.apply
Pool.map
Pool.apply_async    equivalent to apply()
Pool.map_async      equivalent to map()


The Pool.map and Pool.apply will lock the main program until all processes are finished,

sync variants will submit all processes at once and retrieve the results as soon as they are finished

get method after the apply_async() call in order to obtain the return values of the finished processes.
'''
import multiprocessing as mp


def cube(x):
    return x**3

poolProcesses = mp.Pool(processes=4)
results = [poolProcesses.apply(cube, args=(x,)) for x in range(1, 7)]
print(results)

poolProcesses = mp.Pool(processes=4)
results = poolProcesses.map(cube, range(1, 7))
print(results)

poolProcesses = mp.Pool(processes=4)
results = [poolProcesses.apply_async(cube, args=(x,)) for x in range(1, 7)]
output = [p.get() for p in results]
print(output)