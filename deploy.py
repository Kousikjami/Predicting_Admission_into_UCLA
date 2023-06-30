from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)
# Load the model
model = pickle.load(open('admission_Prediction (1).pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    a = int(request.form['a'])
    b = int(request.form['b'])
    c = float(request.form['c'])
    d = float(request.form['d'])
    e = float(request.form['e'])
    f = float(request.form['f'])
    g = int(request.form['g'])
    result = model.predict([[a, b, c, d, e, f, g]])[0]
    if result == 1:
        result = "YES"
    else:
        result = "NO"
    return render_template('index.html', prediction=result)


if __name__ == '__main__':
    app.run(debug=True)
