import threading
import time

def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
start = time.time()
threads = [threading.Thread(target=longSquare,args=(n, results)) for n in range(0,1001)]
[t.start() for t in threads]
[t.join() for t in threads]
fin = time.time()

print(results)
print(f'En {fin - start} segundos')

'''
#We can use this but it's to slow if we have to put one by one
t1 = threading.Thread(target=longSquare,args=(1,results))
t2 = threading.Thread(target=longSquare,args=(2,results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)'''