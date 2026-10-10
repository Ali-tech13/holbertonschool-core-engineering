#!/usr/bin/env python3
"""Module for reading a UTF-8 text file."""


def read_file(filename=""):
    """Read and print the contents of a text file."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
