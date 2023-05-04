from base64 import b64decode

enc_flag = 'VmtkMFUyTnJNVlpPVlZaV1YwZG9VRlpyVlhka01WSnpWV3hLYkdGNlVqVlZNVkpQVkRGS1JrMVVUbFZYU0VKRFZGWmFkMk5XWkhSa1JUVnNZa1ZXTlZZeWVGTldhelZXVGxab1dGZElRazlhVjNoM1l6RlNkR05GTlU1aVNFSjRWakZTUTFSdFZuSldXR3hZWWtaS1lWUlVRWGhPYkZwWllrVTFWMUl4U25rPQ=='

enc_flag = enc_flag.encode()

risultato = b'ITASEC'.hex().encode()

while not enc_flag.startswith(risultato):
    enc_flag = b64decode(enc_flag)

flag = bytes.fromhex(enc_flag.decode()).decode()
print(f'{flag = }')
