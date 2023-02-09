import json
from abc import (
    abstractmethod,
    ABC,
)

from app.settings import SETTINGS


class Device(ABC):
    """Abstract class for reading parameters from device. New device type should inherit this class and override
    get_parameters method to adapt to protocol.
    """
    def __init__(self, device_id: str, *args, **kwargs):
        self.device_id = device_id

    @abstractmethod
    def get_parameters(self) -> dict:
        """Method is used to adapt device output parameter to dictionary used in DeviceMonitor"""
        raise NotImplementedError


class DummyDevice(Device):
    def get_parameters(self) -> dict:
        with open(f'{SETTINGS.DUMMY_DIR_PATH}/{self.device_id}.json') as param_file:
            return json.load(param_file)
