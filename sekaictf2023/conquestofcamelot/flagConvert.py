import hashlib

correct_flag = "SEKAI{n3ur4l_N3T_313c7R0n_C0mbO_uwu}"
correct_flag_hash = hashlib.sha256(correct_flag.encode()).hexdigest()
print(correct_flag_hash)

