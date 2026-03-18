# 🏠 Airbnb Smart Price Predictor (US Market) 🚀

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/Model-LightGBM-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Airbnb Smart Price Predictor** เป็นแอปพลิเคชันวิเคราะห์และพยากรณ์ราคากลางที่เหมาะสมสำหรับที่พักในสหรัฐอเมริกา (NYC, LA, SF, DC, Chicago, Boston) โดยใช้ขุมพลังจาก **Machine Learning (LightGBM)** เพื่อช่วยให้เจ้าของที่พัก (Hosts) สามารถตั้งราคาแข่งขันในตลาดได้อย่างมีประสิทธิภาพ

---

## ✨ Key Features
* **AI Price Prediction:** คำนวณราคากลางรายคืนโดยอิงจากปัจจัยจริง เช่น ทำเล, ประเภทห้อง, จำนวนผู้เข้าพัก และรีวิว
* **Business Insights:** วิเคราะห์รายได้คาดการณ์รายเดือนเปรียบเทียบกับเป้าหมาย (Business Goal)
* **Interactive Dashboard:** ใช้งานง่าย พร้อมแผนที่แสดงทำเลที่ตั้งแบบ Real-time
* **Confidence Score:** แสดงค่าความเชื่อมั่นของโมเดล เพื่อความโปร่งใสในการตัดสินใจ

---

## 🧠 Model Performance
โปรเจกต์นี้ผ่านการเทรนและปรับจูนโมเดล (Hyperparameter Tuning) อย่างละเอียดจนได้ผลลัพธ์ที่น่าพอใจ:
* **Model:** LightGBM Regressor
* **Accuracy (R-squared):** **71.24%** 🎯
* **Validation:** 5-Fold Cross-Validation
* **Optimization:** RandomizedSearchCV



---

## 🛠️ Tech Stack
* **Language:** Python
* **Data Science:** Pandas, NumPy, Scikit-learn, LightGBM
* **Web Framework:** Streamlit
* **Deployment Assets:** Joblib (Model & Scaler Serialization)

---

## 🚀 Installation & Local Setup

หากต้องการรันโปรเจกต์นี้บนเครื่องของคุณเอง ให้ทำตามขั้นตอนดังนี้:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aphi0405/airbnb-price-predictor.git](https://github.com/aphi0405/airbnb-price-predictor.git)
   cd airbnb-price-predictor
   ````

2.  **Create and Activate Virtual Environment:**

    ```bash
    # For Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**

    ```bash
    streamlit run app.py
    ```

-----

## 📂 Project Structure

```text
├── app.py                  # Streamlit Web Application
├── airbnb_price_model.pkl   # Trained LightGBM Model
├── data_scaler.pkl          # Scaled numeric data (StandardScaler)
├── model_columns.pkl        # List of features used in training
├── requirements.txt         # Required Python libraries
└── README.md                # Project documentation
```

-----

## 👩‍💻 Developed by

  * **Aphisara Klayburee** (Software Developer / Data Science Enthusiast)
  * GitHub: [@aphi0405](https://www.google.com/search?q=https://github.com/aphi0405)

-----

*Disclaimer: ข้อมูลราคาเป็นการพยากรณ์จากสถิติเบื้องต้นเพื่อใช้ในการตัดสินใจเท่านั้น*

```

---
