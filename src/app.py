from flask import Flask, render_template, request, send_file
import os
import base64

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
        
        if request.form["options"] == "e":
            from cipher_functions.vigenere import vigenere
            res = vigenere(inputtext, key, True)
            b64 = base64.b64encode(res.encode())
            return render_template("vigenere.html", res=res, b64=b64, key=key, inputtext=inputtext, mode="e")
        else:
            from cipher_functions.vigenere import vigenere
            res = vigenere(inputtext, key, False)
            return render_template("vigenere.html", res=res, key=key, inputtext=inputtext, mode="d")
    return render_template("vigenere.html")

@app.route("/extended-vigenere-cipher", methods=["POST", "GET"])
def extended_vigenere_cipher():
    if request.method == "POST":
        res = ''
        key = request.form["key"]
        inputtext = request.form["inputtext"]
        file = request.files["file"]
        if file:
            UPLOAD_FOLDER = 'uploads'
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            
            file.save(file_path)
            with open(file_path, 'rb') as f:
                inputtext = f.read()
        if request.form["options"] == "e":
            
            if file:
                filename = file.filename.split(".")[0]
                file_extension = file.filename.split(".")[1]
                from cipher_functions.extended_vigenere import extended_vigenere_bin
                extended_vigenere_bin(file_path, f"uploads/{filename}_encrypted.{file_extension}", key, True)
                return render_template("download.html", filename=f"{filename}_encrypted.{file_extension}")
            else:
                from cipher_functions.extended_vigenere import extended_vigenere
                res = extended_vigenere(inputtext, key, True)
            return render_template("extended_vigenere.html", res=res, key=key, inputtext=inputtext, mode="e")
        else:
            if file:
                filename = file.filename.split(".")[0]
                file_extension = file.filename.split(".")[1]
                from cipher_functions.extended_vigenere import extended_vigenere_bin
                extended_vigenere_bin(file_path, f"uploads/{filename}_decrypted.{file_extension}", key, False)

                return render_template("download.html", filename=f"{filename}_decrypted.{file_extension}")
            else:
                from cipher_functions.extended_vigenere import extended_vigenere
                res = extended_vigenere(inputtext, key, False)
            return render_template("extended_vigenere.html", res=res, key=key, inputtext=inputtext, mode="d")
    return render_template("extended_vigenere.html")

@app.route("/playfair-cipher", methods=["POST", "GET"])
def playfair_cipher():
    if request.method == "POST":
        res = ''
        key = request.form["key"]
        inputtext = request.form["inputtext"]
        
        if request.form["options"] == "e":
            from cipher_functions.playfair import playfair
            res = playfair(inputtext, key)
            b64 = base64.b64encode(res.encode())
            return render_template("playfair.html", b64=b64, res=res, key=key, inputtext=inputtext, mode="e")
        else:
            from cipher_functions.playfair import playfair
            res = playfair(inputtext, key, False)
            return render_template("playfair.html", res=res, key=key, inputtext=inputtext, mode="d")
    return render_template("playfair.html")


@app.route("/affine-cipher", methods=["POST", "GET"])
def affine_cipher():
    if request.method == "POST":
        res = ''
        shift = int(request.form["shift"])
        multiplier = int(request.form["multiplier"])
        inputtext = request.form["inputtext"]
        
        if request.form["options"] == "e":
            from cipher_functions.affine import affine
            res = affine(inputtext, multiplier, shift)
            b64 = base64.b64encode(res.encode())
            return render_template("affine.html", b64=b64, res=res, shift=shift, multiplier=multiplier, inputtext=inputtext, mode="e")
        else:
            from cipher_functions.affine import affine
            res = affine(inputtext, multiplier, shift, False)
            return render_template("affine.html", res=res, shift=shift, multiplier=multiplier, inputtext=inputtext, mode="d")
    return render_template("affine.html")

@app.route("/product-cipher", methods=["POST", "GET"])
def product_cipher():
    if request.method == "POST":
        res = ''
        inputtext = request.form["inputtext"]
        length = int(request.form["length"])
        key = request.form["key"]
        
        if request.form["options"] == "e":
            from cipher_functions.transposition import transposition
            from cipher_functions.vigenere import vigenere
            temp = vigenere(inputtext, key, True)
            res = transposition(temp, length, True)
            b64 = base64.b64encode(res.encode())
            return render_template("product.html",b64=b64, res=res, key=key, length=length, inputtext=inputtext, mode="e")
        else:
            from cipher_functions.transposition import transposition
            res = transposition(inputtext, length, False)
            from cipher_functions.vigenere import vigenere
            res = vigenere(res, key, False)
            return render_template("product.html", res=res, key=key, length=length, inputtext=inputtext, mode="d")
    return render_template("product.html")

@app.route("/autokey-vigenere-cipher", methods=["POST", "GET"])
def autokey_vigenere():
    if request.method == "POST":
        res = ''
        key = request.form["key"]
        inputtext = request.form["inputtext"]
        
        if request.form["options"] == "e":
            from cipher_functions.autokey_vigenere import autokey_vigenere
            res = autokey_vigenere(inputtext, key, True)
            b64 = base64.b64encode(res.encode())
            return render_template("autokey_vigenere.html", b64=b64, res=res, key=key, inputtext=inputtext, mode="e")
        else:
            from cipher_functions.autokey_vigenere import autokey_vigenere
            res = autokey_vigenere(inputtext, key, False)
            return render_template("autokey_vigenere.html", res=res, key=key, inputtext=inputtext, mode="d")
    return render_template("autokey_vigenere.html")


@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_file(f"uploads/{filename}", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
