from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
      </head>
      <body>
        <a href="/hello">Take me to hello!</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <input type="submit">
          <br>
          <br>
          <label for="field-compliment">Compliment: </label>
          <select name="compliment" id="field-compliment">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="pythonic">Pythonic</option>
            <option value="neato">Neato</option>
            <option value="fantastic">Fantastic</option>
            <option value="coolio">Coolio</option>
          </select>
        </form>
        <br>
        <br>
        <form action="/diss">
          <label>Let's be mean to who? <input type="text" name="person"></label>
          <input type="submit">
          <br>
          <br>
          <label for="field-diss">Diss: </label>
          <select name="diss" id="field-diss">
            <option value="fine">Fine</option>
            <option value="whatever">Whatever</option>
            <option value="alright">Alright</option>
            <option value="okay">Okay</option>
          </select>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, compliment)

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Sarcastic Diss</title>
      </head>
      <body>
        Hi %s I think you're %s!
      </body>
    </html>
    """ % (player, diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
