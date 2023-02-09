from threading import Thread
from time import sleep

from app.devices.device import DummyDevice
from app.device_monitor import DeviceMonitor


def get_statuses(device_monitor):
    while True:
        print(device_monitor.get_statuses())
        sleep(1)


if __name__ == '__main__':
    device_1 = DummyDevice('1')
    device_2 = DummyDevice('2')
    device_3 = DummyDevice('3')
    device_4 = DummyDevice('4')
    device_5 = DummyDevice('5')
    device_6 = DummyDevice('6')

    device_monitor = DeviceMonitor([device_4])
    device_monitor.start()
    device_monitor.add_device(device_6)

    device_monitor1 = DeviceMonitor([device_1, device_5, device_6])
    device_monitor1.start()

    device_monitor2 = DeviceMonitor([device_2, device_3])
    device_monitor2.start()

    threads = [
        Thread(target=get_statuses, args=[device_monitor1]),
        Thread(target=get_statuses, args=[device_monitor]),
        Thread(target=get_statuses, args=[device_monitor2], daemon=True),
    ]

    for thread in threads:
        thread.start()

    # parameter for device monitor (device_1, device_4) will not be updated, any changes in test files will not impact
    # output
    device_monitor.stop()

    for thread in threads:
        thread.join()

