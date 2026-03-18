import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

# --- 1. CONFIG ---
st.set_page_config(
    page_title="Airbnb Smart Predictor Pro",
    page_icon="🏠",
    layout="wide"
)

# --- 2. LOAD ASSETS ---
@st.cache_resource
def load_assets():
    model = joblib.load('models/airbnb_price_model.pkl')
    scaler = joblib.load('models/data_scaler.pkl')
    model_columns = joblib.load('models/model_columns.pkl')
    return model, scaler, model_columns

try:
    model, scaler, model_columns = load_assets()
except Exception as e:
    st.error(f"🚨 Error: {e}")
    st.stop()

# --- 3. DYNAMIC STYLING ---
st.markdown("""
    <style>
    /* ปุ่มพยากรณ์ราคา */
    div.stButton > button:first-child {
        background-color: #FF5A5F;
        color: white;
        border-radius: 12px;
        border: none;
        height: 60px;
        width: 100%;
        font-size: 20px;
        font-weight: bold;
    }
    /* กล่องผลลัพธ์การทำนาย */
    .result-box {
        padding: 2rem;
        border-radius: 15px;
        border-left: 10px solid #FF5A5F;
        background-color: rgba(255, 90, 95, 0.1);
        margin-top: 1rem;
    }
    /* กล่อง About Project (Text Box) ใน Sidebar */
    .about-box {
        background-color: rgba(255, 255, 255, 0.1); /* ปรับให้เห็นเป็นกล่องชัดเจนขึ้น */
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        color: inherit;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.image("https://icons.veryicon.com/png/o/miscellaneous/home-icon-1/house-30.png", width=100)
    
    st.markdown("### ⚙️ Business Strategy")
    monthly_goal = st.number_input("เป้าหมายรายได้ต่อเดือน ($)", value=3000, step=100)
    
    st.markdown("---")
    st.success("Model Status: Online ✅")
    
    # ส่วน About Project ในรูปแบบ Text Box ที่ชัดเจน
    st.markdown(f"""
    <div class='about-box'>
        <h4 style='margin-top:0;'>📖 About Project</h4>
        <p style='font-size: 0.9rem; opacity: 0.8;'>
        ระบบ AI วิเคราะห์ราคาที่พักรายคืน พัฒนาขึ้นเพื่อช่วยเจ้าของที่พักประเมินมูลค่าตลาดในสหรัฐอเมริกา โดยคำนวณจากสถิติและปัจจัยแวดล้อมจริง
        </p>
        <hr style='opacity: 0.2; margin: 10px 0;'>
        <b style='font-size: 0.85rem;'>How it works:</b><br>
        <span style='font-size: 0.8rem; opacity: 0.7;'>
        • Input: รายละเอียดที่พัก<br>
        • AI: LightGBM ML Model<br>
        • Result: ราคาแนะนำ & Insights
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("Developed by 67160383 Aphisara")

# --- 5. MAIN UI ---
st.title("🏠 Airbnb Smart Pricing Dashboard")
st.write("วิเคราะห์ราคากลางที่เหมาะสมด้วยระบบ **AI** สำหรับที่พักในสหรัฐอเมริกา")

input_col1, input_col2 = st.columns([2, 1], gap="large")

with input_col1:
    st.subheader("📍 Location & Property")
    c1, c2, c3 = st.columns(3)
    with c1:
        city = st.selectbox("เมืองที่ตั้ง", ['NYC', 'LA', 'SF', 'DC', 'Chicago', 'Boston'])
    with c2:
        room_type = st.selectbox("รูปแบบการเช่า", ['Entire home/apt', 'Private room', 'Shared room'])
    with c3:
        prop_type = st.selectbox("ประเภทอาคาร", ['Apartment', 'House', 'Condominium', 'Townhouse', 'Loft'])
    
    st.subheader("🛏️ Capacity & Reviews")
    c4, c5, c6 = st.columns(3)
    with c4:
        accommodates = st.slider("จำนวนผู้เข้าพัก", 1, 16, 2)
    with c5:
        bedrooms = st.number_input("ห้องนอน", 0, 10, 1)
    with c6:
        bathrooms = st.number_input("ห้องน้ำ", 0, 8, 1, 1)

    reviews = st.number_input("จำนวนรีวิวสะสม", 0, 1000, 20)

# เตรียมพิกัด
city_coords = {'NYC': [40.7128, -74.0060], 'LA': [34.0522, -118.2437], 'SF': [37.7749, -122.4194], 'DC': [38.9072, -77.0369], 'Chicago': [41.8781, -87.6298], 'Boston': [42.3601, -71.0589]}
lat, lon = city_coords[city]

# --- 6. PREDICTION ---
with input_col2:
    st.subheader("⚡ AI Analysis")
    if st.button("RUN PREDICTION 🚀"):
        with st.spinner('กำลังคำนวณ...'):
            time.sleep(0.8)
            
            input_df = pd.DataFrame(columns=model_columns)
            input_df.loc[0] = 0 
            input_df['accommodates'] = accommodates
            input_df['bedrooms'] = bedrooms
            input_df['bathrooms'] = bathrooms
            input_df['number_of_reviews'] = reviews
            input_df['latitude'] = lat
            input_df['longitude'] = lon
            input_df['review_scores_rating'] = 95.0
            
            if 'beds' in input_df.columns: input_df['beds'] = accommodates 

            if f'city_{city}' in input_df.columns: input_df[f'city_{city}'] = 1
            if f'room_type_{room_type}' in input_df.columns: input_df[f'room_type_{room_type}'] = 1
            if f'property_type_{prop_type}' in input_df.columns: input_df[f'property_type_{prop_type}'] = 1

            numeric_cols = ['accommodates', 'bathrooms', 'bedrooms', 'beds', 'latitude', 'longitude', 'number_of_reviews', 'review_scores_rating']
            input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])
            
            final_price = np.exp(model.predict(input_df))[0]
            
            st.balloons()
            st.markdown(f"""
                <div class="result-box">
                    <h4 style='margin:0;'>ราคาแนะนำต่อคืน</h4>
                    <h1 style='color: #FF5A5F; margin:0;'>${final_price:.2f}</h1>
                </div>
            """, unsafe_allow_html=True)
            
            st.write(f"**ความเชื่อมั่นโมเดล:** 71.24%")
            st.progress(0.71)
            
            est_monthly = final_price * 20
            st.metric("คาดการณ์รายได้รายเดือน", f"${est_monthly:,.2f}")
            
            if est_monthly >= monthly_goal:
                st.success("เป้าหมาย: สำเร็จ! 🎉")
            else:
                st.warning(f"ขาดอีก ${monthly_goal - est_monthly:,.2f} ถึงเป้าหมาย")
    else:
        st.info("กรุณากดปุ่มเพื่อดูผลลัพธ์")

# --- 8. FOOTER (เพิ่มหัวข้อ Map) ---
st.markdown("---")
st.subheader(f"🗺️ Location Insights: {city}") # เพิ่มหัวข้อแผนที่
st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))
st.caption("Powered by LightGBM | AirBnB Market Analytics")