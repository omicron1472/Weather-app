import requests
import streamlit as st
from dotenv import load_dotenv
import base64
import os

load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')


st.set_page_config(
    page_title="Weather App",
    page_icon="🌦️",
    layout="wide"
)

# Read background image
with open("background7.png", "rb") as file:
    encoded = base64.b64encode(file.read()).decode()

# Apply background
st.markdown(f"""
<style>

.stApp {{
    background-image: url("data:image/png;base64,{encoded}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

</style>
""", unsafe_allow_html=True)

# # App content
# st.title("🌦️ Weather App")


st.set_page_config(page_title='Weather App',page_icon='❄')
st.title('🌦️Weather App')
st.write('Enter the City Name and Click on the button to get the Weather Data')


# if(len(city) == 0):
#  st.warning('Enter the Valid City Name')

# city = st.text_input('Enter the city name')
# Button = st.button('Fetch Weather Data')
# Row A
# colA, colB = st.columns(2)

# with colA:
#     city = st.text_input("Enter the city name")

# with colB:
#     Button1 = st.button("Fetch Weather Data")


col1, col2 = st.columns([9, 4], vertical_alignment="bottom")

with col1:
    city = st.text_input(
        "Enter the city name",
        placeholder="e.g. Nashik"
    )

with col2:
    Button1 = st.button(
        "Fetch Weather Data",
        use_container_width=True
    )



API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

if(Button1):
              response = requests.get(API_URL)

              if(response.status_code == 200):
                            st.success('✅ Weather data fetched successfully!')
                            data = response.json()
                            # print(data)

                            #Extract the Weather Data in variables
                            temperature = data['main']['temp']
                            Humidity = data['main']['humidity']
                            Wind_speed = data['wind']['speed']
                            Weather = data['weather'][0]['main']
                            Pressure = data['main']['pressure']
                            Description = data['weather'][0]['description']  
                            Country = data['sys']['country']
                            Name = data['name']

                            #print(temperature, Humidity, Wind_speed, Weather, Pressure)
                            #It is displayed in terminal.
                            
                            st.subheader(f'Weather for {Name}, {Country}')

                            # Row 1
                            col1, col2= st.columns(2)

                            col1.metric('Temperature', f'🌡️{temperature}°C')
                            col2.metric('Humidity', f'💦{Humidity}%')
                            
                            # Row 2
                            col3, col4 = st.columns(2)

                            col3.metric('Wind Speed', f'🍃{Wind_speed} m/s')
                            col4.metric('Pressure', f'💨{Pressure} millibars (mb)')
                            
                            # Row 3
                            col5, col6 = st.columns(2)

                            col5.metric('Weather', f'🌤️{Weather}')
                            col6.metric('Description', Description)
              else:
                            st.error('❌ City Not Found')

              