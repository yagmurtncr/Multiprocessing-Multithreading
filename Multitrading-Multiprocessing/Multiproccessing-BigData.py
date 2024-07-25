import multiprocessing
import time

def process_data(data_chunk):
    # Veriyi işleme
    result = [x * x for x in data_chunk]
    return result

if __name__ == '__main__':
    data = list(range(1000000))
    chunk_size = len(data) // multiprocessing.cpu_count()
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool() as pool:
        results = pool.map(process_data, chunks)
    
    final_result = [item for sublist in results for item in sublist]
    print("Data processing complete")