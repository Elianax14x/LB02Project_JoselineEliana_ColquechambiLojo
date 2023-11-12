from flask import Flask, request, session

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Authentifizierungslogik hier...

    session['logged_in'] = True
    return 'Erfolgreich eingeloggt!'

if __name__ == '__main__':
    app.run(debug=True)