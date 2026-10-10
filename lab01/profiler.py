import platform

import psutil


def main():
    memory = psutil.virtual_memory()
    print(f"OS Name: {platform.system()} {platform.release()}")
    print(f"Number of CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"Total RAM: {memory.total / (1024**3):.2f} GB")


if __name__ == "__main__":
    main()
