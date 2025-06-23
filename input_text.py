import streamlit as st
import requests
import pandas as pd
import math

# === URL ของ Web App จาก Google Apps Script ===
URL = "https://script.google.com/macros/s/AKfycbxrNH8T-D-Fkwphrpy9TQQfJCxPsP7Du-bIbztjgiLVt6QXZEWxX7GCMKOxD8U_PTgitQ/exec"  # ใส่ของคุณตรงนี้

# ดึงข้อมูล
try:
    res = requests.get(URL)
    data = res.json()  # ได้เป็น list of rows
except Exception as e:
    st.error(f"โหลดข้อมูลไม่สำเร็จ: {e}")
    st.stop()

# สร้าง DataFrame
df = pd.DataFrame(data, columns=["Timestamp", "Name", "Email", "Work", "Status", "Remark"])  # ตั้งชื่อคอลัมน์ตาม sheet

# === แสดงข้อมูลแบบแบ่งหน้า ===
items_per_page = 10
total_rows = len(df)
total_pages = math.ceil(total_rows / items_per_page)

# เลือกหน้า
page = st.number_input("เลือกหน้าที่ต้องการ", min_value=1, max_value=total_pages, step=1)

start_idx = (page - 1) * items_per_page
end_idx = start_idx + items_per_page
st.write(f"แสดงข้อมูลแถวที่ {start_idx + 1} ถึง {min(end_idx, total_rows)} จากทั้งหมด {total_rows} แถว")

# แสดงตาราง
st.dataframe(df.iloc[start_idx:end_idx].reset_index(drop=True))
