from threading import Thread
from time import sleep

from app.devices.device import DummyDevice
from app.device_monitor import DeviceMonitor


class TestDeviceMonitor:
    def test_single_thread_device_monitor(self):
        device = DummyDevice('test')
        device_2 = DummyDevice('test_2')
        device_monitor = DeviceMonitor([device, device_2])
        device_monitor.start()
        expected_statuses = {'test': {'voltage': 1, 'current': 1, 'power': 6, 'name': 'something'},
                             'test_2': {'test_2': 1}}
        sleep(1)
        assert expected_statuses == device_monitor.get_statuses()
        device_monitor.stop()

    def test_add_device_monitor(self):
        device = DummyDevice('test')
        device_2 = DummyDevice('test_2')
        device_monitor = DeviceMonitor([device])
        device_monitor.start()
        device_monitor.add_device(device_2)
        expected_statuses = {'test': {'voltage': 1, 'current': 1, 'power': 6, 'name': 'something'},
                             'test_2': {'test_2': 1}}
        sleep(1)
        device_monitor.stop()
        assert expected_statuses == device_monitor.get_statuses()

    def test_error(self):
        device = DummyDevice('test')
        device_2 = DummyDevice('invalid_id')
        device_monitor = DeviceMonitor([device, device_2])
        device_monitor.start()

        expected_statuses = {'test': {'voltage': 1, 'current': 1, 'power': 6, 'name': 'something'}}
        sleep(1)
        assert expected_statuses == device_monitor.get_statuses()
        device_monitor.stop()

    def test_separate_thread_device_monitor(self):
        device = DummyDevice('test')
        device_2 = DummyDevice('test_2')
        device_monitor = DeviceMonitor([device, device_2])
        device_monitor.start()
        expected_statuses = {'test': {'voltage': 1, 'current': 1, 'power': 6, 'name': 'something'},
                             'test_2': {'test_2': 1}}
        out = []
        t = Thread(target=self._get_statuses, args=[device_monitor, out])
        t.start()
        t.join()
        assert len(out) == 10
        assert out == [expected_statuses for _ in range(10)]
        device_monitor.stop()

    def _get_statuses(self, device_monitor, out):
        for _ in range(10):
            out.append(device_monitor.get_statuses())
