import hashlib
 
def create_hash(hash_option, file):
    try:
        if hash_option == "1":
            return hashlib.sha1(open(file, "rb").read()).hexdigest()
        elif hash_option == "2":
            return hashlib.sha256(open(file, "rb").read()).hexdigest()
        elif hash_option == "3":
            return hashlib.sha512(open(file, "rb").read()).hexdigest()
        elif hash_option == "4":
            return hashlib.md5(open(file, "rb").read()).hexdigest()
        return "Ivalid option"
    except Exception:
        return "File not found"

user_option = input("""
***********************************************
Choose a hash algorithm:
[1] SHA1
[2] SHA256
[2] SHA512
[4] MD5 
***********************************************
""")

file = input("Choose a file: ")
print(create_hash(user_option, file))
