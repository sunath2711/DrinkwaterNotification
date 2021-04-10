import time
from plyer import notification


if __name__ == "__main__":
    while True:
        notification.notify(
        title = "**Please drink Water!!",
        message = "The adult human body is 60% water and your blood is 90% water. Drinking water benefits the whole body in a million ways. From flushing out toxins to preventing acne and giving you glowing skin, water is a miracle drink!",
        app_icon = "E:\WaterAppPython\waterglass.ico",
        timeout =2
        )
        time.sleep(60*60)