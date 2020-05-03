import hmac
import hashlib
#message received after transmission
reveived_message ={
    "Message"         : 'aP_F_CX',
    "sha512"         : 'eb974e37852e862817684379223158fc0c124182da76f4f85ab19b828488e3085db31e4395cde841f4e1e3752bedeaf0409e698a139788933e3fdddab5bd0529',
    "Authentication"  : 'c27c4fb50d124e33b349f8a1e5985e790623e0ea'
}
#decryption
enc_message=reveived_message["Message"]
key='2112000'
message=''
for i in range(len(enc_message)):
    message+=chr( ord(enc_message[i]) ^ ord(key[i%len(key)]) )
message=message.encode('utf-8')
#check the integrity
new_hash=hashlib.sha512(message).hexdigest()
if new_hash==reveived_message['sha512']:
    print("Integrity check : Passed")
else:
    print("Integrity check : Failed")

#Check Authenticity
key=b'2112000'
new_hash_digest=hmac.new(key,message,hashlib.sha1).hexdigest()
if new_hash_digest==reveived_message['Authentication']:
    print("Authentication : Passed")
else:
    print("Authentication : Failed")