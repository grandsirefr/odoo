import logging
import time
from datetime import datetime
_logger = logging.getLogger(__name__)


def log_time(function, func_name="", character="*", count=30):

    _logger.debug("".join([character for i in range(0, count)]))
    start_counter = time.perf_counter()
    current_time = datetime.now().strftime("%H:%M:%S")
    _logger.debug("Starting [{func_name}] at {current_time}".format(func_name=func_name, current_time=current_time))
    function(None)
    end_counter = time.perf_counter()
    total_time = end_counter-start_counter
    current_time = datetime.now().strftime("%H:%M:%S")
    _logger.debug("{func_name} finished at {end_time} with success. It tooks {total_time} seconds".format(func_name=func_name, end_time=current_time, total_time=total_time))
    _logger.debug("".join([character for i in range(0, count)]))

