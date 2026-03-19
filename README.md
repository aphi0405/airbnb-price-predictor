# 🏠 Airbnb Smart Price Predictor (US Market) 🚀

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/Model-LightGBM-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Airbnb Smart Price Predictor** เป็นแอปพลิเคชันวิเคราะห์และพยากรณ์ราคากลางที่เหมาะสมสำหรับที่พักใน 6 เมืองหลักของสหรัฐอเมริกา (NYC, LA, SF, DC, Chicago, Boston) โดยใช้ขุมพลังจาก **Machine Learning (LightGBM)** เพื่อช่วยให้เจ้าของที่พัก (Hosts) สามารถตั้งราคาที่เหมาะสมและวิเคราะห์รายได้เบื้องต้นได้

---

## 🔗 Live Demo
สามารถทดลองใช้งานแอปพลิเคชันเวอร์ชันออนไลน์ได้ที่นี่:
👉 **[Airbnb Price Predictor Web App](https://airbnb-price-predictor-nhqfezkakhhj2u4rssbhzm.streamlit.app/)**

---

## ✨ Key Features
* **AI Price Prediction:** คำนวณราคากลางรายคืนโดยอิงจากปัจจัยจริง เช่น ทำเล (Latitude/Longitude), ประเภทห้อง, จำนวนผู้เข้าพัก และคะแนนรีวิว
* **Business Insights:** วิเคราะห์รายได้คาดการณ์รายเดือนเปรียบเทียบกับเป้าหมายรายได้ (Monthly Revenue Goal)
* **Interactive Dashboard:** ใช้งานง่ายผ่าน Web Interface พร้อมแผนที่แสดงตำแหน่งที่พักจริง
* **Confidence Score:** แสดงค่าความแม่นยำของโมเดลประกอบการตัดสินใจ

---

## 📊 Dataset Reference
ข้อมูลที่ใช้ในการพัฒนาโปรเจกต์นี้มาจาก Kaggle:
* **Dataset:** [Airbnb Price Prediction Dataset](https://www.kaggle.com/datasets/stevezhenghp/airbnb-price-prediction)
* **Timeframe:** ข้อมูล Snapshot ในช่วงปี 2017 ซึ่งเป็นช่วงที่ตลาด Airbnb มีความเสถียรและเหมาะสมกับการสร้าง Model พื้นฐาน

---

## 🧠 Model Performance
โปรเจกต์นี้ผ่านกระบวนการทำ Data Cleaning, EDA และ Hyperparameter Tuning อย่างละเอียด
* **Model:** LightGBM Regressor
* **Accuracy (R-squared):** **71.24%** 🎯
* **Pre-processing:** Log Transformation (Target Variable) และ StandardScaler (Features)

---

## 🛠️ Tech Stack
* **Language:** Python
* **Data Science:** Pandas, NumPy, Scikit-learn, LightGBM
* **Web Framework:** Streamlit
* **Deployment:** Streamlit Cloud

---

## 📂 Project Structure
```text
├── app.py                # ไฟล์หลักสำหรับรัน Streamlit Web App
├── requirements.txt      # รายการ Libraries ที่ต้องใช้
├── README.md             # เอกสารอธิบายโปรเจกต์
├── models/               # โฟลเดอร์เก็บไฟล์ Model และ Scaler
│   ├── airbnb_price_model.pkl
│   ├── data_scaler.pkl
│   └── model_columns.pkl
├── notebooks/            # โฟลเดอร์เก็บขั้นตอนการวิเคราะห์และเทรนโมเดล
│   └── 67160383_Airbnb_project.ipynb
└── assets/               # รูปภาพประกอบแอป
    ├── house.png
    └── 25694.png

-----

## 🚀 Installation & Local Setup

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/aphi0405/airbnb-price-predictor.git](https://github.com/aphi0405/airbnb-price-predictor.git)
    cd airbnb-price-predictor
    ```

2.  **Create and Activate Virtual Environment:**

    ```bash
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

## 👩‍💻 Developed by

  * **67160383 Aphisara Klayburee** 
  * GitHub: [@aphi0405](https://www.google.com/search?q=https://github.com/aphi0405)

-----

*Disclaimer: ข้อมูลราคาเป็นการพยากรณ์จากสถิติเบื้องต้นเพื่อใช้ประกอบการตัดสินใจเท่านั้น*

```
