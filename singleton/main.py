from file_logging import Logger

logger = Logger("program.log")


for i in range(4):
    logger.info(f"log message {i}")


try:
    a = 1 / 0
except ZeroDivisionError:
    logger.error("Can't divide by zero")
