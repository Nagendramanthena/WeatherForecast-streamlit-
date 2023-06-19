import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next few days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecasted days")
option = st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
if place:
    filtered_data = get_data(place,days)
    if filtered_data == None:
        st.error('No such city in our db', icon="🚨")
    elif option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        list = []
        for t in temperatures:
            list.append(t-273)
        d = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=d,y=list,labels={"x":"Date","y":"Temperature(C)"})
        st.plotly_chart(figure)
        st.success(f'Forecast for next {days} days!', icon="✅")
    else:
        images = {"Clear":"images/clear.png","Clouds":"images/cloud.png",
                  "Rain":"images/rain.png","Snow":"images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images_paths = [images[condition] for condition in sky_conditions]
        st.success(f'Forecast for next {days} days!', icon="✅")
        st.image(images_paths,width=115)
