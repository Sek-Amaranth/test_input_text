import streamlit as st
import requests

# === UI Streamlit ===
st.title("ระบบ ส่งข้อมูลไป Google Sheet")

name = st.text_input("ชื่อ")
email = st.text_input("อีเมล")
submit = st.button("ส่ง")

# === ส่งข้อมูลไป Google Apps Script ===
if submit:
    if name and email:
        url = "https://script.google.com/macros/s/AKfycbxrNH8T-D-Fkwphrpy9TQQfJCxPsP7Du-bIbztjgiLVt6QXZEWxX7GCMKOxD8U_PTgitQ/exec"  # ใส่ URL Web App ที่ได้
        payload = {"name": name, "email": email}
        try:
            res = requests.post(url, json=payload)
            if res.status_code == 200:
                st.success("ส่งข้อมูลเรียบร้อย")
            else:
                st.error(f"ผิดพลาด: {res.text}")
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")
    else:
        st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
