from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from sensor_model import model  # Make sure your model is imported correctly

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename.endswith('.csv'):
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            # Load CSV and predict
            df = pd.read_csv(file_path)

            # Assuming your model expects specific columns
            features = df[['Vibration', 'Temperature', 'Pressure', 'Voltage']]
            predictions = model.predict(features)
            df['Prediction'] = predictions

            result_html = df.to_html(classes='table', index=False)
            return render_template('result.html', table=result_html)

        else:
            return "Invalid file format. Please upload a CSV file."

    return render_template('upload.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/result')
def result():
    return render_template('result.html', table=None)

if __name__ == '__main__':
    app.run(debug=True)