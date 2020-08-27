from flask import Flask, request

from utils import generate_random_password

app = Flask(__name__)


@app.route('/generate-password/')
def generate_password():
    password_len = request.args.get('password-len', '10')

    if not password_len.isdigit():
        return 'Error, password-len should be integer'

    password_len = int(password_len)

    if password_len > 100:
        return 'Password should be less than 100'

    return generate_random_password(password_len)

# http://127.0.0.1:8000/gen-pass/?password-len=10

if __name__ == "__main__":
    app.run(port=5000, debug=True)
