#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'User'

import unittest
import datetime

from MainScript import FileHandler

def get_day_of_the_week():
    DayL = ['Mon','Tues','Wednes','Thurs','Fri','Satur','Sun']
    date = DayL[datetime.date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day).weekday()] + 'day'
    return date

class MyTest(unittest.TestCase):
    def setUp(self):
        self.file2 = FileHandler.read_csv('file2.txt')
        self.file3 = FileHandler.read_csv('file3.txt')

    def tearDown(self):
        pass

    def get_row_index(self):
        #Get today's day name like: Saturday
        today_day = get_day_of_the_week()
        #Now check for matching value in static list and return the index.
        for i,val in enumerate(self.static_header):
            if val == today_day:
                return i

    def get_current_time_in_seconds(self):
        current_time_hour = datetime.datetime.now().hour
        current_time_min = datetime.datetime.now().minute
        s_float = str(current_time_hour)+'.'+str(current_time_min)
        current_time = float(s_float)
        return int(current_time*3600)

    def test_f2_f3(self):
        f2_row = [79200, 28800, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        f3_row = [0, 0, 79200, 28800, 79200, 28800, 79200, 28800, 79200, 28800, 79200, 28800, 79200, 28800]

        row_index = 4

        f2_val = f2_row[row_index]
        f3_val = f3_row[row_index]

        current_time_milis = self.get_current_time_in_seconds()

        if f2_val > current_time_milis or f3_val > current_time_milis:
            prev_row_index = row_index
            while True:
                prev_row_index = prev_row_index - 2
                if prev_row_index < 0:
                    break
                f2_val = f2_row[prev_row_index]
                f3_val = f3_row[prev_row_index]
                if f2_val > 0 or f3_val > 0:
                    break

        self.assertEqual(f2_val,0)
        self.assertEqual(f3_val,79200)

if __name__ == '__main__':
    MyTest().main()
