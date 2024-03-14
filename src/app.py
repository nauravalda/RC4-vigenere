from flask import Flask, render_template, request, send_file
import os
import base64
from cipher_functions.rc4_vigenere import rc4


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'



@app.route("/", methods=["POST", "GET"])
def rc4_vigenere():
    if request.method == "POST":
        res = ''
        key = request.form["key"]
        key_b = bytes(key, 'utf-8')
        inputtext = request.form["inputtext"]
        file = request.files["file"]
        if file:
            UPLOAD_FOLDER = 'uploads'
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            
            file.save(file_path)
            with open(file_path, 'rb') as f:
                inputtext = memoryview(f.read())
        if request.form["options"] == "e":
            
            if file:
                filename = file.filename.split(".")[0]
                file_extension = file.filename.split(".")[1]
                enc = rc4(inputtext, key_b, True)
                with open(f"uploads/{filename}_encrypted.{file_extension}", "wb") as f:
                    f.write(enc)
                return render_template("download.html", filename=f"{filename}_encrypted.{file_extension}")
            else:
                plain = bytearray(inputtext, 'utf-8')
                enc = rc4(plain, key_b)
                res = enc.hex().upper()
            return render_template("rc4_vigenere.html", res=res, key=key, inputtext=inputtext, mode="e")
        else:
            if file:
                filename = file.filename.split(".")[0]
                file_extension = file.filename.split(".")[1]
                dec = rc4(inputtext, key_b, False)
                with open(f"uploads/{filename}_decrypted.{file_extension}", "wb") as f:
                    f.write(dec)
                return render_template("download.html", filename=f"{filename}_decrypted.{file_extension}")
            else:
                cipher = bytes.fromhex(inputtext)
                dec = rc4(cipher, key_b, False)
                res = dec.decode()
            return render_template("rc4_vigenere.html", res=res, key=key, inputtext=inputtext, mode="d")
    return render_template("rc4_vigenere.html")




@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):
    return send_file(f"uploads/{filename}", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

