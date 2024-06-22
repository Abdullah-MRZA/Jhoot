# import asyncio
import threading


class Storage:
    def __init__(self):
        self.make_4GB_file()
        self.verify_4GB_file()

    def make_4GB_file(self): ...

    def verify_4GB_file(self): ...


def main() -> None: ...


if __name__ == "__main__":
    # asyncio.run(main())
    main()
