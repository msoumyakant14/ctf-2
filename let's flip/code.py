from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
iv = get_random_bytes(16)

flag = open('flag','rb').read().strip()

def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    enc = cipher.encrypt(pad(data,16,style='pkcs7'))
    return enc.encode('hex')

def decrypt_data(encryptedParams):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    paddedParams = cipher.decrypt(encryptedParams.decode('hex'))
    return unpad(paddedParams,16,style='pkcs7')

msg = "admin=0"
print("Current Auth Message is : " + msg)
print("Encryption of auth Message in hex : " + iv.encode('hex') + encrypt_data(msg))
enc_msg = raw_input("Give me the encypted message (in hex) to get the flag")
try:
    final_dec_msg = decrypt_data(enc_msg)

    if "admin=1" in final_dec_msg:
        print('Whoa!! you got it!! Now its reward time!!')
        print(flag)
    else:
        print('keep trying')
        exit()
except:
    print('Try Again!!')
