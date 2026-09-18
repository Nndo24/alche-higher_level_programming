#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file and returns char count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
