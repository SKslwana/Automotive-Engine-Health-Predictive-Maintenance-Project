from flask import Flask, render_template, request
import pickle

model = pickle.load(open('trained_model-1.0.2.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/engine', methods=['GET', 'POST'])
def engine_post():
    return render_template('engine.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    Engine_rpm = int(request.form['Engine RPM'])
    Lub_oil_pressure = float(request.form['Lubrication Oil Pressure'])
    Fuel_pressure = float(request.form['Fuel Pressure'])
    Coolant_pressure = float(request.form['Coolant Pressure'])
    Lub_oil_temp = float(request.form['Lubrication Oil Temperature'])
    Coolant_temp = float(request.form['Coolant Temperature'])
    pred = model.predict([[Engine_rpm, Lub_oil_pressure, Fuel_pressure, Coolant_pressure, Lub_oil_temp, Coolant_temp]])
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)
