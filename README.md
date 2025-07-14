# 🌸 Iris Flower Prediction 🌸

## 📋 Overview :-

This project is a **web application** that predicts the species of an Iris flower based on its sepal and petal measurements.
It uses a **Decision Tree Classifier** trained on the classic Iris dataset and provides a **full-screen, user-friendly Flask GUI**.

### 🌐 Live App on Render: https://iris-flower-classification-1-zd66.onrender.com 

## 🌟 Features :-

- ✅ Trained **Decision Tree** model
- ✅ **Flask-based** web app with stylish, full-screen GUI
- ✅ User-friendly **form** for entering measurements
- ✅ Displays the **predicted Iris species**
- ✅ Lists possible categories:
  - *Iris-setosa*
  - *Iris-versicolor*
  - *Iris-virginica*

## 📂 Project Structure :-

- `app.py` — Flask app that loads the model & serves predictions
- `classification.py` — Script to train & save the model
- `iris_model.joblib` — Saved Decision Tree model
- `iris_encoder.joblib` — Saved LabelEncoder for target classes
- `templates/index.html` — Stylish HTML GUI for user input
- `README.md` — Project documentation

## 🚀 How to Run Locally :-

### 1️⃣ Clone the repository

git clone https://github.com/your-username/iris-flask-app.git
cd iris-flask-app

### 2️⃣ Create & activate virtual environment

python -m venv venv
venv\Scripts\activate         # on Windows
source venv/bin/activate      # on Linux/Mac

### 3️⃣ Install dependencies

pip install flask scikit-learn pandas joblib

### 4️⃣ Train the model

Run the training script to generate `iris_model.joblib` and `iris_encoder.joblib`:

python classification.py

### 5️⃣ Start the Flask app

python app.py


## 🌐 How to Deploy on Render :-

### Steps to Deploy;

- 1️⃣ Push your code to a public GitHub repository.

- 2️⃣ On [https://render.com](https://render.com):
  - Click **New → Web Service**
  - Connect your GitHub repository
  - Choose **Python**, and set the start command :
        "gunicorn app.main:app"

- 3️⃣ Wait for it to build & deploy.

- 4️⃣ Visit the live URL that Render gives you.

## 📚 Dependencies :-

* Python 3.7+
* Flask
* scikit-learn
* pandas
* joblib
* Bootstrap 

## 👩‍💻 Author :-
Niharika Saxena🌸
