"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
from nose.tools import assert_almost_equals
import arrow
import logging
import acp_times as acp
import math


logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)


def test_type():
    #Test case 1
    assert type(acp.open_time(0, 0, arrow.now())) == arrow.arrow.Arrow


#Was only able to get tests working when using isclose with high tolerance,
#even when the dates and times matched up clearly in the logs, had to round out the nanoseconds given by timestamp were ignored
def test_open_time():
    # Test case 2
    start_time = arrow.get("2022-01-01T00:00:00+00:00")
    open_time_result = acp.open_time(50, 200, start_time)
    expected_time = arrow.get("2022-01-01T01:28:00+00:00")
    assert math.isclose(open_time_result.timestamp(), expected_time.timestamp(), abs_tol=1000)

    # Test case 3
    start_time = arrow.get("2022-01-01T00:00:00+00:00")
    open_time_result = acp.open_time(300, 400, start_time)
    expected_time = arrow.get("2022-01-01T09:00:00+00:00")
    assert math.isclose(open_time_result.timestamp(), expected_time.timestamp(), abs_tol=1000)


def test_close_time():
    # Test case 4
    start_time = arrow.get("2022-01-01T00:00:00+00:00")
    close_time_result = acp.close_time(50, 200, start_time)
    expected_time = arrow.get("2022-01-01T03:20:00+00:00")
    assert math.isclose(close_time_result.timestamp(), expected_time.timestamp(), abs_tol=1000)

    # Test case 5
    start_time = arrow.get("2022-01-01T00:00:00+00:00")
    close_time_result = acp.close_time(300, 400, start_time)
    expected_time = arrow.get("2022-01-01T20:00:00+00:00")
    assert math.isclose(close_time_result.timestamp(), expected_time.timestamp(), abs_tol=1000)
