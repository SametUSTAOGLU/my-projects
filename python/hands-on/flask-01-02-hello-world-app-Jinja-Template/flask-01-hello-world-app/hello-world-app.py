from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"


@app.route("/second")
def second():
    return "Bize her yer trabzon"

@app.route("/third/subthird")
def third():
    return "bu sayfa 3. sayfanın alt sayfasdır."



@app.route("/fourth/<string:id>") 
def fourth(id):
    return f'id number {id}'


if __name__ == '__main__':
    app.run(debug=True)
