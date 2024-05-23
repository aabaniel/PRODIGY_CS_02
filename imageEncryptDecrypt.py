def encrypter(path, key):
    file = open(path, 'rb')
        
    img = file.read()
        
    img = bytearray(img)
    
    for index, values in enumerate(img):
        img[index] = values ^ key
    
    file = open(path, 'wb')
        
    file.write(img)
    file.close()


print("IMAGE ENCRYPTION TOOL\n")

path = input(r'Enter path of Image:')
key = int(input('Enter Key : '))

print('\nDETAILS:\n')
print('The path of file : ', path)
print('Key for encryption / decryption : ', key)

encrypter(path, key)
    
print('\nEncryption / Decryption Done...')