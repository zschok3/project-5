import nose    # Testing framework
from nose.tools import assert_almost_equals
import arrow
import logging
import brevet_db as bdb


def test_brevet_insert():
    distance = 200
    begin_date = "2021-01-01T00:00"
    control_times = [
{'close': '2021-01-01T10:43',
  'km': '160.934400',
  'location': '',
  'miles': '100',
  'open': '2021-01-01T04:44'},
 {'close': '2021-01-01T21:27',
  'km': '321.868800',
  'location': '',
  'miles': '200',
  'open': '2021-01-01T09:41'},
 {'close': '2021-01-02T08:11',
  'km': '482.803200',
  'location': '',
  'miles': '300',
  'open': '2021-01-01T14:53'},
 {'close': '2021-01-02T19:49',
  'km': '643.737600',
  'location': '',
  'miles': '400',
  'open': '2021-01-01T20:21'},
 {'close': '2021-01-03T09:54',
  'km': '804.672000',
  'location': '',
  'miles': '500',
  'open': '2021-01-02T02:06'}
  ]
    # do the insertion
    table= bdb.insert_brevet(distance, begin_date, control_times)
    assert(table != -1 and table != None)

def test_get_brevet():
    distance = 200
    begin_date = "2021-01-01T00:00"
    control_times = [
{'close': '2021-01-01T10:43',
  'km': '160.934400',
  'location': '',
  'miles': '100',
  'open': '2021-01-01T04:44'},
 {'close': '2021-01-01T21:27',
  'km': '321.868800',
  'location': '',
  'miles': '200',
  'open': '2021-01-01T09:41'},
 {'close': '2021-01-02T08:11',
  'km': '482.803200',
  'location': '',
  'miles': '300',
  'open': '2021-01-01T14:53'},
 {'close': '2021-01-02T19:49',
  'km': '643.737600',
  'location': '',
  'miles': '400',
  'open': '2021-01-01T20:21'},
 {'close': '2021-01-03T09:54',
  'km': '804.672000',
  'location': '',
  'miles': '500',
  'open': '2021-01-02T02:06'}
  ]

    table = bdb.insert_brevet(distance,begin_date,control_times)
    _distance, _begin_date, _control_times = bdb.get_brevet()

    assert(distance == _distance)
    assert(begin_date == _begin_date)
    assert(control_times == _control_times)