import os
import time


def main():
    read_fd, write_fd = os.pipe()
    pid = os.fork()
    if pid > 0:
        os.close(write_fd)
        with os.fdopen(read_fd) as read_file:
            print(f"[Trainer PID:{os.getpid()}] Waiting for data...", flush=True)
            data = read_file.read()
        print(f"[Trainer PID:{os.getpid()}] Received Data: '{data}'")
        print(f"[Trainer PID:{os.getpid()}] Training complete.")
        os.waitpid(pid, 0)
    else:
        os.close(read_fd)
        with os.fdopen(write_fd, "w") as write_file:
            print(f" -> [DataLoader PID:{os.getpid()}] Loading image...", flush=True)
            time.sleep(2)
            image_data = "Image_Tensor_Batch_01"
            print(f" -> [DataLoader PID:{os.getpid()}] Sending data...", flush=True)
            write_file.write(image_data)


if __name__ == "__main__":
    main()
