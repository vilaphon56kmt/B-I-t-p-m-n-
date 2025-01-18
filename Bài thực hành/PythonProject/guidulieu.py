import paho.mqtt.client as mqtt
from datetime import datetime
import json
import random
import time

# Cấu hình MQTT
MQTT_BROKER = "192.168.0.103"  # Địa chỉ MQTT Broker
MQTT_PORT = 1883
MQTT_TOPIC = "vilaphon"  # Tên topic
CLIENT_ID = "Python_Client"  # ID client

# Hàm xử lý khi kết nối thành công
def on_connect(client, userdata, flags, rc):
    print(f"Kết nối thành công với mã: {rc}")

# Tạo client MQTT
client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
client.on_connect = on_connect

# Kết nối tới broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Hàm gửi dữ liệu
def publish_data():
    while True:
        data = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": random.randint(1, 100)  # Giá trị random
        }
        client.publish(MQTT_TOPIC, json.dumps(data))
        print(f"Đã gửi: {data}")
        time.sleep(2)  # Gửi mỗi 2 giây

# Chạy chương trình
try:
    client.loop_start()
    publish_data()
except KeyboardInterrupt:
    client.loop_stop()
    print("Dừng chương trình.")