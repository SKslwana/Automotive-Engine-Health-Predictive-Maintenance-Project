from flask import Flask, render_template, request
import pickle

model = pickle.load(open('trained_model-1.0.2.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    Engine_rpm = request.form['Engine_rpm']
    Lub_oil_pressure = request.form['Lub_oil_pressure']
    Fuel_pressure = request.form['Fuel_pressure']
    Coolant_pressure = request.form['Coolant_pressure']
    lub_oil_temp = request.form['lub_oil_temp']
    Coolant_temp = request.form['Coolant_temp']
    pred = model.predict([[Engine_rpm, Lub_oil_pressure, Fuel_pressure, Coolant_pressure, lub_oil_temp, Coolant_temp]])[0]
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















