import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]

ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


APP_NAME = os.getenv("APP_NAME", "Sistema de Usuarios")
APP_VERSION = os.getenv("APP_VERSION", "1.0")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")