from cryptography.fernet import Fernet

def gen_key(file_name):
    k=Fernet.generate_key()
    with open(file_name,"wb") as file:
        file.write(k)
#now to load the key
def load(file_name):
    with open(file_name, "rb") as file:
        return file.read()

def enc(file_tE):
    key=load(file_name)
    cipher=Fernet(key)
    with open(file_tE,"rb") as file:
        data=file.read()
        en=cipher.encrypt(data)
    with open(file_tE,'wb') as file:
        file.write(en)



file_name="keyForPass.key.txt" #the file containing generated key for encryption
file_tE="My All passwords.txt.txt" #file that you want to encrypt
#gen_key(file_name)
enc(file_tE)
with open(file_tE, "rb") as r:
    x = r.read()
    print(f'this is your encryted data==>>> {x}')
