

# 📰 Fake News Detection using Machine Learning

This project detects whether a news article is **Fake or Real** using  
**Natural Language Processing (NLP)** and **Machine Learning** techniques.

It is an end-to-end ML project covering data preprocessing, feature extraction,
model training, evaluation, and optional deployment.

---

## 🎯 Project Objective
To build a machine learning model that can classify news articles as:
- **Real (0)**
- **Fake (1)**  
based on their textual content.

---

## 🧠 Approach Used
1. Text Cleaning & Preprocessing  
2. Feature Extraction using **TF-IDF**
3. Model Training using Linear **Support Vector Machine (SVM)**
4. Model Evaluation using Accuracy, Precision, Recall, and F1-Score
5. Real-world news testing
6. Optional deployment using **Streamlit**

---

## 📊 Dataset
- **WELFake Dataset**
- Source: Kaggle
- Link: https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification

Label format:
- `0` → Real News
- `1` → Fake News

> The dataset is not included in this repository due to file size constraints.

---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- TF-IDF Vectorizer  
- Streamlit (for UI)

---

## 📁 Project Structure


Fake-News-Detection/

├── Fake_News_Detection.ipynb # Main implementation (training + evaluation)

├── app.py # Streamlit app (optional)

├── requirements.txt

├── README.md

└── WELFake_Dataset.csv


📌 **Complete implementation is available in `Fake_News_Detection.ipynb`.**

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

2️⃣ Open the Notebook

```
jupyter notebook Fake_News_Detection.ipynb
```

3️⃣ (Optional) Run Streamlit App
```
streamlit run app.py
```
---
## 📈 Results

- Accuracy: ~95–96%

- Performs well on long-form real news articles

- Uses probability-based predictions

- Avoids aggressive false fake detection
---

## ⚠️ Disclaimer

This model provides probabilistic predictions and should not be treated as
a definitive source for verifying news authenticity.
---
## 🚀 Future Improvements

Use Transformer models like BERT

Add model comparison dashboard

Deploy as a web API

Improve real-time news scraping
---
## 👩‍💻 Author

Nilofar Nadaf

Aspiring Data Analyst / Data Scientist

---
⭐ If you find this project useful, feel free to star the repository!


