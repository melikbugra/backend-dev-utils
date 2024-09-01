import logging

from backend_dev_utils import get_logger


logger = get_logger(
    name="my-logger",
    level=logging.INFO,
    rotating_file_name="my-rotating-log-file.log",
    file_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    max_bytes=10000,
    backup_count=5,
)

logger.info("Hello World!")
