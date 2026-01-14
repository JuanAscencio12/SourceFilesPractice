from multiprocess import Process
import time
#NO LOGRE QUE FUNCIONARA - REVISAR DESPUES
def longSquare(num, results):
    time.sleep(1)
    print(num**2)
    print('Finished computing!')

results = {}
processes = [Process(target=longSquare,args=(n,results)) for n in range(0,10)]
[p.start() for p in processes]
[p.join() for p in processes]