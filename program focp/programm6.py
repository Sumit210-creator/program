def int_to_binary(n):
    if n <= 0:
        raise ValueError
    return bin(n)[2:] 


print(int_to_binary(10))  
print(int_to_binary(255))  

def find_factors(n):
    if n <= 0:
        raise ValueError
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors


print(find_factors(12))  
print(find_factors(17))  

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11)) 
print(is_prime(15))  

def encrypt_message(message):
    return message.replace(" ", "")[::-1]


print(encrypt_message("send cheese"))  

import random
import string

def random_encrypt(message):
    if not message:
        return "", 0
    
    interval = random.randint(2, 20)
    encrypted_message = []
    message_index = 0

    for i in range(len(message) + (len(message) - 1) // interval):
        if i % (interval + 1) == 0 and message_index < len(message):
            encrypted_message.append(message[message_index])
            message_index += 1
        else:
            encrypted_message.append(random.choice(string.ascii_lowercase))

    return ''.join(encrypted_message), interval

encrypted, interval = random_encrypt("send cheese")
print(f"Encrypted Message: {encrypted}, Interval: {interval}")

def decrypt_random_message(encrypted_message, interval):
    return ''.join(encrypted_message[i] for i in range(len(encrypted_message)) if i % (interval + 1) == 0)


decrypted_message = decrypt_random_message(encrypted, interval)
print(f"Decrypted Message: {decrypted_message}")
