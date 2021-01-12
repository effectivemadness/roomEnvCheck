from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
@app.route('/update', methods=['POST'])
def update():
    content = request.json
    print(content)
    currentTime = datetime.now()
    timeText = currentTime.strftime("%Y%m%d_%H:%M:%S")
    tempHumidText = str(content['temp'])+', '+str(content['humid'])
    with open('data.csv','a') as file_data:
        print(timeText+', '+tempHumidText,file=file_data)
    return timeText+', '+tempHumidText
@app.route('/')
def home():
    with open('data.csv','r') as file_data:
        lines = file_data.read().splitlines()
        last_line = lines[-1]
    timeText, tempText, humidText = last_line.split(', ')
    return render_template("index.html", temp=tempText, humid=humidText, time=timeText)
if __name__ == '__main__':
    app.run(debug=True)