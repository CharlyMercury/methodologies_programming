from aws_client import AwsMqttClient

endpoint = "a1svajesngnqg2-ats.iot.us-east-1.amazonaws.com"
port = 443
cert = r"test_thing.cert.pem"
key = r"test_thing.private.key"
ca = r"root-CA.crt"
client_id = "access_control"
topics_subs = [
    f'temperatura']

mqtt_client = AwsMqttClient(endpoint, port, cert, key, ca, client_id, topics_subs)
mqtt_client.subscribe_to_topics()

while 


# Disconnect
print("Disconnecting...")
disconnect_future = mqtt_client.mqtt_connection.disconnect()
disconnect_future.result()
print("Disconnected!")