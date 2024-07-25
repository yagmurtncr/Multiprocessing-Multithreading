# Multithreading, bir uygulamanın aynı anda birden fazla iş parçacığı (thread) çalıştırmasını sağlar.
#  Her iş parçacığı, aynı bellek alanını paylaşır.

import threading
import time

def print_numbers():
    for i in range(10):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(f"Letter: {letter}")
        time.sleep(1)

# İki iş parçacığı oluştur
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# İş parçacıklarını başlat
thread1.start()
thread2.start()

# İş parçacıklarının bitmesini bekle
thread1.join()
thread2.join()

print("Done with multithreading")