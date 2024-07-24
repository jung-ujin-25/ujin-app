import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# OpenWeatherMap API 키 설정
API_KEY = 'YOUR_API_KEY'  # 실제 API 키로 교체하세요

# 사용자 입력 받기
st.title('날씨 데이터 분석')
city = st.text_input('도시 이름을 입력하세요:', 'Seoul')

# API 호출 함수
def get_weather_data(city, API_KEY):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API 요청 중 오류가 발생했습니다: {e}")
        return None

# 데이터 가져오기
weather_data = get_weather_data(city, API_KEY)

# 데이터 프레임으로 변환
if weather_data and weather_data.get('main'):
    df = pd.DataFrame({
        'Parameter': ['Temperature', 'Humidity', 'Pressure'],
        'Value': [weather_data['main']['temp'], weather_data['main']['humidity'], weather_data['main']['pressure']]
    })

    # 데이터 시각화
    fig = px.bar(df, x='Parameter', y='Value', title=f'{city} 날씨 정보')
    st.plotly_chart(fig)

    # 추가 정보 표시
    st.subheader('추가 날씨 정보')
    st.write(f"날씨 상태: {weather_data['weather'][0]['description']}")
    st.write(f"풍속: {weather_data['wind']['speed']} m/s")
    st.write(f"일출 시간: {pd.to_datetime(weather_data['sys']['sunrise'], unit='s')}")
    st.write(f"일몰 시간: {pd.to_datetime(weather_data['sys']['sunset'], unit='s')}")
else:
    st.error('도시 이름을 다시 확인하세요.')
