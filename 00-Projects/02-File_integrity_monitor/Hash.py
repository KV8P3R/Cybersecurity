import hashlib

file = "text.txt"


with open(file, "rb") as f:
    data = f.read()

current_hash = hashlib.sha256(data).hexdigest()

try:
    old_hash = open("hash.txt", "r").read()

    if old_hash == current_hash:
        print("File is OK")

    else:
        print("File changed")

except:
    print("First scan - saving hash")

    with open("hash.txt", "w") as f:
        f.write(current_hash)

