import hashlib

correct_flag = "actf{look1ng_f0r_answers_in_the_p0uring_r4in_b21f9732f829}"
correct_flag_hash = hashlib.sha256(correct_flag.encode()).hexdigest()
print(correct_flag_hash)

