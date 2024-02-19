from tinyec import registry
import secrets

import sys
import os.path
import binascii

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

def demo():
    # key exchange 
    curve = registry.get_curve('brainpoolP256r1')

    alicePrivKey = secrets.randbelow(curve.field.n)
    alicePubKey = alicePrivKey * curve.g
    #alicePubKey2 = curve.g
    #alicePubKey2.x = alicePubKey.x
    #alicePubKey2.y = alicePubKey.y

    #print("alicePubKey2", alicePubKey2)
    #print("Alice priv key:", alicePrivKey)
    #print("Type Alice priv key:", type(alicePrivKey))
 
    print("Alice public key:", compress(alicePubKey))

    bobPrivKey = secrets.randbelow(curve.field.n)
    bobPubKey = bobPrivKey * curve.g
    print("Bob public key:", compress(bobPubKey))
    #print("Type Bob public key x :", type(bobPubKey.x))
    
    print("Now exchange the public keys (e.g. through Internet)")

    aliceSharedKey = alicePrivKey * bobPubKey
    print("Alice shared key:", compress(aliceSharedKey))


    bobSharedKey = bobPrivKey * alicePubKey
    print("Bob shared key:", compress(bobSharedKey))


    #bobSharedKey2 = bobPrivKey * alicePubKey2
    #print("Bob shared key 2:", compress(bobSharedKey2))

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
        curve = registry.get_curve('brainpoolP256r1')

        PrivKey = secrets.randbelow(curve.field.n)
        PubKey = PrivKey * curve.g
        

        name_file = sys.argv[2]
        pub_file = name_file + ".pub"
        priv_file = name_file + ".priv"
        # SAVING KEY
        public_key_hex = format(PubKey.x, 'x')+format(PubKey.y,'x')
        with open(pub_file, 'wb') as f:
            f.write(str("0x").encode()+str(public_key_hex).encode())


        secret_key_hex = hex(PrivKey)
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

