from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/vigenere-cipher", methods=["POST", "GET"])
def vigenere_cipher():
    # if request.method == "POST":
    #     plaintext = request.form["plaintext"]
    #     key = request.form["key"]
    #     return render_template("vigenere.html", plaintext=plaintext, key=key)
    return render_template("vigenere.html")

if __name__ == '__main__':
    app.run(debug=True)
