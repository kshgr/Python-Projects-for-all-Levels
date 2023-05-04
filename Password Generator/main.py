import secrets
import string

letters = string.ascii_letters
digits = string.digits

alphabet = letters + digits

pwd_length = 16

pwd = ''

for i in range(pwd_length):
  x = secrets.choice(alphabet)
  pwd += ''.join(x)

print("Password:",pwd)
