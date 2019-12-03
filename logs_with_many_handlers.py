import logging
import random

formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger("my-logger")
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename='info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)


class MyFilter:

    def filter(self, logRecord):
        return logRecord.levelno == logging.INFO


file_handler.addFilter(MyFilter())

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


levels = ['debug', 'info', 'warning', 'error', 'critical']

for _ in range(10):
    level = random.choice(levels)
    eval('logger.{level}("тестовое сообщение уровня {level}")'.format(level=level))

