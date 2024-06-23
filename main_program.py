import threading
import hashlib
import math
import os


def work_out_sha_256(text_str: str) -> str:
    return hashlib.sha256(text_str.encode("utf-8")).hexdigest()


class Storage:
    def __init__(self, total_file_size_GB: int):
        print("Storing data in memory")

        data = "".join(
            str(x % 10) for x in range(1024**3)
        )  # make 1 GB of size in memory

        data_sha256 = work_out_sha_256(data)

        for file_part in range(math.ceil(total_file_size_GB)):
            print(f"Making file {file_part + 1}")
            with open(f"{file_part}.jhoot", "w") as file:
                _ = file.write(data)

            print("    Verifying produced file is correct")
            with open(f"{file_part}.jhoot", "r") as file:
                new_sha256 = work_out_sha_256(file.read().strip())
                if new_sha256 != data_sha256:
                    print("ERROR - SHA256 DOES NOT MATCH")
                    print(f"{new_sha256}, WHEN EXPECTED {data_sha256}")
                    print(
                        "DATA CORRUPTION HAS OCCURED, POSSIBLY INDICATING FAULTY DRIVE"
                    )
                    choice = input("CONTINUE ANYWAYS? (Y/n)").lower()
                    if choice == "n":
                        return


def main() -> None:
    files = Storage(total_file_size_GB=int(input("How many Gigabytes to test:")))


if __name__ == "__main__":
    main()
    # print(work_out_sha_256("hello"))
