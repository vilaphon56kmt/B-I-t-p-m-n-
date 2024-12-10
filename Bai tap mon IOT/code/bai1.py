from sense_emu import SenseHat
import time

# Khởi tạo Sense HAT
sense = SenseHat()

# Hiển thị tên trên LED Matrix
def display_name(name):
    sense.show_message(name, scroll_speed=0.05, text_colour=[255, 0, 0])

# Đọc và hiển thị thông tin nhiệt độ, độ ẩm
def display_environment():
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    print(f"Nhiệt độ: {temp:.1f}°C")
    print(f"Độ ẩm: {humidity:.1f}%")

# Xử lý sự kiện joystick
def joystick_event(event):
    if event.action == "pressed":
        print(f"Joystick {event.direction} được nhấn")

# Gắn sự kiện joystick
sense.stick.direction_any = joystick_event

# Hiển thị thông tin liên tục
try:
    while True:
        # Hiển thị thông tin môi trường
        display_environment()
        time.sleep(2)  # Dừng 2 giây trước khi cập nhật lại thông tin
        sense.clear()  # Xóa màn hình LED Matrix
        display_name("vilaphon viengsavanh")  # Thay thế bằng tên của bạn
except KeyboardInterrupt:
    print("Dừng chương trình")
    sense.clear()
