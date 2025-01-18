from flask import Flask, request, jsonify, render_template
import paho.mqtt.publish as publish
import json

app = Flask(__name__)

# Địa chỉ IP của Raspberry Pi hoặc PC nhận dữ liệu (MQTT Broker)
MQTT_BROKER = "192.168.0.100"  # Địa chỉ IP của PC nhận dữ liệu

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    message = data.get("message")
    if not message or "status" not in message:
        return jsonify({"error": "Không có trạng thái động cơ được cung cấp"}), 400

    try:
        # Chuyển đổi đối tượng message thành chuỗi JSON
        message_json = json.dumps(message)

        # Gửi tin nhắn qua MQTT
        publish.single("MQTT_DongCo_DCs2", message_json, hostname=MQTT_BROKER)
        return jsonify({"success": True, "message": "Trạng thái động cơ đã được cập nhật!"})
    except Exception as e:
        return jsonify({"error": f"Không thể gửi tin nhắn: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)