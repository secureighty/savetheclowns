import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    result = ""
    with open("embed") as f:
        result += f.read()
    result += "<br>"
    result += "Please, save this poor clown. He's single. Contact Draco Blaze#0942 on Discord. <br>"
    result += "<img src=/burritoman.jpg width=560>"
    return result

@app.route('/burritoman.jpg')
def burritoman():
    return flask.send_file("burritoman.jpg")

app.run()

