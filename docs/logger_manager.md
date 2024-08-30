LoggerManager is a singleton to provide logger instances with provided configuration. In this module we have tge *get_logger* function to return a logger instance from this singleton. 

<!-- termynal: {"prompt_literal_start": ["$", ">>>"], title: python} -->

```python
>>> from backend_dev_utils import get_logger
>>> logger = get_logger(name="my-logger")
>>> logger.info("Hello World!")
my-logger - INFO - Hello World!
```

With only name argument provided, other arguments will take their default values.

```python

{!./docs_src/logger_manager/file_handler.py!}

```