import urllib.request
import json
import random
key= 'ab5bf4b0970860437fc442604639d812' # for openweathermap
def create_message():
  url1 ='http://hp-api.herokuapp.com/api/characters'
  request1 = urllib.request.urlopen(url1)
  result1 = json.loads(request1.read())
  
  char = random.randint(1,40) # random niumber for the result
  
  print(result1[char])
  
  city = 'brampton'
  url2 =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}' #url to read brampton weather data, where city = brampton 
  response = urllib.request.urlopen(url2) #fetching url
  result2 = json.loads(response.read())
  print(result2)
  temp_c = result2["main"]["temp"]- 273.15 #temp in Kelvin, so subtracted 273.15 to change to celcius
  
  url3 ='http://api.open-notify.org/astros.json'
  request2 = urllib.request.urlopen(url3)
  result3 = json.loads(request2.read()) #result of space people details
  
  
  message_twi = f'This message is from Space Station by {result3["people"][random.randint(0,9)]["name"]}. His favorite Harry potter character is {result1[char]["name"]}. He says that he can sense the temperature of brampton. The temperature is {temp_c}'
  return(message_twi) #return the message
