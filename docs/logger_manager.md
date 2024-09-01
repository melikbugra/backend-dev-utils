LoggerManager is a [NamedSingleton](design_patterns.md#namedsingleton) to provide logger instances with provided configuration. In this module we have the *get_logger* function to return a logger instance from this singleton. 

With only name argument provided, it will return a stream logger (which only logs to console) and the other arguments will take their default values as logging level info and stream logger format *%(name)s - %(levelname)s - %(message)s*.

<!-- termynal: {"prompt_literal_start": ["$", ">>>"], title: python} -->

```python
>>> from backend_dev_utils import get_logger
>>> logger = get_logger(name="my-logger")
>>> logger.info("Hello World!")
my-logger - INFO - Hello World!
```

Or, if you provide the argument *file_path*, the logger will automatically create a logger that logs to file.

```python

{!./docs_src/logger_manager/file_handler.py!}

```

Finally, if you provide the *rotating_file_path* argument, the output file size will be limited by *max_bytes* argument, and at most *backup_count* of files will be created named as *log-file.log.1*, *log-file.log.2* etc. And when all limits are full and it needs to write a new log file, it starts deleting from the oldest one.

```python

{!./docs_src/logger_manager/rotating_file_handler.py!}

```