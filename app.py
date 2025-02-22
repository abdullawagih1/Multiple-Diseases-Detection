from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the models
diabetes_model = pickle.load(open('Saved Models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('Saved Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('Saved Models/parkinsons_model.sav', 'rb'))

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Diabetes prediction route
@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
    diagnosis = ""
    if request.method == 'POST':
        try:
            data = [
                float(request.form['Pregnancies']),
                float(request.form['Glucose']),
                float(request.form['BloodPressure']),
                float(request.form['SkinThickness']),
                float(request.form['Insulin']),
                float(request.form['BMI']),
                float(request.form['DiabetesPedigreeFunction']),
                float(request.form['Age'])
            ]
            prediction = diabetes_model.predict([data])
            diagnosis = "The person is diabetic" if prediction[0] == 1 else "The person is not diabetic"
        except Exception as e:
            diagnosis = "Error processing input data: " + str(e)
    
    if diagnosis == 1:
        return render_template('diabetes.html', diagnosis=diagnosis)
    else:
        return render_template('index.html')

# Heart disease prediction route
@app.route('/heart-disease', methods=['GET', 'POST'])
def heart_disease():
    diagnosis = ""
    if request.method == 'POST':
        try:
            data = [
                float(request.form['age']),
                float(request.form['sex']),
                float(request.form['cp']),
                float(request.form['trestbps']),
                float(request.form['chol']),
                float(request.form['fbs']),
                float(request.form['restecg']),
                float(request.form['thalach']),
                float(request.form['exang']),
                float(request.form['oldpeak']),
                float(request.form['slope']),
                float(request.form['ca']),
                float(request.form['thal'])
            ]
            prediction = heart_disease_model.predict([data])
            diagnosis = "The person has heart disease" if prediction[0] == 1 else "The person does not have heart disease"
        except Exception as e:
            diagnosis = "Error processing input data: " + str(e)
    return render_template('heart_disease.html', diagnosis=diagnosis)

# Parkinson's prediction route
@app.route('/parkinsons', methods=['GET', 'POST'])
def parkinsons():
    diagnosis = ""
    if request.method == 'POST':
        try:
            data = [
                float(request.form['fo']),
                float(request.form['fhi']),
                float(request.form['flo']),
                float(request.form['Jitter_percent']),
                float(request.form['Jitter_Abs']),
                float(request.form['RAP']),
                float(request.form['PPQ']),
                float(request.form['DDP']),
                float(request.form['Shimmer']),
                float(request.form['Shimmer_dB']),
                float(request.form['APQ3']),
                float(request.form['APQ5']),
                float(request.form['APQ']),
                float(request.form['DDA']),
                float(request.form['NHR']),
                float(request.form['HNR']),
                float(request.form['RPDE']),
                float(request.form['DFA']),
                float(request.form['spread1']),
                float(request.form['spread2']),
                float(request.form['D2']),
                float(request.form['PPE'])
            ]
            prediction = parkinsons_model.predict([data])
            diagnosis = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
        except Exception as e:
            diagnosis = "Error processing input data: " + str(e)
    return render_template('parkinsons.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
