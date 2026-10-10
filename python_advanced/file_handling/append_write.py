#!/usr/bin/env python3
"""Module for appending to a UTF-8 text file."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
