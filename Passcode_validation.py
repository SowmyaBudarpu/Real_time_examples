#!/usr/bin/python
import re

# Password Criteria
# 1. Should contain alphanumeric
# 2. At least one Capital Letter
# 3. At least one small letter
# 4. 8-20 characters
# 5. at least one special character !@#$%^&*_
# 6. No whitespace please

passwords = ['SpiderMan', 'Spider Man0$','Pokemon$', 'Batman_123*', '12Pooh#', 'Sh0rt5!','Sh0rt5!89***^AWS+', 'short', 'Passw0rd#', 'SecureP@ss']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '_']

# Password History
password_history = ['PreviousPassword1', 'PreviousPassword2', 'Batman_123*', '12Pooh#']

# Using Regular Expression
pattern = '^((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*_])(?=.*[\S])[0-9a-zA-Z!@#$%^&*_]{8,20})$'

def check_password_history(password):
    if password in password_history:
        return False
    return True

for password in passwords:
    print(password)
    if not check_password_history(password):
        print("Password Denied: Password has been used previously.")
        continue
    result = re.match(pattern,password)
    if result:
        print("Password Accepted")
    else:
        print("Password Denied")
