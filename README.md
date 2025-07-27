# 🧠 Breast Cancer Prediction Web App

A lightweight, Flask-based web application that predicts the likelihood of breast cancer (Benign or Malignant) using clinical features. The prediction model is built using an Artificial Neural Network (ANN) trained on the UCI Breast Cancer Wisconsin dataset.

---

## 🚀 Features

- Simple, user-friendly form to input clinical features
- Real-time prediction using a trained Keras ANN model
- Flask backend with HTML frontend
- Clean code and modular structure
- Ready for local deployment or cloud hosting

---

## 🧠 Model Details

- **Input Features**: 30 features from the UCI dataset (e.g., radius_mean, texture_mean, perimeter_mean, etc.)
- **Architecture**:
  - Input Layer: 30 neurons
  - Hidden Layers: 2 Dense layers with ReLU
  - Output Layer: 1 neuron with Sigmoid activation
- **Loss**: Binary Crossentropy
- **Optimizer**: Adam
- **Accuracy**: ~96% on validation set

---

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- Flask
- HTML / CSS
- Pandas / NumPy

---


