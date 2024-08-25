import logging
import logging.handlers
import threading

class LoggerManager:
    _instance = None
    _lock = threading.Lock()
    _loggers = {}

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(LoggerManager, cls).__new__(cls)
        return cls._instance

    def get_logger(self, name="app_logger", level=logging.INFO, 
                   file_handler=None, rotating_file_handler=None, 
                   max_bytes=10000, backup_count=5,
                   stream_formatter='%(name)s - %(levelname)s - %(message)s', 
                   file_formatter='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        
        if name not in self._loggers:
            logger = logging.getLogger(name)
            logger.setLevel(level)

            # Set up the stream handler
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(level)
            stream_formatter = logging.Formatter(stream_formatter)
            stream_handler.setFormatter(stream_formatter)
            logger.addHandler(stream_handler)

            if file_handler:
                file_handler = logging.FileHandler(file_handler)
                file_handler.setLevel(level)
                file_formatter = logging.Formatter(file_formatter)
                file_handler.setFormatter(file_formatter)
                logger.addHandler(file_handler)

            if rotating_file_handler:
                rotating_handler = logging.handlers.RotatingFileHandler(
                    rotating_file_handler, maxBytes=max_bytes, backupCount=backup_count
                )
                rotating_handler.setLevel(level)
                rotating_handler.setFormatter(file_formatter)
                logger.addHandler(rotating_handler)

            self._loggers[name] = logger
        
        return self._loggers[name]

def get_logger(name="app_logger", level=logging.INFO, 
               file_handler=None, rotating_file_handler=None, 
               max_bytes=10000, backup_count=5,
               stream_formatter='%(name)s - %(levelname)s - %(message)s', 
               file_formatter='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
    logger_manager = LoggerManager()
    return logger_manager.get_logger(name, level, file_handler, rotating_file_handler,
                                      max_bytes, backup_count, stream_formatter, file_formatter)

