# FileSentinel - File Integrity Monitor

Junior SOC Analyst project. Detects if attacker changed a file by comparing hashes.

## What it does

Hashes files with SHA256, saves baseline, later re-hashes and alerts if file changed.

Think like SOC: Attacker changes config or log, defender detects change by hash.

## Files

- monitor.py - Monitor code
- README.md - This file
- hashes.json - Created when you run baseline, stores clean hashes

## How to run

python3 monitor.py test_folder baseline
python3 monitor.py test_folder check

## Tests

mkdir -p test_folder
echo "hello" > test_folder/file1.txt
python3 monitor.py test_folder baseline
python3 monitor.py test_folder check

# Should print OK

echo "hacked" > test_folder/file1.txt
python3 monitor.py test_folder check

# Should print ALERT

## How it works

- hash_file(file_path) - Open file in rb, read bytes, hashlib.sha256(data).hexdigest(), return hash
- create_baseline(folder) - Loop os.listdir, if isfile, hash_file, save hashes[filename] = file_hash, json.dump to hashes.json
- check_integrity(folder) - json.load baseline, re-hash each file, if new_hash != old_hash, add to tampered, return tampered
- main() - Get folder from sys.argv, if "baseline" in sys.argv call create_baseline else call check_integrity, if tampered print ALERT else OK

## Skills

Python, Hashing SHA256, JSON, File I/O, SOC integrity monitoring
