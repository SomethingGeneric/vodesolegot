# stdlib
import os,sys

# Pip
from flask import Flask, render_template, redirect, make_response

# Custom
from translator import to_mandoa

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('basic.html', page_name="Yaim", content="<h2>Morutar!</h2>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4242, debug=True)