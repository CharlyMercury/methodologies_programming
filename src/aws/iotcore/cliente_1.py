from aws_client import AwsMqttClient
import threading

received_all_event = threading.Event()

endpoint = "a1svajesngnqg2-ats.iot.us-east-1.amazonaws.com"
port = 443
cert = r"./certificates/device_cert.pem.crt"
key = r"./certificates/private.pem.key"
ca = r"./certificates/AmazonRootCA1.pem"
client_id = "thing_esp32"
topics_subs = [
    f'sensors']

mqtt_client = AwsMqttClient(endpoint, port, cert, key, ca, client_id, topics_subs)
mqtt_client.subscribe_to_topics()

# received_all_event.wait()
# print("{} message(s) received.")

while True:
    pass
    
# Disconnect
print("Disconnecting...")
disconnect_future = mqtt_client.mqtt_connection.disconnect()
disconnect_future.result()
print("Disconnected!")