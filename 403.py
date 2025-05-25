import streamlit as st
import time
st.title('my progress')
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)
import streamlit as st
if st.button('Click me'):
    st.balloons()
st.title("giới thiệu bản thân")
name = st.text_input("Họ và tên: ")
st.write("Xin chào: ", name)
birthday = st.text_input("Ngày sinh: ")
st.write("Ngày sinh của mình là: ", birthday)
subject = st.text_input("Môn học yêu thích: ")
st.write("Môn học yêu thích của mình là: ", subject)
hobbies = st.text_input("Sở thích: ")
st.write("Sở thích của mình là: ", hobbies)
