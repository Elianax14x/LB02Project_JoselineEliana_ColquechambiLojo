from flask import Flask

app = Flask(__name__)

#B3G
@app.route('/quadrat/<int:zahl>', methods=['GET'])
def quadrat(zahl):
    quadrieren = lambda x: x**2
    ergebnis = quadrieren(zahl)
    return f'Das Quadrat von {zahl} ist {ergebnis}.'

#B3F
@app.route('/addition/<int:zahl1>/<int:zahl2>', methods=['GET'])
def addition(zahl1, zahl2):
    addieren = lambda x, y: x + y
    ergebnis = addieren(zahl1, zahl2)
    return f'Die Summe von {zahl1} und {zahl2} ist {ergebnis}.'

#B3E
@app.route('/sortieren/<word_list>', methods=['GET'])
def sortieren(word_list):
    words = word_list.split(',')
    sortierte_liste = sorted(words, key=lambda x: len(x))
    return f'Sortierte Liste: {", ".join(sortierte_liste)}'

if __name__ == '__main__':
    app.run(debug=True)