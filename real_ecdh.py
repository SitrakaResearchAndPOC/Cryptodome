from tinyec import registry
import secrets

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

alicePrivKey = secrets.randbelow(curve.field.n)
alicePubKey = alicePrivKey * curve.g
alicePubKey2 = curve.g
alicePubKey2.x = alicePubKey.x
alicePubKey2.y = alicePubKey.y
 
print("Alice public key:", compress(alicePubKey))

bobPrivKey = secrets.randbelow(curve.field.n)
bobPubKey = bobPrivKey * curve.g
print("Bob public key:", compress(bobPubKey))

print("Now exchange the public keys (e.g. through Internet)")

aliceSharedKey = alicePrivKey * bobPubKey
print("Alice shared key:", compress(aliceSharedKey))


bobSharedKey = bobPrivKey * alicePubKey
print("Bob shared key:", compress(bobSharedKey))


bobSharedKey2 = bobPrivKey * alicePubKey2
print("Bob shared key 2:", compress(bobSharedKey2))

print("Equal shared keys:", aliceSharedKey == bobSharedKey)

