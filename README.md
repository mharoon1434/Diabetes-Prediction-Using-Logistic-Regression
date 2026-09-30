<div>

# 🩺 Diabetes Prediction

### Logistic Regression Machine Learning Project

Predict diabetes from patient health parameters using **Python + Scikit-learn**.

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Model-Logistic%20Regression-green?style=for-the-badge">
<img src="https://img.shields.io/badge/ML-Scikit--learn-orange?style=for-the-badge">

</div>

---

## About

This project uses **Logistic Regression** to predict whether a patient is diabetic or non-diabetic.

- `0` → Not Diabetic
- `1` → Diabetic

### Features

- Data preprocessing
- Outlier removal
- Train/test split
- Feature scaling
- Logistic Regression
- Accuracy evaluation
- Interactive prediction

---

<details>
<summary> Technologies</summary>

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

</details>

<details>
<summary> Dataset</summary>

Dataset: `diabetes.csv`

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Glucose level |
| BloodPressure | Blood pressure |
| SkinThickness | Skin thickness |
| Insulin | Insulin level |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree value |
| Age | Patient age |
| Outcome | Diabetes result |

</details>

<details>
<summary>🤖 Machine Learning Model</summary>

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_reg = LogisticRegression()
log_reg.fit(X_train_scaled, y_train)

y_pred = log_reg.predict(X_test_scaled)

score = accuracy_score(y_test, y_pred)
print("Accuracy:", score)
