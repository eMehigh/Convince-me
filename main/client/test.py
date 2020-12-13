from client import Client
import time

from threading import Thread


def update_messages():
    msgs = []
    run = True
    while run:
        time.sleep(0.1)
        new_messages = c1.get_messages()
        msgs.extend(new_messages)
    for msg in new_messages:
        print(msg)
        if msg == "{quit}":
            break


#Thread(target=update_messages).start()


c1 = Client("mihai")

c2 = Client("alin")

c1.send_message("hello")
time.sleep(3)
c2.send_message("hello")
time.sleep(3)

c1.send_message("cf")
time.sleep(3)

c2.send_message("bn")
time.sleep(3)
c1.disconnect()
c2.disconnect()

