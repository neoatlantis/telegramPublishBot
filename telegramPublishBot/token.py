#!/usr/bin/env python3

import nacl.signing
import base64

__VERIFY_KEY_CACHE = {}
__SIGNING_KEY_CACHE = {}


class Base32Encoder:
    
    @staticmethod
    def encode(data):
        return base64.b32encode(data).decode("ascii").lower()

    @staticmethod
    def decode(data):
        return base64.b32decode(data.upper())

def newToken():
    privateKey = nacl.signing.SigningKey.generate()
    publicKey = privateKey.verify_key
    tostr = lambda i: i.encode(encoder=Base32Encoder).rstrip("=")
    return {
        "public": "pub:" + tostr(publicKey),
        "private": "prv:" + tostr(privateKey)
    }

def derivePublicToken(privateKey):
    assert type(privateKey) == str and privateKey.startswith("prv:")
    privateKey = (privateKey[4:] + "====")
    key = nacl.signing.SigningKey(privateKey, encoder=Base32Encoder)
    publicKey = key.verify_key
    return "pub:" + publicKey.encode(encoder=Base32Encoder).rstrip("=")
    

def sign(privateKey, data):
    global __SIGNING_KEY_CACHE
    assert type(data) == bytes and type(privateKey) == str
    if privateKey in __SIGNING_KEY_CACHE:
        key = __SIGNING_KEY_CACHE[privateKey]
    else:
        try:
            assert privateKey.startswith("prv:")
            privateKey = (privateKey[4:] + "====")
            key = nacl.signing.SigningKey(privateKey, encoder=Base32Encoder)
            __SIGNING_KEY_CACHE[privateKey] = key
        except:
            raise Exception("Not a valid private key.")
    return bytes(key.sign(data))

def verify(publicKey, data):
    """Verify data against a public key. If ok, return verified data.
    Otherwise None."""
    global __VERIFY_KEY_CACHE
    assert type(data) == bytes and type(publicKey) == str
    if publicKey in __VERIFY_KEY_CACHE:
        key = __VERIFY_KEY_CACHE[publicKey]
    else:
        try:
            assert publicKey.startswith("pub:")
            publicKey = (publicKey[4:] + "====")
            key = nacl.signing.VerifyKey(publicKey, encoder=Base32Encoder)
            __VERIFY_KEY_CACHE[publicKey] = key
        except:
            raise Exception("Not a valid public key.")
    try:
        return key.verify(data)
    except:
        return None


if __name__ == "__main__":
    pair = newToken()
    pub = pair["public"]
    prv = pair["private"]

    print(verify(pub, sign(prv, b"hello")))
