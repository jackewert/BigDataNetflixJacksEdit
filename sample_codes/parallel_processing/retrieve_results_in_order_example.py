'''
https://sebastianraschka.com/Articles/2014_multiprocessing.html
Note: The order of the obtained results does not necessarily have to match the order of the processes (in the processes list)
Depends on '._identity' attribute
'''
import multiprocessing as mp

# Define an output queue
output = mp.Queue()

# define a example function
def rand_string(length, pos, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str = ''.join(random.choice(
                        string.ascii_lowercase
                        + string.ascii_uppercase
                        + string.digits)
                   for i in range(length))
    output.put((pos, rand_str))

# Setup a list of processes that we want to run
processes = [mp.Process(target=rand_string, args=(5, x, output)) for x in range(4)]

# Run processes
for p in processes:
    p.start()

# Exit the completed processes
for p in processes:
    p.join()

# Get process results from the output queue
results = [output.get() for p in processes]

print(results)   # Results will be in tuple

# Make sure the results are in order
# To make sure that we retrieved the results in order, we could simply sort the results and optionally get rid of the position argument:
results.sort()
results = [r[1] for r in results]
print(results)
