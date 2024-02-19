from sibc.csidh import CSIDH, default_parameters
import sys
import os
import binascii

def help() :
    print("help")
    print("python3 shared_csidh_sibc.py -p <pub_file.pub> -s <priv_file.priv> -k  <shared_file.key>")
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
            
    csidh = CSIDH(**default_parameters)
    public_key= binascii.unhexlify(inf_pub)
    secret_key = binascii.unhexlify(inf_priv)
    shared_secret = csidh.dh(secret_key, public_key)
    print("shared key")
    print(shared_secret.hex())	
    key = shared_secret.hex()	
    # save shared key
    with open(shared_file, 'wb') as f:
        f.write(str(key).encode())



if __name__ == '__main__':
    main()

