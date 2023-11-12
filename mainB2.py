from flask import Flask

app = Flask(__name__)

# Äußere Funktion, die eine innere Funktion (Closure) zurückgibt
def generate_greeting_function(prefix):
    def greeting(name):
        return f"{prefix}, {name}!"
    return greeting

# Funktion als Closure verwenden und in Variable speichern
friendly_greeting = generate_greeting_function("Hello")
respectful_greeting = generate_greeting_function("Dear Ladies and Gentlemen")

@app.route('/friendly/<name>')
def friendly_greeting_route(name):
    return friendly_greeting(name)

@app.route('/respectful/<name>')
def respectful_greeting_route(name):
    return respectful_greeting(name)

if __name__ == '__main__':
    app.run(debug=True)

