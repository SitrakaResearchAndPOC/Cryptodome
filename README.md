# Cryptodome
* OS : Tested Ubuntu focal (20.04)

## Installing Dependecies
```
apt update
```
```
apt-get install python3-pip wget
```

##  TESTING DH
```
pip3 install -U PyCryptodome
```
```
pip install pyDHE
```
```
wget https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/real_dh.py
```
```
python3 real_dh.py 
```

## TESTING SEPARATE DH
```
wget https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/keygen_dh.py
```
```
wget  https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/shared_dh.py
```
```
python3 keygen_dh.py -n alice
```
```
ls
```
```
python3 keygen_dh.py -n bob
```
```
ls
```
```
python3 shared_dh.py -p alice.pub -s bob.priv -k key1.key
```
```
python3 shared_dh.py -p bob.pub -s alice.priv -k key2.key
```

## TESTING ECDH
```
pip install tinyec
```
```
wget https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/real_ecdh.py
```
```
python3 real_ecdh.py 
```
## TESTING SEPARATE ECDH

```
wget https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/keygen_ecdh.py
```
```
wget  https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/shared_ecdh.py
```
```
rm -rf *.pub
```
```
rm -rf *.priv
```
```
rm -rf *.key
```
```
python3 keygen_ecdh.py -n alice
```
```
ls
```
```
python3 keygen_ecdh.py -n bob
```
```
ls
```
```
python3 shared_ecdh.py -p alice.pub -s bob.priv -k key1.key
```
```
python3 shared_ecdh.py -p bob.pub -s alice.priv -k key2.key
```
## TESTING ECDSA
```
pip install ecdsa
```
```
wget  https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/real_ecdsa.py
```
```
python3 real_ecdsa.py
```

## TESTING RSA1
```
wget  https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/rsa1_main.py
```
```
python3 rsa1_main.py
```


## TESTING RSA2

```
wget  https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/rsa2_main.py
```
```
python3 rsa2_main.py
```

## TESTING RSA
```
pip install rsa
```
```
pip install rsa_python
```
```
wget  https://raw.githubusercontent.com/SitrakaResearchAndPOC/Cryptodome/main/real_rsa.py
```
```
python3 real_rsa.py
```



# Documentations
* https://cryptobook.nakov.com/key-exchange/dhke-examples
* https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/asymmetric-key-ciphers/ecc-encryption-decryption.html
* https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/asymmetric-key-ciphers/ecdh-key-exchange.html
* https://www.youtube.com/watch?v=txz8wYLITGk
* https://pypi.org/project/rsa-python/
* https://www.section.io/engineering-education/rsa-encryption-and-decryption-in-python/
* https://www.educative.io/answers/how-to-verify-digital-signature-in-python-using-ecdsa-signingkey
* https://github.com/Amaterazu7/rsa-python
* https://gist.github.com/marnix135/582c78891b29186ba4c6882a4bc62822

