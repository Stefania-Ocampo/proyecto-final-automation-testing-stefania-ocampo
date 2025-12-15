import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "reports/logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("automation_logger")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    f"{LOG_DIR}/suite.log",
    maxBytes=2_000_000,
    backupCount=5
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

logger.addHandler(handler)

