import re
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "Hoş Geldiniz"

@app.route("/hakkinda")
def hakkinda():
    return '<h1>Burası Hakkında sayfası başkaları sizin hakkınızda ne düşünüyor burdan görebilirisiniz :) </h1>'

@app.route("/hata")
def hata():
    return f'<h1>!!!!!!!!!!!!!!!!   YETKİSİZ ERİŞİM    !!!!!!!!!!</h1>'

@app.route("/admin")
def admin():
    return redirect(url_for('hata'))



@app.route("/<isim>")
def hosgeldin(isim):
    return render_template("hosgeldiniz.html", isim_html = isim )

@app.route("/liste")
def liste():
    return render_template("liste.html")

@app.route("/kosul")
def kosul():
    ilk = ""
    return render_template("kosul.html", mesaj=ilk)






if __name__ == "__main__":
    app.run(debug=True)

