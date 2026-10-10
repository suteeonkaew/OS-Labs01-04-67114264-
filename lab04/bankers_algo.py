import numpy as np


total_resources = np.array([10, 5, 7])
max_need = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2]])
allocated = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2]])


def is_safe_state(available, maximum, current_allocation):
    number_of_jobs = len(current_allocation)
    work = available.copy()
    finish = [False] * number_of_jobs
    safe_sequence = []
    need = maximum - current_allocation
    while len(safe_sequence) < number_of_jobs:
        progressed = False
        for job in range(number_of_jobs):
            if not finish[job] and np.all(need[job] <= work):
                work += current_allocation[job]
                finish[job] = True
                safe_sequence.append(f"Job_{job}")
                progressed = True
        if not progressed:
            return False, []
    return True, safe_sequence


def main():
    print("--- OS Scheduler: Banker's Algorithm Check ---")
    available = total_resources - np.sum(allocated, axis=0)
    need = max_need - allocated
    print(f"Currently Available Resources: {available}")
    print(f"Need Matrix:\n{need}")
    safe, sequence = is_safe_state(available, max_need, allocated)
    if safe:
        print(f">> SYSTEM IS SAFE. Execution Sequence: {' -> '.join(sequence)}")
    else:
        print(">> WARNING: SYSTEM IS UNSAFE. Request denied.")


if __name__ == "__main__":
    main()
