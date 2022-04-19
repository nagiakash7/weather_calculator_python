import requests,json 

api_key= 'f766200f6843771024be40f6357b641e'
city_name=input("enter the city  \t")

url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

obj=requests.get(url)



x= obj.json()

print(x["main"]["temp"])