# Cryptodome
* OS : Tested Ubuntu focal (20.04)

## Installing Dependecies
```
apt update
```
```
apt-get install python3-pip wget
```
```
mkdir SRC
```
```
cd SRC
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

## PostQuantum Cryptography
```
apt-get install python3-pip
```
```
pip3 install progressbar
```
```
pip3 uninstall numpy
```
```
pip3 install "numpy<1.20.0"
```
```
pip3 install click
```
```
pip3 install progress
```
```
pip3 install sympy
```
```
apt-get install git
```
```
git clone https://github.com/Krijn-math/Constant-time-CSURF-CRADS
```
```
cd Constant-time-CSURF-CRADS/
```
```
python3 main.py --help
```
```
python3 main.py -p p512  -m unscaled -s wd2 -v -a csidh -e 5
```
```
python3 main.py -p p512  -m unscaled -s wd1 -v -a csidh -e 10
```
```
python3 main.py -p p512  -m scaled -s wd2 -v -a csidh -e 5
```
```
python3 main.py -p p512  -m unscaled -s wd2 -v -a csurf -e 5
```
```
cd ..
```
```
sudo apt install -y dh-python python3-click python3-progress  python3-numpy python3-matplotlib python3-networkx   python3-stdeb python3-setuptools-scm python3-setuptools python3-cpuinfo
pip3 install dh click numpy progress matplotlib networkx stdeb setuptools-scm setuptools
```
```
sudo apt-get install python-all
```
## SIBC API for Isogenies
* INSTALLATION BY SOURCE
``` 
git clone https://github.com/JJChiDguez/sibc
```
```
cd sibc
```
```
python3 setup.py bdist_deb
```
```
sudo python3 setup.py install
```
```
python3 sibc csidh-bench
```
```
python3 sibc -p p512 -f hvelu -a csidh -s df -e 10 csidh-main
```
```
sibc -p p512 -f hvelu -a csidh -s df -e 10 csidh-main
```

* INSTALLATION BY APT 
```
sudo pip3 install sibc
```
```
cd ..
```
```
sibc -p p512 -f hvelu -a csidh -s df -e 10 csidh-main
```
```
wget https://github.com/SitrakaResearchAndPOC/Cryptodome/blob/main/real_csidh.py
```
```
python3 real_csidh.py 
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

