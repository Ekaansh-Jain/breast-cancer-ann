from flask import Flask, render_template, request
import numpy as np
from keras.models import load_model

app = Flask(__name__)

model = load_model('breast_cancer_model.h5')
features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']
@app.route('/')
def home():
    return render_template("index.html", features=features)

@app.route('/predict', methods = ['POST'])
def greet():

    values = [float(request.form[feature]) for feature in features]
    array = np.array(values)
    array = np.array(values).reshape(1, -1)
    prediction = model.predict(array)[0][0]
    result = "Malignant (1)" if prediction >= 0.5 else "Benign (0)"
    return f"<h2>Prediction: {result}</h2>"
    

if __name__ == '__main__':
    app.run(debug=True)