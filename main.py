from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!!</h1>"

@app.route("/curso")
def index1():
    return "<h1>Meu curso é Desenvolvimento de Sistemas</h1>"

if __name__ == "__main__":
    app.run()
