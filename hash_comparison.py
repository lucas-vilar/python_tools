import sys
import hashlib

def hash_comparison(file1, file2):
    hash1 = hashlib.new("sha1")
    hash2 = hashlib.new("sha1")
    try:
        hash1.update(open(file1, "rb").read())
        hash2.update(open(file2, "rb").read())
    except:
        return "There was an error opening the files. Did you write the names correctly?"

    if hash1.digest() != hash2.digest():
        return f"{file1} and {file2} have different hashes!"
    return f"{file1} and {file2} have the same hash!"

print(hash_comparison(sys.argv[1], sys.argv[2]))