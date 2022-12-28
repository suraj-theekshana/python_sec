import os
import hashlib

def ransomware_detector(path):
  # Dictionary to store hashes of known good files
  known_good_hashes = {
    "file1.txt": "1234567890abcdef",
    "file2.txt": "0987654321fedcba"
  }

  # Dictionary to store hashes of suspect files
  suspect_hashes = {}

  # Iterate over all files in the specified directory
  for root, dirs, files in os.walk(path):
    for file in files:
      # Calculate the hash of the current file
      file_path = os.path.join(root, file)
      with open(file_path, "rb") as f:
        file_contents = f.read()
        file_hash = hashlib.sha256(file_contents).hexdigest()

      # Check if the file is in the known good hashes dictionary
      if file_hash in known_good_hashes.values():
        continue
      else:
        # If not, add it to the suspect hashes dictionary
        suspect_hashes[file] = file_hash

  # Return the suspect hashes dictionary
  return suspect_hashes

# Test the ransomware detector
suspect_hashes = ransomware_detector("C:\\Users\\example\\Documents")
print(suspect_hashes)
