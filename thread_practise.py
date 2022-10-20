import time
import pandas as pd
from multiprocessing import Process, Queue, Array, Manager
import sys

manager = Manager()
error_queue = manager.Queue()
if error_queue:
    print(error_queue)
error_queue.put("hello world")
print(error_queue.qsize())
error_queue.put(None)
print(error_queue.qsize())
p = error_queue.get()
print(p)
p = error_queue.get()
print(p)

print(error_queue.qsize())

sys.exit(1)



def func(arr, temp):
    for i in range(100000000):
        k = 1
    k = {"prem":1}
    # arr += k
    arr.append(k)
    return 

# returned_arr = []
# start_time = int(time.time())
# p = func(returned_arr)
# func(returned_arr)
# func(returned_arr)
# func(returned_arr)
# end_time = int(time.time())
# print(end_time - start_time)
# print(p)


temp = 1
manager = Manager()
dd = manager.dict()

arr = manager.list()
print("arr")
print(arr)
processes_list = []

lll = [1,2,3,4]
for i in lll:
    processes_list.append(Process(target=func, args=(arr, "prem", )))

print("processes_list")
print(processes_list)

# p1 = Process(target=func, args=(arr, "prem", ))
# p2 = Process(target=func, args=(arr, "soumik", ))
# p3 = Process(target=func, args=(arr, "rohit", ))
# p4 = Process(target=func, args=(arr, "palande", ))

start_time = int(time.time())
for each in processes_list:
    each.start()
for each in processes_list:
    each.join()


if arr:
    print("arr")
    print(arr)


# p1.start()
# p2.start()
# p3.start()
# p4.start()
# p1.join()
# p2.join()
# p3.join()
# p4.join()
end_time = int(time.time())
print(end_time - start_time)

print(arr)
print(type(arr))
ll = []
for i in arr:
    ll.append(i)
print(type(ll))
df = pd.DataFrame(ll)
print(df)


'''
to get the returned value
import multiprocessing

def worker(procnum, return_dict):
    """worker function"""
    print(str(procnum) + " represent!")
    return_dict[procnum] = procnum


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_dict.values())
'''
