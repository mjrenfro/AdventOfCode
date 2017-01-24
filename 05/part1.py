import hashlib

password=''

doorID='ugkcyxxp'
index =0

def nextChar():
    global password
    global index
    #make possible new index and door id combo
    seed=doorID+str(index)
    hashed=hashlib.md5(seed.encode('utf-8')).hexdigest()
    if valid(hashed):
        password+=hashed[5]
        #optional loading presentation
        print ("------------------"+str(len(password))+"-----------------")

    index+=1

def valid(hashed):
        return hashed.startswith('00000')

def genPassword ():
    while len(password)<8:
        nextChar()
if __name__ == "__main__":
    genPassword()
    print (password)
