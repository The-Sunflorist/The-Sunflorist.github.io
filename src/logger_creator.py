# coding=utf-8
#
# logger_creator.py
# The-Sunflorist.github.io/src/
#
# Created by 向阳花花农(The Sunflorist) on 2024-10-31.
# Copyright © 2024 向阳花花农(The Sunflorist). All rights reserved.
#
# Create a logger.


import os
from datetime import datetime
from logging import (
    CRITICAL, DEBUG, ERROR, FileHandler, Formatter, getLogger,
    INFO, Logger, LogRecord, StreamHandler, WARNING,
)
from warnings import warn

from sty import fg, rs


class ColoredFormatter(Formatter):
    # color of message for each level
    __colors = {
        DEBUG: fg.blue,
        INFO: fg.green,
        WARNING: fg.yellow,
        ERROR: fg(208),
        CRITICAL: fg.red,
    }
    __format_left = f'[%(asctime)s]{fg.cyan}[%(name)s %(lineno)d]'
    __format_right = f' %(message)s{rs.all}'

    def __init__(self, date_format: str) -> None:
        super().__init__(fmt=None, datefmt=date_format)

    def format(self, record: LogRecord) -> str:
        """Format a log record based on its level.

        :param record: A log record.
        :return: Formatted string of a record.
        """

        self._style._fmt = (
            f'{self.__format_left}{self.__colors[record.levelno]}'
            f'{self.__format_right}'
        )
        return super().format(record=record)


class ColoredLogger:
    """Use color names as log functions.
    """

    # https://docs.python.org/3/library/datetime.html#format-codes
    __date_format: str = '%Y-%m-%d %H:%M:%S %z'
    stream_formatter = ColoredFormatter(date_format=__date_format)
    file_formatter = Formatter(
        fmt=f'[%(asctime)s][%(name)s %(lineno)d] %(message)s',
        datefmt=__date_format,
    )

    def __init__(self, logger: Logger) -> None:
        self.__logger = logger
        self.blue = self.__logger.debug
        self.green = self.__logger.info
        self.yellow = self.__logger.warning
        self.orange = self.__logger.error
        self.red = self.__logger.critical

    def newline(self) -> None:
        """Log a newline without formatter.
        """

        for handler in self.__logger.handlers:
            handler.setFormatter(fmt=Formatter(fmt=''))
        self.__logger.critical('')
        for handler in self.__logger.handlers:
            # note: FileHandler is a subclass of StreamHandler
            handler.setFormatter(
                fmt=self.file_formatter if isinstance(handler, FileHandler)
                else self.stream_formatter
            )


class LoggerCreator:
    @staticmethod
    def get_logger(
            name: str,
            level: int = DEBUG,
            to_console: bool = True,
            log_folder_path: str | None = os.path.join('.tmp', '_logs'),
    ) -> ColoredLogger:
        """Create a logger.

        :param name: logger name
        :param level: log level, default is logging.DEBUG
        :param to_console: log to console if True
        :param log_folder_path: log to a file `log_folder_path/YYYY-MM-DD.log`
            if provided
        :return: a colored logger
        """

        # create a logger, set its logging level,
        # and stop it from propagating the message to its parent
        logger = getLogger(name=name)
        logger.setLevel(level=level)
        logger.propagate = False

        if not (to_console or log_folder_path):
            warn(
                f'{fg.yellow}Logger {name} has no handler, '
                f'nothing will be logged.{fg.rs}'
            )

        # configure a console handler
        if to_console:
            stream_handler = StreamHandler()
            stream_handler.setLevel(level=level)
            stream_handler.setFormatter(fmt=ColoredLogger.stream_formatter)
            logger.addHandler(hdlr=stream_handler)

        # configure a file handler
        if log_folder_path:
            os.makedirs(name=log_folder_path, mode=0o755, exist_ok=True)
            file_handler = FileHandler(
                filename=os.path.join(
                    log_folder_path,
                    f'{datetime.now().strftime(format='%Y-%m-%d')}.log',
                ),
                mode='a',
                encoding='utf-8',
            )
            file_handler.setLevel(level=level)
            file_handler.setFormatter(fmt=ColoredLogger.file_formatter)
            logger.addHandler(hdlr=file_handler)

        return ColoredLogger(logger=logger)
