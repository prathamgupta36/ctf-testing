import hashlib

correct_flag = "FLAG"
correct_flag_hash = hashlib.sha256(correct_flag.encode()).hexdigest()
print(correct_flag_hash)

