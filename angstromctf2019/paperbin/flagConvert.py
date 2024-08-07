import hashlib

correct_flag = "actf{proof by triviality}"
correct_flag_hash = hashlib.sha256(correct_flag.encode()).hexdigest()
print(correct_flag_hash)

