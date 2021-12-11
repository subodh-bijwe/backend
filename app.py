from flask import Flask, request, url_for, redirect, render_template
import pandas as pd
import pickle
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)
model = pickle.load(open("model_weights.pkl", "rb"))


@app.route('/')
def use_template():
    return render_template("index.html")
# 'age', 'sex', 'bmi', 'children', 'smoker', 'age_range','have_children'
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    input_one = request.form['1']
    input_two = request.form['2']
    input_three = request.form['3']
    input_four = request.form['4']
    input_five = request.form['5']

    setup_df = pd.DataFrame([pd.Series([input_one, input_two, input_three, input_four, input_five])])
    charges_prediction = model.predict(setup_df)
    print(charges_prediction[0])
    return str(charges_prediction[0])
if __name__ == '__main__':
    app.run(debug=True)
