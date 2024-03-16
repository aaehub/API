from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='templates')

data1 = "Initial data 1"
data2 = "Initial data 2"

@app.route('/GET1', methods=['GET'])
def get1():
    return data1

@app.route('/PUT1', methods=['POST'])
def put1():
    new_data = request.form.get('new_data')
    global data1
    data1 = new_data
    return ('', 204)  

@app.route('/GET2', methods=['GET'])
def get2():
    return data2

@app.route('/PUT2', methods=['POST'])
def put2():
    new_data = request.form.get('new_data')
    global data2
    data2 = new_data
    return jsonify({'message': 'Data 2 updated successfully'})

@app.route("/")
def home():
    return render_template('index.html', color=get_color())

def get_color():
    global data1
    if data1.lower() == 'true':
        return 'green'
    else:
        return 'red'

if __name__ == '__main__':
    app.run(debug=True)