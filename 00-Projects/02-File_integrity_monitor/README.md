# File Integrity Monitor

Simple Python tool that detects changes in files using SHA256 hashing.

## Description

This project creates a hash of a file and checks if the file was modified.

If the file changes, the program detects it and shows an alert.

# Features

- Generate SHA256 hash
- Save file baseline
- Detect file modifications

# Technologies

- Python
- hashlib

# How it works

1. Program creates a SHA256 hash of the file
2. Hash is saved
3. Next scans compare the new hash with the old one
4. If hashes are different, the file was changed
