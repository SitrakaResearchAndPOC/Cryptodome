from sibc.csidh import CSIDH, default_parameters
import sys
import os.path
import binascii

def demo():
    csidh = CSIDH(**default_parameters)
    # alice generates a key
    alice_secret_key = csidh.secret_key()
    alice_public_key = csidh.public_key(alice_secret_key)
    # bob generates a key
    bob_secret_key = csidh.secret_key()
    bob_public_key = csidh.public_key(bob_secret_key)
    # if either alice or bob use their secret key with the other’s respective
    # public key, the resulting shared secrets are the same
    shared_secret_alice = csidh.dh(alice_secret_key, bob_public_key)
    shared_secret_bob = csidh.dh(bob_secret_key, alice_public_key)
    print("Bob shared key : "+shared_secret_bob.hex())
    print("Alice shared key : "+shared_secret_alice.hex())

    # Alice and bob produce an identical shared secret
    assert shared_secret_alice == shared_secret_bob
    print('ok')
    sys.exit()


def help() :
    print("help")
    print("python3 keygen_csidh_sibc -demo")
    print("python3 keygen_csidh_sibc -n <name>")
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
        csidh = CSIDH(**default_parameters)
        # generates a key
        secret_key = csidh.secret_key()
        public_key = csidh.public_key(secret_key)
        name_file = sys.argv[2]
        pub_file = name_file + ".pub"
        priv_file = name_file + ".priv"
        #print("pub_key")
        #print(public_key)
        #print("pub_key")
        #print(public_key.hex())

        #print("pub_key")
        #print(bytes.fromhex(public_key.hex()))
 
        #print("priv_key")
        #print(secret_key)
        #print(bytes.fromhex(hex_string))
       
        with open(pub_file, 'wb') as f:
            f.write(str(public_key.hex()).encode())

        with open(priv_file, 'wb') as f:
            f.write(str(secret_key.hex()).encode())
            
        # opening file for verification

        #try:
        #    with open(pub_file, 'rb') as f:
        #        inf = f.read()

        #except:
        #    print ("Error while trying to read input file.")
        #    sys.exit()
            
        #print("inf")
        #https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3
        #print(binascii.unhexlify(inf))
    else : 
        help()
    
if __name__ == '__main__':
    main()


#print(alice_secret_key)
#print(alice_public_key)

