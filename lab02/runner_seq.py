import time

from task import process_image


def main():
    num_images = 16
    print(f"--- Starting Sequential Processing for {num_images} images ---")
    start_time = time.perf_counter()
    for image_id in range(num_images):
        process_image(image_id)
    elapsed = time.perf_counter() - start_time
    print(f"Total Time (Sequential): {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
