import paho.mqtt.client as mqtt


# Se llama a esta función cuando el cliente se quiere conectar al broker 
# También se hacen las suscripciones a tópicos
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect

mqttc.connect("192.168.0.104", 1883, 60)
mqttc.publish("temperatura1", "DESDE PYTHON")