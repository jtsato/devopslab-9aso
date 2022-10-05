from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "There's a point where we just let the music take over everything."

if __name__ == '__main__':
    app.run()