from werkzeug.security import generate_password_hash, check_password_hash

a = generate_password_hash('firebot')
print(a)