import logging

from backend_dev_utils import get_logger


logger = get_logger(
    name="my-logger",
    level=logging.INFO,
    file_name="my-log-file.log",
    file_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger.info("Hello World!")
