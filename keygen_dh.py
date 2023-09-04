import pyDHE
import sys
import os.path
import binascii

def demo():
    # key exchange 
    # https://github.com/deadPix3l/pyDHE/blob/master/lib/pyDHE/__init__.py
    # OTHER : https://github.com/lowazo/pyDHE/blob/master/DiffieHellman.py
    # https://github.com/lowazo/pyDHE/blob/master/DiffieHellman.pyyts.torrentbay.to 
    # https://dev.to/codesphere/basics-of-encryption-the-diffie-hellman-key-exchange-explained-3a1c
    # https://codeahoy.com/learn/practicalcryptography/toc/
    # https://www.section.io/engineering-education/diffie-hellman-elgamal/
    # https://medium.com/@aseemchopra/practical-cryptography-part-vii-45c187e23a8f
    # https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/key-exchange/dhke-examples.html
    # https://www.thesecuritybuddy.com/cryptography-and-python/diffie-hellman-key-exchange-protocol-using-the-pydhe-python-library/
    # https://medium.com/@aseemchopra/practical-cryptography-part-vii-45c187e23a8f
    # https://github.com/deadPix3l/pyDHE/blob/master/lib/pyDHE/__init__.py
    
    alice = pyDHE.new()
    print("secret key alice")
    print(alice)
    alicePubKey = alice.getPublicKey()
    print("Alice public key:", hex(alicePubKey))
    #print("alice get secret key : ", alice.a)

    bob = pyDHE.new()
    bobPubKey = bob.getPublicKey()
    print("Bob public key:", hex(bobPubKey))

    print("Now exchange the public keys (e.g. through Internet)")

    aliceSharedKey = alice.update(bobPubKey)
    print("Alice shared key:", hex(aliceSharedKey))

    bobSharedKey = bob.update(alicePubKey)
    print("Bob shared key:", hex(bobSharedKey))

    print("Equal shared keys:", aliceSharedKey == bobSharedKey)


def help() :
    print("help")
    print("python3 keygen_sibc_csidh.py -demo")
    print("python3 keygen_sibc_csidh.py -n <name>")
    print("-n <name> : name of public and private generated key")
    sys.exit()

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-demo':
        demo()

    if len(sys.argv) < 2:
        help()
        sys.exit()

    if(len(sys.argv)  > 1 and sys.argv[1] == "-n") : 
        print("option n")
        dh = pyDHE.new()
        
        public_key = dh.getPublicKey()

        name_file = sys.argv[2]
        pub_file = name_file + ".pub"
        priv_file = name_file + ".priv"
        # SAVING KEY
        public_key_hex = hex(public_key)
        with open(pub_file, 'wb') as f:
            f.write(str(public_key_hex).encode())


        secret_key_hex = hex(dh.a)
        with open(priv_file, 'wb') as f:
            f.write(str(secret_key_hex).encode())
            
        # GETTING KEY        
        #try:
        #    with open("test_publicfile.pub", 'rb') as f:
        #        inf2 = f.read()
        #except :
        #    print ("Error while trying to read input file.")
        #    sys.exit()
        #public_key_translate = int(inf2, base=16)      



    else : 
        help()
    
if __name__ == '__main__':
    main()


#print(alice_secret_key)
#print(alice_public_key)

