### Contains functions to encrypt-decrypt string data
### Cipher used is AES


import random, secrets
from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import scrypt
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Hash import SHA256
from format import tobyte, tostr

# encrypts the msg
# key is derived based on passphrase
# input is string plaintext
# output is bytestring ciphertext
def encrypt(passphrase, pname, msg):
    salt = pad(pname.encode(), 32)
    key = scrypt(passphrase.encode(), salt, 32, 2**14, 8, 1)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(msg.encode(), AES.block_size))
    return (cipher.iv, ciphertext)

# encrypts the msg
# key is derived based on passphrase
# input is bytestring ciphertext
# output is string plaintext
def decrypt(passphrase, pname, iv, ciphertext):
    salt = pad(pname.encode(), 32)
    key = scrypt(passphrase.encode(), salt, 32, 2**14, 8, 1)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = (unpad(cipher.decrypt(ciphertext), AES.block_size)).decode()
    return plaintext

# generates a random passphrase
def randpass():
    with open('wordlist.txt', 'r') as f:
        l = f.readlines()
        return '-'.join(secrets.choice(l).split('\n')[0] for i in range(3))

# hashes using sha256 and returns bytestring digest
def shahash(string):
    hobj = SHA256.new(data=string.encode())
    return tostr(hobj.digest(), raw=True)


if __name__ == '__main__':
    ciphertext = encrypt('secret', 'my password', '123456')
    print(ciphertext[0])
    print(ciphertext[1])
    print()
    plaintext = decrypt('secret', 'my password', ciphertext[0], ciphertext[1])
    print(plaintext)
    ciphtext = encrypt('mediative-espresso-prefab-complice-stolid', 'username', 'notapassword')
    print(ciphtext[1])
    plaitext = decrypt('mediative-espresso-prefab-complice-stolid', 'username', ciphtext[0], ciphtext[1])
    print(plaitext)
    print()
    print(randpass())
    print(shahash('secret-pass-phrase'))
