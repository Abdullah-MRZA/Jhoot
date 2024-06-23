import hashlib
import string
from rich import print
from rich.progress import track
import math
# import random
# import threading
# import os


def work_out_sha_256(text_str: str) -> str:
    return hashlib.sha256(text_str.encode("utf-8")).hexdigest()


def storage_analysis(total_file_size_GB: int) -> None:
    print("Storing random data in memory...")

    # data = "".join(
    #     str(random.randint(0, 9)) for x in track(range(1024**3))
    # )  # make 1 GB of size in memory
    data = ((string.ascii_letters + string.digits) * 2)[:100] * ((1024**3) // 100)

    data_sha256 = work_out_sha_256(data)
    total_corrupted: int = 0

    print("Writing data to disk")
    for file_part in track(range(math.ceil(total_file_size_GB))):
        print(f"Making file {file_part + 1}")
        with open(f"{file_part}.jhoot", "w") as file:
            _ = file.write(data)

        print("    Verifying produced file is correct")
        with open(f"{file_part}.jhoot", "r") as file:
            new_sha256 = work_out_sha_256(file.read().strip())

            if new_sha256 != data_sha256:
                print("ERROR - SHA256 DOES NOT MATCH")
                print(f"{new_sha256}, WHEN EXPECTED {data_sha256}")
                print("DATA CORRUPTION HAS OCCURED, POSSIBLY INDICATING FAULTY DRIVE")
                choice = input("CONTINUE ANYWAYS? (Y/n)").lower()
                total_corrupted += 1
                if choice == "n":
                    return
    print(f"\nProgram completed, with {total_corrupted} corrupted files")


def main() -> None:
    storage_analysis(total_file_size_GB=int(input("How many Gigabytes to test:")))


if __name__ == "__main__":
    main()
    # print(work_out_sha_256("hello"))
