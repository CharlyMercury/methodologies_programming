import paho.mqtt.client as mqtt


# Se llama a esta función cuando el cliente se quiere conectar al broker 
# También se hacen las suscripciones a tópicos
def on_connect(client, reason_code):
    print(f"Connected with result code {reason_code}")
    client.subscribe("temperatura/cuarto1")
    client.subscribe("temperatura/cuarto2")


# Se llama esta función cuando llega un mensaje a la suscripción
def on_message(client, msg):
    print(client, msg.topic+" "+str(msg.payload))


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)
mqttc.loop_forever()
