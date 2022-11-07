import pyperclip
from flask import Flask, render_template, redirect
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    symbols = ["$", "!", "@", "&", "%", "*", "^"]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    random_letters = random.sample(letters,4)
    random_symbols = random.sample(symbols,4)
    random_numbers = random.sample(numbers,4)

    final_letters = "".join(random_letters)
    final_symbols = "".join(random_symbols)
    final_numbers = "".join(random_numbers)

    password_list = random.sample(final_letters+final_symbols+final_numbers,12)

    final_password = "".join(password_list)

    print(final_password)
    
    return render_template("index.html", final_password=final_password)

if __name__ == '__main__':
    app.run(debug=True)