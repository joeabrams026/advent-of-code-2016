import hashlib
input = 'ojvtpuvg'
input = 'abc'

def crack(input):
    password = ''
    for i in xrange(50000000):
        if len(password) == 8:
            break
        key = input + str(i)
        key = key.strip()
        md5 = hashlib.md5()
        md5.update(key)
        if md5.hexdigest().startswith('00000'):
            #3231929
            print key, md5.hexdigest()
            password = password + md5.hexdigest()[5]
            
    return password
            
print crack ('abc') == '18f47a30'
print crack ('ojvtpuvg')