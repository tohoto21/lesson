import json
import requests
def get_course(valute):
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = json.loads(response.text)
    #print(data['Valute'][valute]['Value'])
    return {
   "currency": valute,

    "rub_course": data['Valute'][valute]['Value']
    }#data['Valute'][valute]['Value']



get_course('USD')