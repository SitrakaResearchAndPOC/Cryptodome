import pyDHE
import sys
import os
import binascii

def help() :
    print("help")
    print("python3 shared_dh.py -p <pub_file.pub> -s <priv_file.priv> -k  <shared_file.key>")
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
            
    dh = pyDHE.new()
    public_key = int(inf_pub, base=16)
    secret_key = int(inf_priv, base=16)
    # alice part
    dh.a = secret_key
    dh.public = pow(dh.g, dh.a, dh.p)
    dh.key = 0
    
    # bob part
    shared_secret = dh.update(public_key)

    print("shared key")
    print(hex(shared_secret))	
    # format instead of hex
    # https://java2blog.com/print-hex-without-0x-python/
    key = format(shared_secret, 'x')	
    # save shared key
    with open(shared_file, 'wb') as f:
        f.write(str(key).encode())



if __name__ == '__main__':
    main()

