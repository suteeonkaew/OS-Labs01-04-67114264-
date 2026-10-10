import threading
import time


shared_resource_lock = threading.Lock()
job_counts = {"Greedy_Model_A": 0, "Greedy_Model_B": 0, "Polite_Model": 0}
stop_event = threading.Event()


def greedy_task(name):
    while not stop_event.is_set():
        with shared_resource_lock:
            job_counts[name] += 1
        time.sleep(0.00001)


def polite_task(name):
    while not stop_event.is_set():
        time.sleep(0.01)
        with shared_resource_lock:
            job_counts[name] += 1


def main():
    print("--- Starting Cluster Starvation Simulation (3 seconds) ---")
    threads = [
        threading.Thread(target=greedy_task, args=("Greedy_Model_A",)),
        threading.Thread(target=greedy_task, args=("Greedy_Model_B",)),
        threading.Thread(target=polite_task, args=("Polite_Model",)),
    ]
    for thread in threads:
        thread.start()
    time.sleep(3.0)
    stop_event.set()
    for thread in threads:
        thread.join()
    print("\n--- Final Resource Acquisition Counts ---")
    for worker_name, count in job_counts.items():
        print(f"{worker_name}: {count} times")


if __name__ == "__main__":
    main()
