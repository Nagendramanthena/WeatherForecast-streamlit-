import requests
def get_data(place,forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid=a59949a0706f0c7e2db0de86e1de08cd"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == "404":
        return None
    filtered_data = data["list"]
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    # sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
    # print(sky_conditions)
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Hxx",forecast_days=2))