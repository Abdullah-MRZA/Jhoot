# Jhoot
A program to determine if your USB/SD card or other storage device has the capacity you think it does

A simple program to determine if a storage medium has the storage capacity that it claims to have...

## Features

- Single file, easy to carry around
- Custom fragmentation, so that any partitioning method can be checked
- ~~doesn't require any external dependencies (other than python)~~ Added a dependancy for better viewing of how many tasks left
- ~~Multithreaded, meaning your drive can work at its full capacity (for a faster test)~~ Single threaded is fast *enough*


If you have any ideas for extending the functionality of this program, get in touch!

## How it works

Enter how many gigabytes you want to check.
The program will then create those files, and check if they are corrupt.

If they are corrupt, it will halt, and notify you that, and give you an option to continue, or terminate the program.

At the end, you can see how many files were corrupted, and how many were preserved

The program then runs a final test of the data, and prints the result of this as well.

## What information can this tell me?

Some USB/SD cards fake their storage, so this program makes sure that they store exactly what they say they do.

There should not be any corruption whatsoever, so any corrupted files may be a sign that you need to investigate...
