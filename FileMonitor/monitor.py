import hashlib
import json
import os
import sys


def hash_file(file_path):

    with open(file_path, "rb") as f:
        data = f.read()

    hash = hashlib.sha256(data).hexdigest()

    return hash


def create_baseline(folder):
    hashes = {}
    for filename in os.listdir(folder):

        full_path = folder + "/" + filename

        if os.path.isfile(full_path):
            file_hash = hash_file(full_path)
            hashes[filename] = file_hash

    with open("hashes.json", "w") as f:
        json.dump(hashes, f)

    return hashes


def check_integrity(folder):

    with open("hashes.json", "r") as f:
        baseline = json.load(f)

    tampered = []

    for filename, old_hash in baseline.items():
        new_hash = hash_file(folder + "/" + filename)
        if new_hash != old_hash:
            tampered.append(filename)

    return tampered


def main():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = "test_folder"

    if "baseline" in sys.argv:
        create_baseline(folder)
        print("Baseline saved")
    else:
        tampered = check_integrity(folder)
        if tampered:
            print("ALERT")
        else:
            print("OK")


if __name__ == "__main__":
    main()
