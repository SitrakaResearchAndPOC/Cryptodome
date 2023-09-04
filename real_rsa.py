from rsa_python import rsa
key_pair = rsa.generate_key_pair(1024)
cipher = rsa.encrypt("Hello World!", key_pair["public"], key_pair["modulus"])
decrypted_message = rsa.decrypt(cipher, key_pair["private"], key_pair["modulus"])
print(decrypted_message)
