setxkbmap fr
apt update
sudo su
apt-get install python3-pip
pip3 install progressbar
pip3 uninstall numpy
pip3 install "numpy<1.20.0"
pip3 install click
pip3 install progress
pip3 install sympy

git clone https://github.com/Krijn-math/Constant-time-CSURF-CRADS
cd Constant-time-CSURF-CRADS/


python3 main.py --help
python3 main.py -p p512  -m unscaled -s wd2 -v -a csidh -e 5
python3 main.py -p p512  -m unscaled -s wd1 -v -a csidh -e 10
python3 main.py -p p512  -m scaled -s wd2 -v -a csidh -e 5
python3 main.py -p p512  -m unscaled -s wd2 -v -a csurf -e 5

cd ..

______________________________________________________________________
sudo apt install -y dh-python python3-click python3-progress  python3-numpy python3-matplotlib python3-networkx   python3-stdeb python3-setuptools-scm python3-setuptools python3-cpuinfo
pip3 install dh click numpy progress matplotlib networkx stdeb setuptools-scm setuptools
sudo apt-get install python-all

INSTALLATION BY SOURCE : 
git clone https://github.com/JJChiDguez/sibc
cd sibc
python3 setup.py bdist_deb
sudo python3 setup.py install

python3 sibc csidh-bench
python3 sibc -p p512 -f hvelu -a csidh -s df -e 10 csidh-main

sibc -p p512 -f hvelu -a csidh -s df -e 10 csidh-main


INSTALLATION BY APT : 
sudo pip3 install sibc
sibc -p p512 -f hvelu -a csidh -s df -e 10 csidh-main


TEST

python3 real_csidh.py 
cd ..
_________________________________________________________________________
git clone https://github.com/suhrikim/HuffCSIDH.git
cd HuffCSIDH/
cd HuffCSIDH/
make BITS=512
./main 
clear

cd ..
cd ..

git clone https://github.com/suhrikim/MontMinus.git
cd MontMinus/
cd CSURF_mm/
./main 
clear

DANS MAIN : gedit main.c
   test_csidh();
   test_Hybrid();
   test_Huff();
   test_Hybrid_sqrt();

   test_Huff_sqrt_opt();

   test_Huff_edwards();
   test_Huff_sqrt_edwards();
   
   ================
    test_csidh();
    test_csidh_hy();
    test_csurf();
    test_hybrid_sqrt();
    test_csurf_sqrt();
    test_csurf_rad3_sqrt();


cd ..
cd ..
_________________________________________________________________________
Installing DH : 
https://cryptobook.nakov.com/key-exchange/dhke-examples

pip3 install -U PyCryptodome
pip install pyDHE

python3 real_dh.py 

_________________________________________________________________________
Installing ECDH : 
https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/asymmetric-key-ciphers/ecc-encryption-decryption.html
https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/asymmetric-key-ciphers/ecdh-key-exchange.html

pip install tinyec

python3 real_ecdh.py 



webographie : 
https://github.com/JJChiDguez/sibc
https://isogenyschool2020.co.uk/schedule/is_FRH.pdf
https://github.com/Krijn-math/Constant-time-CSURF-CRADS
clone https://github.com/suhrikim/HuffCSIDH.git
clone https://github.com/suhrikim/MontMinus.git


    

