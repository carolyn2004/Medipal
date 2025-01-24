import time
import requests
import serial
# Establish serial communication with micro:bit; replace with your serial port
# Note: 115200 is the baud rate for micro:bit
ser = serial.Serial('COM9', 115200)  
# API URL for updating ThingSpeak channel
url3 = "https://api.thingspeak.com/update.json"
api_key = 'F167Q5TKU3V2BDWG' # Replace with your API key for the new lab8_2 channel
api_key_1 = 'SWUIIJE32IWHHY7A'
# Continuously read data from micro:bit
while True:
    # Read temperature value from micro:bit
  mbit_data = ser.readline()
  print(mbit_data)
  value = mbit_data.decode().strip()  # Convert bytes to string and strip leading/trailing whitespace
  # check if : is in the string
  if ":" in value:
    value1 = value.split(":")[1] # Split the string by ':', extract the second element (the temperature value).
    name = value.split(":")[0]
    print(value1)
    print(name)
  else:
    print('Serial data not in correct format')
    # Read light value from micro:bit
  
  if name == 'value':
    datastring = {'api_key':api_key, 'field1':value1}
    response = requests.post(url3, data=datastring)
    with open(r"data_page.html", "a") as indexfile:
    # "a" stands for append
    # this is a relative path 
      indexfile.write('<tr><td>'+value1+'</td><td>'+time.ctime(time.time())+'</td></tr>\n')
  elif name == 'temp':
    datastring = {'api_key':api_key_1, 'field1':value1}
    response = requests.post(url3, data=datastring)
  print(f"Sent data {datastring} to {url3}, got status code {response.status_code}")
  # *lab8_3* Append temperature, light data, and timestamp to index.html


