# 📊 Marketing AI System – Target Customer Prediction

## 🔥 Project Overview

The **Marketing AI System** is an intelligent data-driven application designed to help marketing teams identify **high-probability customers** for a new product.

Instead of targeting all users blindly, this system uses **machine learning + behavioral analysis + similarity intelligence** to recommend only those users who are most likely to purchase.

---

## 🎯 Problem Statement

Marketing teams often face challenges in:

* Identifying the right target audience
* Reducing advertising cost
* Increasing conversion rate
* Utilizing customer behavior data effectively

This project solves the problem by:

> Predicting and recommending a set of customers who have a **high probability of buying a given product**

---

## 📁 Dataset Description

We used a **synthetic E-commerce dataset** consisting of:

| File            | Description                                      |
| --------------- | ------------------------------------------------ |
| users.csv       | Customer details (ID, name, email, city, gender) |
| products.csv    | Product catalog (name, category, brand, price)   |
| orders.csv      | Order-level data                                 |
| order_items.csv | Product-level transaction details                |
| reviews.csv     | Ratings and feedback                             |
| events.csv      | User actions (view, cart, purchase)              |

---

## 🧠 System Architecture

```
User Input (UI)
      ↓
Flask App (app.py)
      ↓
Pipeline Engine
      ↓
Data Loader → Data Merger
      ↓
Product Similarity Engine
      ↓
User Interaction Scoring
      ↓
Feature Engineering
      ↓
ML Model (Best Selected)
      ↓
Target Customer Filtering
      ↓
UI Output (Ranked Customers)
```

---

## ⚙️ Working Flow (Step-by-Step)

### 1. User Input

* Product Name
* Category
* Brand

---

### 2. Product Similarity (NLP)

* Converts product data into text
* Uses **TF-IDF Vectorization**
* Applies **Cosine Similarity**
* Finds top similar products

---

### 3. Interaction Scoring

User behavior is converted into scores:

| Event    | Score |
| -------- | ----- |
| View     | 1     |
| Cart     | 3     |
| Purchase | 5     |

Review ratings add bonus scores.

---

### 4. Feature Engineering

Key features created:

* total_score
* avg order value
* product price

---

### 5. Model Training

Multiple models are trained:

* Logistic Regression
* Random Forest
* Decision Tree

---

### 6. Model Evaluation

Models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score (Primary metric)

---

### 7. Model Selection

* Best model is selected based on **highest F1 Score**
* Saved as:

```
src/models/model.pkl
```

---

### 8. Prediction

* Predict probability of purchase
* Assign probability score to each user

---

### 9. Target Filtering

* Only users with high probability are selected
* Sorted and limited as per user input

---

### 10. UI Output

Displays:

* User ID
* Name
* Email
* Gender
* City
* Probability Score
* Confidence Level (High/Medium/Low)

---

## 🤖 Machine Learning Models Used

| Model               | Purpose                             |
| ------------------- | ----------------------------------- |
| Logistic Regression | Baseline classification             |
| Random Forest       | High accuracy + non-linear patterns |
| Decision Tree       | Fast and interpretable              |

---

## 📊 Evaluation Metrics

| Metric    | Description                        |
| --------- | ---------------------------------- |
| Accuracy  | Overall correctness                |
| Precision | Correct positive predictions       |
| Recall    | Coverage of actual positives       |
| F1 Score  | Balance between Precision & Recall |

👉 **F1 Score is used for final model selection**

---

## 🔥 Key Features

✔ Similarity-based product matching
✔ Behavior-based user scoring
✔ Multi-model evaluation & selection
✔ Real-time prediction pipeline
✔ Robust fallback handling
✔ Clean UI with filters and sorting

---

## ⚠️ Challenges Solved

* Handling unknown product inputs
* Avoiding empty results (fallback mechanism)
* Managing multiple data sources
* Ensuring modular and scalable architecture

---

## 🚀 Future Improvements

* Add deep learning recommendation system
* Real-time API deployment
* Dashboard with analytics (charts)
* User segmentation (clustering)
* Geo-based targeting

---

## 🛠️ Tech Stack

* Python 3.11
* Flask
* Pandas / NumPy
* Scikit-learn
* Bootstrap (UI)

---

## 🧠 Conclusion

This system demonstrates how **machine learning + data engineering + user behavior analysis** can be combined to create a powerful **marketing intelligence system**.

It improves:

* Target accuracy
* Cost efficiency
* Customer engagement

---

## 👨‍💻 Author

Developed as a Mini Project for academic and practical learning purposes.

---
### Data set link
- https://www.kaggle.com/datasets/abhayayare/e-commerce-dataset

---
#### How to run 
1. Train model (once)
  - python main.py train
2. Run prediction pipeline (optional)
  - python main.py run
3. Run UI
 - python app.py

 