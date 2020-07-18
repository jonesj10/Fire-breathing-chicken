from werkzeug.security import generate_password_hash, check_password_hash


pwdhsh = 'pbkdf2:sha256:150000$aGGKoQ4Y$5a02602fe0dd38bfdeeb8802fea58c62db0230d09dcc7fb22750891c06725ce2'  # hash for password
password = input("Please enter your password\n")
passhash = generate_password_hash(password)
auth = check_password_hash(pwdhsh, password)
a = generate_password_hash('firebot')

if auth:
    print('\nLogin Successful\n')
else:
    print('\nPassword is incorrect! Try again.')