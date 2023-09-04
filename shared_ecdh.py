from tinyec import registry
import secrets

import sys
import os
import binascii

def help() :
    print("help")
    print("python3 shared_ecdh.py -p <pub_file.pub> -s <priv_file.priv> -k  <shared_file.key>")
    print("-p <pub_file.pub>    : input public key")
    print("-s <priv_file.priv>  : input private key")
    print("-k <shared_file.key> : output shared calculated key")
    sys.exit()

def main():
    if len(sys.argv) < 6 :
        help()
        sys.exit()

    if(len(sys.argv)  > 1 and sys.argv[1] == "-p") : 
        pub_file = sys.argv[2]
        if os.path.exists(pub_file) != True : 
            help()
        try:
            with open(pub_file, 'rb') as f:
                inf_pub = f.read()

        except:
            print ("Error while trying to read input file.")
            sys.exit()

    if(len(sys.argv)  > 3 and sys.argv[3] == "-s") : 
        priv_file = sys.argv[4]
        if os.path.exists(priv_file) != True : 
            help()
        try:
            with open(priv_file, 'rb') as f:
                inf_priv = f.read()

        except:
            print ("Error while trying to read input file.")
            sys.exit()
            
    if(len(sys.argv)  > 5 and sys.argv[5] == "-k") : 
        shared_file = sys.argv[6]

    curve = registry.get_curve('brainpoolP256r1')

    PrivKey_alice = int(inf_priv, base=16)
    PubKey_bob =  curve.g

            
    #print("public_key ", PubKey_bob)
  
    #print("inf pub all", inf_pub)
    len_x = (len(inf_pub)-2)/2
    len_x +=2
    inf_pub_x = inf_pub[0:int(len_x)]
    inf_pub_y = inf_pub[int(len_x):]
    inf_pub_y = b'0x'+inf_pub_y
    PubKey_bob.x = int(inf_pub_x, base=16)
    PubKey_bob.y = int(inf_pub_y, base=16)

    #print("inf pub x", inf_pub_x)
    #print("inf pub y", inf_pub_y)
    
    secret_key = PrivKey_alice 
    shared_secret = secret_key * PubKey_bob
    print("shared key")
    print(hex(shared_secret.x)+hex(shared_secret.y))	
    # format instead of hex
    # https://java2blog.com/print-hex-without-0x-python/
    key = format(shared_secret.x, 'x')+format(shared_secret.y,'x')
    # save shared key
    with open(shared_file, 'wb') as f:
        f.write(str(key).encode())



if __name__ == '__main__':
    main()

