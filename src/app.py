from flask import Flask, render_template, request
import os

import cipher_functions.vigenere


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/vigenere-cipher", methods=["POST", "GET"])
def vigenere_cipher():
    if request.method == "POST":
        res = ''
        key = request.form["key"]
        print(key)
        inputtext = request.form["inputtext"]
        file = request.files["file"]
        if file:
            UPLOAD_FOLDER = 'uploads'
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            
            file.save(file_path)
            with open(file_path, 'r') as f:
                inputtext = f.read()
        if request.form["options"] == "e":
            from cipher_functions.vigenere import encrypt_vigenere
            res = encrypt_vigenere(inputtext, key)
            return render_template("vigenere.html", res=res, key=key, inputtext=inputtext, mode="e")
        else:
            from cipher_functions.vigenere import decrypt_vigenere
            res = decrypt_vigenere(inputtext, key)
            return render_template("vigenere.html", res=res, key=key, inputtext=inputtext, mode="d")
    return render_template("vigenere.html")

if __name__ == '__main__':
    app.run(debug=True)
