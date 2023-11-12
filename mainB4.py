from flask import Flask, jsonify
import itertools

app = Flask(__name__)

# Beispiel-Daten
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map: Quadriere jedes Element
mapped_data = list(map(lambda x: x**2, data))

# Filter: Auswahl nur der geraden Zahlen
filtered_data = list(filter(lambda x: x % 2 == 0, mapped_data))

# Gruppierung und Aggregation: Gruppiere nach Modulo 3 und summiere
grouped_data = itertools.groupby(filtered_data, key=lambda x: x % 3)
aggregated_data = {key: sum(group) for key, group in grouped_data}

# Flask-Route zur Anzeige der Ergebnisse
@app.route('/b4')
def index():
    return jsonify({
        'original_data': data,
        'mapped_data': mapped_data,
        'filtered_data': filtered_data,
        'aggregated_data': aggregated_data
    })

if __name__ == '__main__':
    app.run(debug=True)
