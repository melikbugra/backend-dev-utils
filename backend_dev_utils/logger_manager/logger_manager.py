import logging
import logging.handlers
import threading


class LoggerManager:
    """Logger manager singleton class that returns a logger with a name."""

    _instance = None
    _lock: threading.Lock = threading.Lock()
    _loggers: dict[str, logging.Logger] = {}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def get_logger(
        self,
        name: str,
        level: int,
        file_name: str,
        rotating_file_name: str,
        max_bytes: int,
        backup_count: int,
        stream_format: str,
        file_format: str,
    ):
        """Get a logger instance with given name and configuration.

        :param name: Logger name
        :type name: str
        :param level: Logging level (logging.DEBUG, logging.INFO etc.)
        :type level: int
        :param file_name: File name for file handler
        :type file_name: str
        :param rotating_file_name: File name for rotating file handler
        :type rotating_file_name: str
        :param max_bytes: Maximum bytes limit for rotating file handler's single file
        :type max_bytes: int
        :param backup_count: Backup file number for rotating file handler
        :type backup_count: int
        :param stream_format: Formatter for stream handler (see formatters in python's logging module)
        :type stream_format: str
        :param file_format: Formatter for file and rotating file handler (see formatters in python's logging module)
        :type file_format: str
        :return: Logger instance
        :rtype: logging.Logger
        """

        if name not in self._loggers:
            logger = logging.getLogger(name)
            logger.setLevel(level)

            # Set up the stream handler
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(level)
            stream_formatter = logging.Formatter(stream_format)
            stream_handler.setFormatter(stream_formatter)
            logger.addHandler(stream_handler)

            if file_name:
                file_handler = logging.FileHandler(file_name)
                file_handler.setLevel(level)
                file_formatter = logging.Formatter(file_format)
                file_handler.setFormatter(file_formatter)
                logger.addHandler(file_handler)

            if rotating_file_name:
                rotating_handler = logging.handlers.RotatingFileHandler(
                    rotating_file_name, maxBytes=max_bytes, backupCount=backup_count
                )
                rotating_handler.setLevel(level)
                rotating_file_formatter = logging.Formatter(file_format)
                rotating_handler.setFormatter(rotating_file_formatter)
                logger.addHandler(rotating_handler)

            self._loggers[name] = logger

        return self._loggers[name]


def get_logger(
    name: str = "logger",
    level: int = logging.INFO,
    file_name: str = None,
    rotating_file_name: str = None,
    max_bytes: int = 10000,
    backup_count: int = 5,
    stream_format: str = "%(name)s - %(levelname)s - %(message)s",
    file_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
):
    """Get a logger instance with given name and configuration.

    :param name: Logger name, defaults to "logger"
    :type name: str, optional
    :param level: Logging level (logging.DEBUG, logging.INFO etc.), defaults to logging.INFO
    :type level: int, optional
    :param file_name: File name for file handler, defaults to None
    :type file_name: str, optional
    :param rotating_file_name: File name for rotating file handler, defaults to None
    :type rotating_file_name: str, optional
    :param max_bytes: Maximum bytes limit for rotating file handler's single file, defaults to 10000
    :type max_bytes: int, optional
    :param backup_count: Backup file number for rotating file handler, defaults to 5
    :type backup_count: int, optional
    :param stream_format: Formatter for stream handler (see formatters in python's logging module), defaults to "%(name)s - %(levelname)s - %(message)s"
    :type stream_format: str, optional
    :param file_format: Formatter for file and rotating file handler (see formatters in python's logging module), defaults to "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    :type file_format: str, optional
    :return: Logger instance
    :rtype: logging.Logger
    """
    logger_manager = LoggerManager()
    return logger_manager.get_logger(
        name,
        level,
        file_name,
        rotating_file_name,
        max_bytes,
        backup_count,
        stream_format,
        file_format,
    )
