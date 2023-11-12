from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

@app.route('/b1', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_list = list(map(int, request.form['number_list'].split(',')))

        bubble_sort(input_list)

        return render_template('index.html', sorted_list=input_list)

    return render_template('index.html', sorted_list=None)

if __name__ == '__main__':
    app.run(debug=True)