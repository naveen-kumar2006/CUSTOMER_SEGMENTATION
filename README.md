# Customer Segmentation using KMeans

## 📌 Project Overview

This project performs **customer segmentation** using **KMeans clustering** to group customers based on their purchasing behavior.
The goal is to identify distinct customer groups so businesses can apply targeted marketing strategies.

---

## 🎯 Problem Statement

Businesses often have large customer bases with different behaviors.
This project groups customers into meaningful segments using:

* Annual Income
* Spending Score

These segments help in:

* Targeted marketing
* Customer retention
* Personalized recommendations

---

## 📊 Dataset

The dataset contains the following features:

* **Annual Income (k$)**
* **Spending Score (1–100)**

(Optional: add dataset source if applicable)

---

## ⚙️ Approach

1. Data preprocessing (scaling)
2. Model selection: KMeans clustering
3. Optimal cluster selection:

   * Elbow Method
   * Silhouette Score
4. Final model trained with **k = 5**

---

## 📈 Model Evaluation

* **Silhouette Score:** 0.559
* Interpretation: Clusters are well-separated and meaningful

---

## 🧠 Customer Segments (Business Meaning)

| Cluster | Segment Name          |
| ------- | --------------------- |
| 0       | Rich but low spenders |
| 1       | Average customers     |
| 2       | Young high spenders   |
| 3       | Premium customers     |
| 4       | High value customers  |

---

## 💼 Business Insights

* **Premium customers** → Focus on retention and loyalty programs
* **High value customers** → Offer exclusive deals and rewards
* **Young high spenders** → Target with ads and trendy products
* **Rich but low spenders** → Provide discounts to increase spending
* **Average customers** → Upsell and cross-sell opportunities

---

## 🖥️ Streamlit Application

An interactive web app is built using Streamlit:

* User inputs:

  * Annual Income
  * Spending Score
* Output:

  * Predicted cluster
  * Business segment
  * Actionable insight

---

## 🚀 How to Run the Project

```bash
# Clone the repository
git clone https://github.com/naveen-kumar2006/CUSTOMER_SEGMENTATION

# Navigate to project folder
cd customer-segmentation

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 📁 Project Structure

```
customer-segmentation/
│── main.py
│── customer_segmentation_model.pkl
│── Mall_Customers.csv
│── jupyternotebook.ipynb
│── README.md
```

---

## 📦 Requirements

* streamlit
* pandas
* scikit-learn
* joblib
* python-version 3.11

---

## 🔮 Future Improvements

* Include additional features (Age, Purchase Frequency)
* Try other clustering methods
* Deploy the app online (Streamlit Cloud)
* Add interactive visualizations

---

## ⭐ Acknowledgment
This project is built as part of learning Machine Learning and Customer Segmentation concepts.

---

## 👤 Author

Naveen Kumar T
[GitHub]:(https://github.com/naveen-kumar2006)
[Email] :mrgnk455@gmail.com
