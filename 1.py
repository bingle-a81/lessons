import threading
import time
import queue

def source():
    for i in range(20):
        time.sleep(i/10)
        yield i

def worker(q):
    time.sleep(q/2)
    print(f'эл {q} обработан {threading.get_ident()} ')

my_queue = queue.Queue()

def producer():
    for element in source():
        my_queue.put(element)
        a= threading.get_ident()
        print(f'эл {element} был доб {a} в очередь {my_queue.qsize()}')
    my_queue.put(None)
    print(f'очередь заполнена')

def consumer():
    while True:
        elem=my_queue.get()
        if elem is None:
            my_queue.put(None)
            print(f'клиент закончил работу {threading.get_ident()}')
            break
        worker(elem)

thred_producer = threading.Thread(target=producer, daemon=True)
thred_producer.start()

thread_consumer1 = threading.Thread(target=consumer, daemon=True)
thread_consumer2 = threading.Thread(target=consumer, daemon=True)

thread_consumer1.start()
thread_consumer2.start()
thread_consumer1.join()
thread_consumer2.join()