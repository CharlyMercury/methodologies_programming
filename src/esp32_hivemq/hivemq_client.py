import os
import time
import ujson
import dht
from machine import Pin
import network
from simple import MQTTClient
import mh_z19

wifi_ssid = "Totalplay-2.4G-fee0"
wifi_password = "UUuQkjdK56LGPyjX"

hivemq_endpoint = "608359e51bfa42d5a47f3d14c8f5d47f.s1.eu.hivemq.cloud"
client_id = "embedded_client_001"
username = "foco_sala"
password = "Bob22esponja"

topic_pub = "sensors"
topic_sub = "led"

dht_temp_hum = dht.DHT11(Pin(4))
led = Pin(2, Pin.OUT)
info = os.uname()

mhz = mh_z19.MHZ19(17, 16)
mhz.set_detection_range(5000)
mhz.read_co2()
mhz.read_co2_continuous(5000)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('Connecting to network...')
    wlan.connect(wifi_ssid, wifi_password)
    while not wlan.isconnected():
        pass
    print('Connected:', wlan.ifconfig())

def mqtt_connect():
    mqtt = MQTTClient(
        client_id=client_id,
        server=hivemq_endpoint,
        port=8883,
        user=username,
        password=password,
        keepalive=60,
        ssl=True  # <--- TLS connection (needed for port 8883)
    )
    print("Connecting to HiveMQ...")
    mqtt.connect()
    print("Connected!")
    return mqtt

def mqtt_publish(client, topic=topic_pub, message=''):
    print("Publishing message...")
    client.publish(topic, message)
    print(message)

def mqtt_subscribe(topic, msg):
    print("Message received:")
    message = ujson.loads(msg)
    print(topic, message)
    if message['state']['led']:
        led_state(message)

def led_state(message):
    print(message['state']['led']['onboard'])
    led.value(message['state']['led']['onboard'])

try:
    mqtt = mqtt_connect()
    mqtt.set_callback(mqtt_subscribe)   
    mqtt.subscribe(topic_sub)
except Exception as err:
    print("Unable to connect to HiveMQ.", err)

while True:
    try:
        mqtt.check_msg()
    except:
        print("Unable to check for messages.")
    
    dht_temp_hum.measure() 
    mhz.update()
    mesg = ujson.dumps({
        "state": {
            "reported": {
                "device": {
                    "client": client_id,
                    "uptime": time.ticks_ms(),
                    "hardware": info[0],
                    "firmware": info[2]
                },
                "sensors": {
                    "humidity": dht_temp_hum.humidity(),
                    "temperature": dht_temp_hum.temperature(),
                    "co2": mhz.get_co2()
                },
                "led": {
                    "onboard": led.value()
                }
            }
        }
    })

    try:
        mqtt_publish(client=mqtt, message=mesg)
    except:
        print("Unable to publish message.")
    
    print("Sleeping for 10 seconds...")
    time.sleep(10)
