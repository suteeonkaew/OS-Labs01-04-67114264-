import threading
import time


gpu_0_lock = threading.Lock()
gpu_1_lock = threading.Lock()


def train_model(name):
    print(f"[{name}] Waiting for GPU 0...")
    with gpu_0_lock:
        print(f"[{name}] Got GPU 0. Processing...")
        time.sleep(0.1)
        print(f"[{name}] Waiting for GPU 1...")
        with gpu_1_lock:
            print(f"[{name}] Got GPU 1! Training complete.")


def main():
    print("--- Starting ML Training Cluster (Safe Mode) ---")
    thread_1 = threading.Thread(target=train_model, args=("Model A",))
    thread_2 = threading.Thread(target=train_model, args=("Model B",))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    print("--- Cluster Execution Completed Successfully ---")


if __name__ == "__main__":
    main()
