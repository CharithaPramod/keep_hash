import hashlib
import os

# Define a whitelist of known file hashes (example hashes)
    # can exract hashes from https://www.virustotal.com/gui/home/upload
    # will use virustotal in future
whitelisted_hashes = {
    'C:\\Windows\\System32\\notepad.exe': '45d494d6578e5b0b147ea654e9608db5',
    'C:\\Windows\\System32\\calc.exe': '2e88a9f06b2f9f01c10e9a875407dc9d',
    # Add more file paths and their corresponding hashes as needed
}

def calculate_hash(file_path, hash_algorithm='sha256'):
    try:
        hasher = hashlib.new(hash_algorithm)

        with open(file_path, 'rb') as file:
            while True:
                data = file.read(65536)  # Read in 64k chunks
                if not data:
                    break
                hasher.update(data)

        return hasher.hexdigest()

    except Exception as e:
        # Handle any exceptions that may occur during hashing
        print(f"Error calculating hash: {str(e)}")

    return None

def is_whitelisted_hash(file_path):
    try:
        normalized_file_path = os.path.normpath(file_path)
        if normalized_file_path in whitelisted_hashes:
            return True

        # Calculate the hash of the file
        file_hash = calculate_hash(normalized_file_path)

        # Check if the calculated hash matches a whitelisted hash
        if file_hash and file_hash == whitelisted_hashes.get(normalized_file_path):
            return True

    except Exception as e:
        # Handle any exceptions that may occur during hash calculation or comparison
        print(f"Error checking file hash: {str(e)}")

    return False

# Example usage:
file_path = 'C:\\Windows\\System32\\notepad.exe'
if is_whitelisted_hash(file_path):
    print(f"'{file_path}' is a whitelisted file.")
else:
    print(f"'{file_path}' is not a whitelisted file.")
