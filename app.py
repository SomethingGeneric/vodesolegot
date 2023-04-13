# stdlib
import os,sys

# Pip
from flask import Flask, request, render_template, redirect, make_response

# Custom
from translator import to_mandoa, to_english

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('basic.html', page_name="Yaim", content="<h2>Morutar!</h2>"+render_template("form.html"))
    elif request.method == 'POST':
        text = request.form['itext']
        lang = request.form['lang']
        print(f"got {text} in {lang}")
        if lang == "mandoa":
            out = to_english(text)
            for item in out:
                if not " " in item[1]:
                    out = item[1]
                else:
                    out = item[1].split(" ")[0]
            rlang = "english"
        elif lang == "english":
            out = to_mandoa(text)
            for item in out:
                if not " " in item[0]:
                    out = item[0]
                else:
                    out = item[0].split(" ")[0]
            rlang = "mando'a"
        else:
            out = "how'd we get here??"
        return render_template('basic.html', page_name="Result", content=f"<p>\"{text}\" in {lang} is \"{out}\" in {rlang}</p>"+render_template("form.html"))
    else:
        return "what? go away"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4242, debug=True)