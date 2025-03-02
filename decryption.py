from cryptography.fernet import Fernet

def load_key(): #load the generated key
    with open("keyForPass.key.txt",'rb') as r:
        return r.read()

def dec(file_name):
    k=load_key()
    cipher=Fernet(k)
    with open(file_name,"rb") as f:
        data=f.read()
        dec=cipher.decrypt(data)
    with open(file_name,"wb") as w:
        w.write(dec)


file_name="My All passwords.txt.txt" #file to be decrypted
dec(file_name)
with open(file_name,"rb") as r:
    x=r.read()
    print(f'This is the decryted file ++>{x}')
