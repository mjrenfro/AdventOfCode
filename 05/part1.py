import hashlib

#the provided door id 
doorID='ugkcyxxp'
index =0
password=''
while len(password)<8:
    seed=doorID+str(index)
    hashed=hashlib.md5(seed.encode('utf-8')).hexdigest()
    if hashed.startswith('00000'):
        password+=hashed[5]
        #optional loading presentation
        print ("------------------"+str(len(password))+"-----------------")
    index+=1
print(password)
