import hashlib
import os
import sys

# SHA-56 hash of the correct flag (precomputed)
correct_flag_hash = '1e76068d47cff63a7afb2b17203e44f45df34f46ff3351a77673d90990dde68e'

def get_user_flag():
    return input("Enter the flag: ").strip()

def verify_flag(user_flag):
    # Compute SHA-256 hash of the user-provided flag
    user_flag_hash = hashlib.sha256(user_flag.encode()).hexdigest()
    return user_flag_hash == correct_flag_hash

def read_flag_file():
    with open('/flag', 'r') as f:
        return f.read()

def main():
    user_flag = get_user_flag()
    if verify_flag(user_flag):
        print("Correct flag!")
        print(read_flag_file())
    else:
        print("Incorrect flag.")

if __name__ == '__main__':
    main()
