import os


import urllib.request


from flask import Flask, request, render_template, jsonify, send_from_directory

__author__ = 'ibininja'

app = Flask(__name__ , static_folder='/Users/Nipun/Desktop/src/images')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

global filename

global html_page


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    print("Approot" + APP_ROOT)

    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        print("filename is "+filename)
        destination = "/".join([target,filename])
        print(destination)
        file.save(destination)
        print("http://127.0.0.1:4555/Users/Nipun/Desktop/src"+filename)



    # return send_from_directory("images", filename, as_attachment=True)
        return render_template("complete.html" )



@app.route("/download", methods = ["GET"])
def download():
    with urllib.request.urlopen("http://127.0.0.1:4555/Users/Nipun/Desktop/src"+filename) as url:
        s = url.read()
    # I'm guessing this would output the html source code?
    print(s)



@app.route('/data')
def data():
    query_string = request.query_string  ## There is it
    return "<h1>DATA<h1>"


if __name__ == "__main__":
    app.run(port=4555, debug=True)
