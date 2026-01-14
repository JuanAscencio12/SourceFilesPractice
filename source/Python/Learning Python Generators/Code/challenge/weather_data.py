from datetime import datetime

data =[
    {
        "country": "Somalia",
        "temp": "88",
        "date": "4/5/2046",
        "wind_speed": "23.64mph",
    }
]

def clean_data(data):
    for info in data:
        cleaned = {}
        cleaned["country"] = info["country"]
        cleaned["temp"] = int(info["temp"])
        cleaned["temp"] = datetime.strptime(info["date"], "%m/%d/%Y")
        cleaned["wind_speed"] = float(info["wind_speed"].replace("mph",""))
        yield cleaned

def main():
    print(list(clean_data(data)))

if __name__ == "__main__":
    main()