import os


class Settings:
    DUMMY_DIR_PATH: str = os.getenv("DUMMY_DIR_PATH", "devices_files")
    RETRY_SLEEP_TIME: int = int(os.getenv("RETRY_SLEEP_TIME", 5))


SETTINGS = Settings()
