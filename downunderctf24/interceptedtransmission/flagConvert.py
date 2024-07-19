import hashlib

correct_flag = "DUCTF{##TH3_QU0KK4'S_AR3_H3LD_1N_F4C1LITY_#11911!}"
correct_flag_hash = hashlib.sha256(correct_flag.encode()).hexdigest()
print(correct_flag_hash)

