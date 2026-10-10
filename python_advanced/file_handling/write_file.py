
#!/usr/bin/env python3
"""Write a string to a UTF-8 text file."""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
