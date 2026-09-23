Diabetes Prediction Using Logistic Regression

A machine learning project that predicts whether a person is likely to have diabetes based on health-related input data using Logistic Regression.

📌 Project Overview

This project implements a binary classification model using Logistic Regression. The system takes health information as input and predicts one of two outcomes:

Output	Meaning
0	No Diabetes
1	Diabetes
🧠 Machine Learning Model

Algorithm: Logistic Regression

Logistic Regression is used because the target variable contains two possible outcomes: diabetes or no diabetes.

📊 Input Features

The model uses the following features:

Feature	Description
Pregnancies	Number of pregnancies
Glucose	Plasma glucose concentration
Blood Pressure	Diastolic blood pressure
Skin Thickness	Triceps skin fold thickness
Insulin	2-Hour serum insulin
BMI	Body Mass Index
Diabetes Pedigree Function	Diabetes-related genetic risk indicator
Age	Age of the person
⚙️ Workflow
Patient Input
     ↓
Data Preprocessing
     ↓
Feature Scaling
     ↓
Logistic Regression
     ↓
Prediction
     ↓
Diabetes / No Diabetes

🛠️ Technologies

Python

Pandas

NumPy

Scikit-learn

Logistic Regression

📂 Project Structure
diabetes-prediction/
│
├── diabetes_prediction.py
├── diabetes.csv
├── README.md
└── requirements.txt

🚀 Installation

Clone the repository:

git clone https://github.com/your-username/diabetes-prediction.git


Navigate to the project directory:

cd diabetes-prediction


Install the required dependencies:

pip install -r requirements.txt

▶️ Run the Project
python diabetes_prediction.py


Enter the required health information when prompted. The system will then display the predicted result.

💻 Example
Enter Pregnancies: 2
Enter Glucose: 120
Enter Blood Pressure: 70
Enter Skin Thickness: 30
Enter Insulin: 100
Enter BMI: 28.5
Enter Diabetes Pedigree Function: 0.45
Enter Age: 35

Prediction: No Diabetes

📈 Prediction

The trained Logistic Regression model returns a binary classification:

0 → No Diabetes
1 → Diabetes

📄 Requirements

Create a requirements.txt file containing:

pandas
numpy
scikit-learn

⚠️ Disclaimer

This project is developed for educational and machine learning purposes only. The prediction should not be considered a medical diagnosis or a replacement for professional medical advice.