import os
import sys
import time


def main():
    print(f"[Parent] My PID is {os.getpid()}", flush=True)
    pid = os.fork()
    if pid > 0:
        print(f"[Parent] Waiting for Child PID {pid}.", flush=True)
        finished_pid, status = os.waitpid(pid, 0)
        print(f"[Parent] Reaped PID {finished_pid}; status={status}.")
    else:
        print(f"[Child] My PID is {os.getpid()}.", flush=True)
        time.sleep(1)
        sys.exit(0)


if __name__ == "__main__":
    main()
