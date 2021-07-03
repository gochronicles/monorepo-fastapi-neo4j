from pathlib import os
from api.utils import load_config

# Load Config
config_path = os.getenv("DOMAIN_CONFIG", "config.yml")
config = load_config(config_path)


from api.api import app
