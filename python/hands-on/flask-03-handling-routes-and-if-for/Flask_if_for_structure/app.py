from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "bu benim ilk tecrübem"
    return render_template("index.html", message=first)


@app.route("/samet")
def my_list():
    liste = ["a","b",2,3,4]
    return render_template("body.html",object=liste)













if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=80)