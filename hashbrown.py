import hashlib
import os
import argparse

def calculate_file_hash(file_path, algorithm):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None
    
    try:
        hash_func = getattr(hashlib, algorithm)
        hash_obj = hash_func()
    except AttributeError:
        print(f"Error: Unsupported algorithm '{algorithm}'")
        return None
    
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        print(f"Error: An error occured while reading the file. {e}")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the hash of the file.")
    parser.add_argument("file_path", help="The path to the file to hash.")
    parser.add_argument("algorithm", help="The hash algorithm to use (e.g., 'md5', 'sha1', 'sha256', etc.).")

    args = parser.parse_args()

    hash_value = calculate_file_hash(args.file_path, args.algorithm)
    if hash_value:
        print(f"The {args.algorithm} hash of the file {args.file_path} is: {hash_value}")