import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    result = ""
    with open("embed") as f:
        result += f.read()
    result += "<br>"
    result += "Please, save this poor clown. He's single. Contact dbcu on Discord. <br>"
    result += "<img src=/burritoman.jpg width=560>"
    result += "<br>"
    result += "And this one. She's also single. Contact soleilcrow on Discord <br>"
    result += "<img src=/rockwoman.jpg width=560>"
    return result

@app.route('/burritoman.jpg')
def burritoman():
    return flask.send_file("burritoman.jpg")

@app.route('/rockwoman.jpg')
def rockwoman():
    return flask.send_file("rockwoman.jpg")

app.run()

