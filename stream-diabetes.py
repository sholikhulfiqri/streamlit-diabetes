import pickle 
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Diabetes')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.number_input('Input Nilai Pregnancies')

with col2 :
    Glucose = st.number_input('Input Nilai Glucose')

with col1 :
    BloodPressure = st.number_input('Input Nilai BloodPressure')

with col2 :
    SkinThickness = st.number_input('Input Nilai SkinThickness')

with col1 :
    Insulin = st.number_input('Input Nilai Insulin')

with col2 :
    BMI = st.number_input('Input Nilai BMI')

with col1 :
    DiabetesPedigreeFunction = st.number_input('Input Nilai DiabetesPedigreeFunction')

with col2:
    Age = st.number_input('Input Nilai Age')

#code untuk prediksi
diabetes_diagnosis = ''

#membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
    if(diabetes_prediction[0] == 1):
        diabetes_diagnosis = 'Pasien Terkena Diabates'
    else:
        diabetes_diagnosis = 'Pasien Tidak Terkena Diabetes'        
    
    st.success(diabetes_diagnosis)
