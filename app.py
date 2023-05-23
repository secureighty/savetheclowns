import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    with open("embed") as f:
        return f.read()

app.run()

