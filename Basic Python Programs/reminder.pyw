import time 
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="Please Drink Water Now !",
            message="The U.S. National Academies of Sciences, Engineering, and Medicine determined that an"
            "adequate daily fluid intake is: About 11.5 cups(2.7 liters) of fluids a day for women.",
            app_icon="C:/Users/DELL/Desktop/Python/icon.ico",
            timeout=30        
        )
        time.sleep(3600)
