import logging
import logging.handlers
import threading

from backend_dev_utils.design_patterns.singletons.named_singleton.named_singleton_base import (
    NamedSingletonBase,
)


class LoggerManager(NamedSingletonBase):
    """Logger manager singleton class that returns a logger with a name."""

    _lock: threading.Lock = threading.Lock()
    _loggers: dict[str, logging.Logger] = {}

    def __init__(self, name: str):
        self.name = name

    def get_logger(
        self,
        name: str,
        level: int,
        file_name: str = None,
        rotating_file_name: str = None,
        max_bytes: int = 10000,
        backup_count: int = 5,
        stream_format: str = "%(name)s - %(levelname)s - %(message)s",
        file_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    ) -> logging.Logger:
        """Get a logger instance with the given name and configuration."""

        with self._lock:
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
) -> logging.Logger:
    """Get a logger instance with the given name and configuration."""
    logger_manager = LoggerManager(name=name)
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
