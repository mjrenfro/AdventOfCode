import hashlib

#the provided door id
doorID='ugkcyxxp'
index =0
password=['*']*8 #hexidecimal encoded chars only contain [a-fA-F0-9]
while '*' in password:
    seed=doorID+str(index)
    hashed=hashlib.md5(seed.encode('utf-8')).hexdigest()
    try:
        if hashed.startswith('00000') and password[int(hashed[5])] =='*':
            password[int(hashed[5])]=hashed[6]
            #optional loading presentation
            print ("".join(password))
    except (ValueError, IndexError):
        pass
    index+=1
print("".join(password))
