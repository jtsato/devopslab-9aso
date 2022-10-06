from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/")
def pagina_inicial():
    return "There's a point where we just let the music take over everything."

if __name__ == '__main__':
    app.run()