import os
from dynaconf import Dynaconf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

settings = Dynaconf(
    settings_files=[
        os.path.join(BASE_DIR, "config/settings.toml"),
        os.path.join(BASE_DIR, "config/.secrets.toml"),
    ],
    environments=True,
    env="default",
    merge_enabled=True,
    lowercase_read=True,
)