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
