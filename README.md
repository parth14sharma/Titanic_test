# 🚢 Titanic - Machine Learning from Disaster

This repository contains a machine learning project based on the famous **Titanic dataset** from [Kaggle](https://www.kaggle.com/c/titanic). The objective is to predict whether a passenger survived or not based on features like age, gender, ticket class, etc.

## 🧠 Project Objective

Build a supervised machine learning model to classify Titanic passengers as **Survived (1)** or **Did not survive (0)**.

---

## 📁 Repository Structure


---

## 📊 Dataset Description

The dataset contains the following features:

| Feature       | Description                            |
|---------------|----------------------------------------|
| PassengerId   | Unique ID of passenger                 |
| Survived      | Survival (0 = No, 1 = Yes)             |
| Pclass        | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)|
| Name          | Name of passenger                      |
| Sex           | Gender                                 |
| Age           | Age in years                           |
| SibSp         | # of siblings / spouses aboard         |
| Parch         | # of parents / children aboard         |
| Ticket        | Ticket number                          |
| Fare          | Passenger fare                         |
| Cabin         | Cabin number                           |
| Embarked      | Port of Embarkation (C, Q, S)          |

---

## 🛠️ Model Architecture

A basic stacking classifier is used with the following architecture:

- **Base Learners**:
  - `MultinomialNB`
  - `Calibrated LinearSVC`
- **Meta Learner**:
  - `MLPClassifier`

All features are preprocessed using:

- TF-IDF Vectorization (for text-based features if any)
- Label Encoding
- Imputation for missing values
- Chi-squared feature selection

---

## 🔍 Performance Metrics

The model is evaluated using:

- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **Confusion Matrix**

Sample accuracy (varies based on data split and seed):  
`Accuracy: ~0.79`

---

## ▶️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/titanic-ml.git
cd titanic-ml
