import hashlib

def crack_sha1_hash(hash, use_salts = False):
    # list of salts
    try:
        with open("known-salts.txt", "r", encoding="utf-8") as file:
            salt_list = file.read().splitlines()
    except FileNotFoundError:
        print("Error: The file 'data.txt' was not found.")

    # list of password database
    try:
        with open("top-10000-passwords.txt", "r", encoding="utf-8") as file:
            psw_list = file.read().splitlines()
    except FileNotFoundError:
        print("Error: The file 'data.txt' was not found.")

    if use_salts == False:
        for psw in psw_list:
            psw_hash = hashlib.sha1(psw.encode('utf-8'))
            if psw_hash.hexdigest() == hash:
                return psw
                break
        return "PASSWORD NOT IN DATABASE"

    else:
        for psw in psw_list:
            for salt in salt_list:
                psw_hash = hashlib.sha1((psw+salt).encode('utf-8'))
                if psw_hash.hexdigest() == hash:
                    return psw
                    break
                psw_hash = hashlib.sha1((salt+psw).encode('utf-8'))
                if psw_hash.hexdigest() == hash:
                    return psw
                    break

    return "PASSWORD NOT IN DATABASE"

# usage
# print(f"password: {crack_sha1_hash("80540a46a2c1a0eae58d9868f01c32bdcec9a010")}") # 01071988
# print(f"password: {crack_sha1_hash("18c28604dd31094a8d69dae60f1bcd347f1afc5a")}") # superman
# print(f"password: {crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True)}") # superman
# print(f"password: {crack_sha1_hash("da5a4e8cf89539e66097acd2f8af128acae2f8ae", use_salts=True)}") # q1w2e3r4t5
