from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

def upload_file():
    filedata

@app.route("/hello", methods=['POST', 'GET'])
def index():

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")

@app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == "POST":
        greeting = "File was uploaded."
        return render_template("index.html", greeting=greeting)

    else:
        return render_template("file_upload_form.html")

if __name__ == "__main__":
    app.run()
