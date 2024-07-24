import streamlit as st
import plotly.express as px
import pandas as pd

# 샘플 데이터 생성
df = pd.DataFrame({
    'Parameter': ['Temperature', 'Humidity', 'Pressure'],
    'Value': [22, 55, 1013]
})

# 데이터 시각화
fig = px.bar(df, x='Parameter', y='Value', title='Sample Weather Data')
st.plotly_chart(fig)
