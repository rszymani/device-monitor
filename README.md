# Device Monitor

Device monitor is app to monitor parameters devices concurrently. 
Monitoring of devices in background could be useful in cases where we don't want to block main thread of application.


To add new type of device it is needed to inherit adapter Device and implement get_parameters method which is compatible with the rest of DeviceMonitor.


Modification of the dummy device parameters (which is used by DummyDevice) is possible during running test application.

# Structure
```
├── app
│   ├── device_monitor.py
│   ├── devices
│   ├── __init__.py
│   ├── main.py
├── devices_files
```
- devices_files contains test json used to simulate devices.
- device_monitor.py module with main monitoring tool.
- main.py - test of the library
- devices - adapter for devices which are compatible with DeviceMonitor

# How to run

## Script tests

To run test script from project directory just run `export PYTHONPATH=$(pwd); python test_script.py`

## Tests
From project root directory`export DUMMY_DIR_PATH=tests/test_files;export RETRY_SLEEP_TIME=0;pytest --cov=app tests/ --cov-report term-missing`

