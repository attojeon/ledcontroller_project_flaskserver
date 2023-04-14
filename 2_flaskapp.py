from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_cors import CORS

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_P = 25
GPIO.setup(LED_P, GPIO.OUT)
LED_S = 'on'

def led_on():
    global LED_S
    print(">>> led light on!")
    GPIO.output(LED_P, True)
    LED_S = 'on'


def led_off():
    global LED_S
    print("   <<< led light off!")
    GPIO.output(LED_P, False)
    LED_S = 'off'

def set_data(onoff):
    data = {
        "result": [
            {
                "led": onoff
            },
            {
                "led": "off"
            }
        ]
    }

    return data 


app = Flask(__name__)
CORS(app)  # CORS 설정


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/led")
def start():
    data = set_data( LED_S)
    print(f">>> {data}")
    return jsonify(data)  # 값을 반환해주어야 합니다.


@app.route("/led_onoff")
def led_onoff():
    sw = request.args.get('sw')
    print(f">>> sw:{sw}")
    if sw == 'on':
        led_on()
    elif sw == 'off':
        led_off()
    # else:
    #     print(" >>>>>>>>>> frontend msg : not expected!!!")

    # data = {"result": LED_S}
    data = set_data( LED_S)
    return jsonify(data)  # 값을 반환해주어야 합니다.


app.debug = True
app.run(host="0.0.0.0", port=8000)
