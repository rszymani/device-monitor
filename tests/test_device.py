import pytest

from app.devices.device import DummyDevice


class TestDummyDevice:
    def test_correct_get_parameters(self):
        assert {'current': 1, 'name': 'something', 'power': 6, 'voltage': 1} == DummyDevice('test').get_parameters()

    def test_not_existing_get_parameters(self):
        with pytest.raises(FileNotFoundError):
            DummyDevice('not_existing').get_parameters()
