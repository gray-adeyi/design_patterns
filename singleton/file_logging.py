from enum import Enum


class Level(str, Enum):
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARN = "WARN"
    INFO = "INFO"
    DEBUG = "DEBUG"


def write_log(level: Level, msg: str):
    with open("program.log", "a") as log_file:
        log_file.write(f"[{level}] {msg}\n")


def critical(msg: str):
    write_log(Level.CRITICAL, msg)


def error(msg: str):
    write_log(Level.ERROR, msg)


def warn(msg: str):
    write_log(Level.WARN, msg)


def info(msg: str):
    write_log(Level.INFO, msg)


def debug(msg: str):
    write_log(Level.DEBUG, msg)


class Logger:
    """A file-based message logger with the following properties

    Attributes:
            file_name: a string representing the full path of the log file to which
            this logger will write its messages
    """

    def __init__(self, file_name: str):
        """Returns a Logger instance whose file_name is *file_name*"""
        self.file_name = file_name

    def _write_log(self, level: Level, msg: str):
        """Writes a message to the file_name for a specific Logger instance"""
        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def critical(self, msg: str):
        self._write_log(Level.CRITICAL, msg)

    def error(self, msg: str):
        self._write_log(Level.ERROR, msg)

    def warn(self, msg: str):
        self._write_log(Level.WARN, msg)

    def info(self, msg: str):
        self._write_log(Level.INFO, msg)

    def debug(self, msg: str):
        self._write_log(Level.DEBUG, msg)
