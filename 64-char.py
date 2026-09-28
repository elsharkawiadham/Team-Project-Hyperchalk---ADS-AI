import secrets, string
alphabet = string.ascii_letters+string.digits+"!#$%&()*+,-./:;<=>?@[]^_{|}~"
print(''.join(secrets.choice(alphabet) for _ in range(64)))
