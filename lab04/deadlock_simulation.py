import threading
import time


gpu_0_lock = threading.Lock()
gpu_1_lock = threading.Lock()


def train_model_a():
    print("[Model A] Waiting to acquire GPU 0...")
    gpu_0_lock.acquire()
    print("[Model A] Acquired GPU 0.")
    time.sleep(0.1)
    print("[Model A] Waiting to acquire GPU 1...")
    gpu_1_lock.acquire()
    print("[Model A] Acquired GPU 1.")
    gpu_1_lock.release()
    gpu_0_lock.release()


def train_model_b():
    print("[Model B] Waiting to acquire GPU 1...")
    gpu_1_lock.acquire()
    print("[Model B] Acquired GPU 1.")
    time.sleep(0.1)
    print("[Model B] Waiting to acquire GPU 0...")
    gpu_0_lock.acquire()
    print("[Model B] Acquired GPU 0.")
    gpu_0_lock.release()
    gpu_1_lock.release()


def main():
    print("--- Starting ML Training Cluster ---")
    thread_1 = threading.Thread(target=train_model_a)
    thread_2 = threading.Thread(target=train_model_b)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    print("--- Cluster Execution Completed ---")


if __name__ == "__main__":
    main()
