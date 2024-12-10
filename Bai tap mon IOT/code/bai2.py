import cherrypy
from sense_emu import SenseHat
import time

# Khởi tạo Sense HAT
sense = SenseHat()

class Dashboard:
    def __init__(self):
        self.temp = 0
        self.humidity = 0
        self.name_to_display = ""

    # Trang chính
    @cherrypy.expose
    def index(self):
        self.get_environment_data()
        return f"""
        <html>
            <head><title>Sense HAT Dashboard</title></head>
            <body>
                <h1>Sense HAT Dashboard</h1>
                
                <h2>📊 Thông tin Môi Trường</h2>
                <p><b>Nhiệt độ:</b> {self.temp:.1f} °C</p>
                <p><b>Độ ẩm:</b> {self.humidity:.1f}%</p>
                
                <h2>💬 Hiển thị tên của bạn trên LED Matrix</h2>
                <form method="POST" action="/display_name">
                    <label>Nhập tên của bạn: </label>
                    <input type="text" name="name" required>
                    <input type="submit" value="Hiển thị tên">
                </form>
                
                <h2>🎮 Trạng thái Joystick</h2>
                <p>Tương tác joystick mô phỏng trong Sense HAT.</p>
            </body>
        </html>
        """

    # Hiển thị tên trên LED Matrix
    @cherrypy.expose
    def display_name(self, name):
        self.name_to_display = name
        sense.show_message(name, scroll_speed=0.05, text_colour=[255, 0, 0])
        return f"<h2>✅ Tên '{name}' hiển thị trên LED Matrix!</h2><a href='/'>Quay lại</a>"

    # Lấy thông tin nhiệt độ và độ ẩm
    def get_environment_data(self):
        self.temp = sense.get_temperature()
        self.humidity = sense.get_humidity()


# Khởi chạy server CherryPy
if __name__ == "__main__":
    cherrypy.quickstart(Dashboard())
