####### PYTHON MULTI THREADING EXAMPLE BY ATHUL NANDASWAROOP

'''
Python have 3 type of concurrency
1. Multi Processing (different process uses different cores of cpu,
   then creates worker threads according to the heavyness/cpu usage of task)
2. Multi Threading (different process uses creates multiple worker threads in a single core)
3. AsyncIO (uses only a single core and single thread, execution controlled by a very fast event loop such as uvloop)

concurrency method is selected based on the cpu need of process. Multi processing for highest load, other two follows

Here I am demonstrating  multi threading concurrency and proves it is working by providing
the time taken for the same Muti threaded vs Non Multi threaded version of code.

'''

from concurrent.futures import ThreadPoolExecutor
import uuid
import time



# SET WORKER/THREAD COUNT
workers = 5

# SET NUMBER OF FILES TO BE GENERATED
file_count = 5

# TO GENERATE RANDOM FILE NAME
gen_rand_name_list = lambda count:['./generated_files/'+str(uuid.uuid4())+'.txt' for _ in range(count)] 

# TO CREATE FILE
def create_file(name):
    # print(name)
    open(name, "w")

    # delay provided for understanding whether multi thread works or not. 
    # because, for very small process/load single threaded may become faster by overtaking thread creation time.
    time.sleep(0.5)
    
# FUNCTION WHICH PERFORM MULTI THREADING
def main():
    with ThreadPoolExecutor(max_workers=workers) as executor:
       
            executor.map(create_file,  gen_rand_name_list(file_count) )
            executor.shutdown(wait=True)

start_time = time.time()

main()

# PRINTS TOTAL EXECUTION TIME
print("Multi Threading Code took ________   %s seconds   ________" % (time.time() - start_time))

sync_time = time.time()

# NON MULTI THREADED MODE
file_names = gen_rand_name_list(file_count);
for item in file_names:
    create_file(item)

# PRINTS TOTAL EXECUTION TIME
print("Synchronous/Single thread Code took ________   %s seconds   _________" % (time.time() - sync_time))
