from Crypto.Cipher import AES


def encrypt_aes(string,key,mode='GCM'):
  m = ''
  if mode == 'GCM':
    m = AES.MODE_GCM
  elif mode == 'EAX':
    m = AES.MODE_EAX
  elif mode == 'CCM'  :
    m = AES.MODE_CCM
  else: 
    raise Exception(f"no mode {mode}")
  st_utf = string.encode('utf-8')
  k = bytes(key.encode('ascii'))
  cipher = AES.new(k, m)
  ciphertext, tag = cipher.encrypt_and_digest(st_utf)
  z = [x for x in (cipher.nonce, tag, ciphertext)]
  return f"{z}"
  

def decrypt_aes(string,key,mode='GCM'):
  m = ''
  if mode == 'GCM':
    m = AES.MODE_GCM
  elif mode == 'EAX':
    m = AES.MODE_EAX
  elif mode == 'CCM'  :
    m = AES.MODE_CCM
  else: 
    raise Exception(f"no mode {mode}")
  
  key = bytes(key.encode('ascii'))


  nonce, tag, ciphertext = string[0],string[1],string[2]

  cipher = AES.new(key, m, nonce)
  data = cipher.decrypt_and_verify(ciphertext, tag)
  return data.decode('utf-8')
