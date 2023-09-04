
pip install ecdsa


from ecdsa import SigningKey
private_key = SigningKey.generate() # uses NIST192p
signature = private_key.sign(b"Educative authorizes this shot")
print(signature)
public_key = private_key.verifying_key
print("Verified:", public_key.verify(signature, b"Educative authorizes this shot"))


https://www.educative.io/answers/how-to-verify-digital-signature-in-python-using-ecdsa-signingkey



RSA : 
# https://www.youtube.com/watch?v=txz8wYLITGk
https://pypi.org/project/rsa-python/
pip install rsa
pip install python_rsa

from rsa_python import rsa
key_pair = rsa.generate_key_pair(1024)
cipher = rsa.encrypt("Hello World!", key_pair["public"], key_pair["modulus"])
decrypted_message = rsa.decrypt(cipher, key_pair["private"], key_pair["modulus"])
print(decrypted_message)



# https://www.section.io/engineering-education/rsa-encryption-and-decryption-in-python/


