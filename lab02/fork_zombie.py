import os
import sys
import time


def main():
    print(f"[Parent] My PID is {os.getpid()}", flush=True)
    print("[Parent] Forking a child process...", flush=True)
    pid = os.fork()
    if pid > 0:
        print(f"[Parent] Created Child with PID {pid}.", flush=True)
        print("[Parent] Open htop and look for the child's Z state.", flush=True)
        time.sleep(60)
        print("[Parent] Waking up and exiting.")
    else:
        print(f"[Child] My PID is {os.getpid()}. I am finishing quickly!", flush=True)
        sys.exit(0)


if __name__ == "__main__":
    main()
