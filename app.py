from flask import Flask, render_template, request

from utils import generate_password

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password_length = int(request.form.get('length'))
        letters = request.form.get('letters')
        numbers = request.form.get('numbers')
        special_symbols = request.form.get('special_symbols')
        password = generate_password(length=password_length, letters=letters, numbers=numbers,
                                     special_symbols=special_symbols)
        selected_length = password_length
    if request.method == 'GET':
        password = generate_password(length=12)
        selected_length = 12
        letters = True
        numbers = True
        special_symbols = True

    password_length_range = range(1, 51)
    return render_template('index.html', password=password, password_length_range=password_length_range,
                           selected_length=selected_length, letters=letters, numbers=numbers,
                           special_symbols=special_symbols)


if __name__ == '__main__':
    app.run(debug=True)
