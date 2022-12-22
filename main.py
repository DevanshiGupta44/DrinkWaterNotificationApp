import time
from plyer import notification

while True:
    notification.notify(
        title="Please Drink Water Now!!",
        message="Stay hydrated,  \n"
                "Stay healthy <3 ",
        timeout=15,
        app_icon= r".\Iconsmind-Outline-Glass-Water.ico"
    )

    time.sleep(60 * 60)