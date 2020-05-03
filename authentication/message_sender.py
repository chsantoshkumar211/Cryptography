import hmac
import hashlib

#message
message='Santosh'
enc_msg=''
key='2112000'
for i in range(len(message)):
    enc_msg+=chr(ord(message[i])^ord(key[i%len(key)]))
print(enc_msg)

#Integrity check
message=bytes(message.encode('utf-8'))
hash_of_msg=hashlib.sha512(message).hexdigest()
print(hash_of_msg)

#Authentication
key=b'2112000'
hexdigest = hmac.new(key,message,hashlib.sha1).hexdigest()
print(hexdigest)

#final_message to transmit
final_message = {
    "Message"         : message,
    "sha512"          : hash_of_msg,
    "Authentication"  : hexdigest
}