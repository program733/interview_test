print("hello world...")
import threading
import time
from threading import Thread

# Function to be executed in multiple threads
def print_numbers():
    for i in range(1, 6):
        print(f"Thread {threading.current_thread().name} - Number: {i}")
        time.sleep(1)  # Simulate some time-consuming task

# Create two threads
thread1 = threading.Thread(target=print_numbers, name="Thread 1")
thread2 = threading.Thread(target=print_numbers, name="Thread 2")

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Multithreading example completed.")


import requests
import multiprocessing

# Function to make API requests
def test_api(val):
    val = val
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    try:
        response = requests.get(url)
        print(f"URL: {url}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"URL: {url}, Exception: {val}")

if __name__ == "__main__":
    # List of API endpoints to test
    api_endpoints = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        # Add more API endpoints as needed
    ]

    # Create a pool of worker processes (number of processes is set to 4)
    pool = multiprocessing.Pool(processes=4)

    # Use the pool to map the API endpoints to the test_api function
    # This will execute the function concurrently for each endpoint
    pool.map(test_api, range(49))


    # Close the pool and wait for the worker processes to complete
    pool.close()
    pool.join()

    print("API testing completed.")
