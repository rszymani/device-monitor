from copy import deepcopy
from threading import (
    Event,
    Lock,
    Thread,
)
from time import sleep

from app.devices.device import Device
from app.settings import SETTINGS


class DeviceMonitor(Thread):
    """Main module for monitoring devices. Monitored devices should be passed during object creation."""
    def __init__(self, monitored_devices: list[Device], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._monitored_devices = monitored_devices
        self._output_map = {}
        self._stopped = Event()
        self._lock = Lock()

    def start(self):
        """Method for start DeviceMonitor in another thread."""
        Thread.start(self)

    def stop(self):
        self._stopped.set()

    def run(self):
        """Monitoring all devices from """
        while True:
            for monitored_device in self._monitored_devices:
                try:
                    # Assumed that the devices are not removed from map. Operation of assigning in dictionary
                    # are atomic, and should be thread-save. However, it is safer to lock operation in cases of changes
                    # GIL in the future.
                    with self._lock:
                        self._output_map[monitored_device.device_id] = monitored_device.get_parameters()
                except Exception as error:
                    # in case of any error in any device I assumed that there is some problem with devices, and we
                    # should stop requesting data from device for a moment.
                    print('Fetching parameter error', error)
                    sleep(SETTINGS.RETRY_SLEEP_TIME)

            if self._stopped.is_set():
                return
            sleep(2)

    def get_statuses(self):
        # deep copy is not thread-safe operation, so it needed to acquire lock that no other thread modify output map
        # changed size during iteration
        with self._lock:
            return deepcopy(self._output_map)

    def add_device(self, device: Device):
        self._monitored_devices.append(device)
