 #Multiprocessing, bir uygulamanın aynı anda birden fazla işlem (process) çalıştırmasını sağlar.
 #Her işlem, kendi bellek alanına sahiptir.


import multiprocessing
import time

def print_numbers():
    for i in range(10):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'abcdefghij':
        print(f"Letter: {letter}")
        time.sleep(1)

if __name__ == '__main__':
    # İşlemleri oluştur
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # İşlemleri başlat
    process1.start()
    process2.start()

    # İşlemlerin bitmesini bekle
    process1.join()
    process2.join()

    print("Done with multiprocessing")
