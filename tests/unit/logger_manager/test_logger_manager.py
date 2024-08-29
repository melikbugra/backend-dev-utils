import logging
import pytest
from io import StringIO
from assertpy import assert_that
from backend_dev_utils.logger_manager.logger_manager import get_logger, LoggerManager


def test_multiple_loggers():
    """
    Test the creation of multiple loggers with different names and levels.

    **Test Scenario**:
    - Create two loggers with different names.
    - Verify that each logger has the correct name and logging level.

    **Assertions**:
    - The logger names should match the provided names.
    - The logger levels should match the provided levels.
    """
    logger1 = get_logger(name="TestLogger1", level=logging.DEBUG)
    logger2 = get_logger(name="TestLogger2", level=logging.ERROR)

    assert_that(logger1.name).is_equal_to("TestLogger1")
    assert_that(logger2.name).is_equal_to("TestLogger2")
    assert_that(logger1.level).is_equal_to(logging.DEBUG)
    assert_that(logger2.level).is_equal_to(logging.ERROR)


def test_singleton_logger():
    """
    Test that the logger instances are the same for the same name, adhering to the singleton pattern.

    **Test Scenario**:
    - Create two loggers with the same name.
    - Verify that both references point to the same logger instance.

    **Assertions**:
    - The two logger instances should be the same object.
    """
    logger1 = get_logger(name="TestLogger")
    logger2 = get_logger(name="TestLogger")

    assert_that(logger1).is_same_as(logger2)


def test_stream_handler_format(caplog: pytest.LogCaptureFixture):
    """
    Test the stream handler's formatting of log messages.

    **Test Scenario**:
    - Create a logger with a specific stream formatter.
    - Log a message and verify the captured log.

    **Assertions**:
    - The log record should have the correct message content.
    - The log level should match the expected level.
    - The logger name should match the expected name.
    """
    logger = get_logger(
        name="TestLogger", stream_format="%(name)s - %(levelname)s - %(message)s"
    )

    with caplog.at_level(logging.INFO):
        logger.info("This is a test message")

    assert_that(caplog.records).is_length(1)
    assert_that(caplog.records[0].message).is_equal_to("This is a test message")
    assert_that(caplog.records[0].levelname).is_equal_to("INFO")
    assert_that(caplog.records[0].name).is_equal_to("TestLogger")


def test_file_handler(tmp_path):
    """
    Test that the file handler correctly writes log messages to a file.

    **Test Scenario**:
    - Create a logger with a file handler.
    - Log a message and verify its presence in the log file.

    **Assertions**:
    - The log file should contain the expected log message.
    - The log file should include the logger's name.
    """
    log_file = tmp_path / "test.log"
    logger = get_logger(name="TestFileLogger", file_name=str(log_file))

    logger.info("This is a test log message")

    with open(log_file, "r") as f:
        log_contents = f.read()

    assert_that(log_contents).contains("This is a test log message")
    assert_that(log_contents).contains("TestFileLogger")


def test_rotating_file_handler(tmp_path):
    """
    Test the rotating file handler's functionality in creating backup log files.

    **Test Scenario**:
    - Create a logger with a rotating file handler.
    - Log multiple messages to exceed the specified file size.
    - Verify that multiple log files are created.

    **Assertions**:
    - There should be multiple log files after rotation.
    - The original log content should be present in one of the log files.
    """
    log_file = tmp_path / "rotating_test.log"
    logger = get_logger(
        name="TestRotatingLogger",
        rotating_file_name=str(log_file),
        max_bytes=50,
        backup_count=2,
        file_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Set the formatter
    )

    for i in range(10):
        logger.info(f"Log entry {i}")

    log_files = list(tmp_path.glob("rotating_test.log*"))
    assert_that(log_files).is_not_empty()

    # Read the contents of the first log file
    with open(log_files[0], "r") as f:
        log_contents = f.read()

    assert_that(log_contents).contains("Log entry")


def test_logger_without_file_handler(caplog):
    """
    Test the functionality of a logger without a file handler, using only a stream handler.

    **Test Scenario**:
    - Create a logger without a file handler.
    - Log a message and verify the captured log in the stream.

    **Assertions**:
    - The log record should have the correct message content.
    - The log message should be captured by the stream handler.
    """
    logger = get_logger(name="TestLoggerWithoutFile")

    with caplog.at_level(logging.INFO):
        logger.info("This is a stream-only log message")

    assert_that(caplog.records).is_length(1)
    assert_that(caplog.records[0].message).is_equal_to(
        "This is a stream-only log message"
    )
