import os, sys

sys.path.insert(0, os.path.abspath('packages'))

from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import pandas as pd

app = Flask(__name__)
app.secret_key = 'Asecretisasecret'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        file_name = request.form['file_name']
        try:
            result = subprocess.run(['python3', 'nlp.py', file_name], check=True, text=True, capture_output=True)
            flash('Model training completed successfully!')
            flash(result.stdout)
        except subprocess.CalledProcessError as e:
            flash('Error in training the model.')
            flash(e.stderr)
        return redirect(url_for('result'))
    return render_template('train.html')

@app.route('/result')
def result():
    # Read the training data file
    df = pd.read_csv('training_data.csv')
    return render_template('result.html', tables=[df.to_html(classes='data', header="true")])

if __name__ == '__main__':
    app.run(debug=True)
