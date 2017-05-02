#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2017/5/2
import unittest


class DateInfo(object):
    _month_day_num = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31,
                      4: 30, 6: 30, 9: 30, 11: 30, 2: 28}

    @staticmethod
    def is_leap_year(year):
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

    @classmethod
    def get_day_num_of_month(cls, year, month):
        return 29 if month == 2 and cls.is_leap_year(year) else cls._month_day_num[month]

    @classmethod
    def get_date_later_month(cls, year, month, day, num=1):
        if month + num <= 12:
            return year, month + num, day - max(0, day - cls.get_day_num_of_month(year, month + num))
        else:
            return year + 1, month + num - 12, day - max(0, day - cls.get_day_num_of_month(year + 1, month + num - 12))

    @classmethod
    def get_date_month_later(cls, year, month, day):
        return cls.get_date_later_month(year, month, day, num=1)

    @classmethod
    def get_date_season_later(cls, year, month, day):
        return cls.get_date_later_month(year, month, day, num=3)

    @classmethod
    def get_date_semester_later(cls, year, month, day):
        return cls.get_date_later_month(year, month, day, num=6)

    @classmethod
    def get_date_year_later(cls, year, month, day):
        return cls.get_date_later_month(year, month, day, num=12)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.di = DateInfo()

    def tearDown(self):
        del self.di

    def test_info(self):
        self.assertEqual(DateInfo.is_leap_year(2000), True)
        self.assertEqual(DateInfo.is_leap_year(2001), False)
        self.assertEqual(DateInfo.is_leap_year(2004), True)
        self.assertEqual(DateInfo.is_leap_year(2100), False)
        self.assertEqual(self.di.get_day_num_of_month(2017, 4), 30)
        self.assertEqual(self.di.get_day_num_of_month(2017, 5), 31)
        self.assertEqual(self.di.get_day_num_of_month(2017, 2), 28)
        self.assertEqual(self.di.get_day_num_of_month(2016, 2), 29)
        self.assertEqual(self.di.get_date_month_later(2016, 1, 31), (2016, 2, 29))
        self.assertEqual(self.di.get_date_season_later(2015, 11, 30), (2016, 2, 29))
        self.assertEqual(self.di.get_date_semester_later(2015, 8, 31), (2016, 2, 29))
        self.assertEqual(self.di.get_date_year_later(2015, 2, 28), (2016, 2, 28))
        self.assertEqual(self.di.get_date_year_later(2016, 2, 29), (2017, 2, 28))


if __name__ == '__main__':
    # unittest.main()
    import datetime
    from collections import defaultdict
    begin = datetime.date(2016, 1, 1)
    end = datetime.date(2018, 1, 1)
    delta = datetime.timedelta(days=1)
    get = defaultdict(list)
    while begin < end:
        get[DateInfo.get_date_month_later(begin.year, begin.month, begin.day)] += [(begin.year, begin.month, begin.day)]
        get[DateInfo.get_date_season_later(begin.year, begin.month, begin.day)] += [(begin.year, begin.month, begin.day)]
        get[DateInfo.get_date_semester_later(begin.year, begin.month, begin.day)] += [(begin.year, begin.month, begin.day)]
        get[DateInfo.get_date_year_later(begin.year, begin.month, begin.day)] += [(begin.year, begin.month, begin.day)]
        begin += delta

    print(get)
    get = defaultdict(list, {k: v for k, v in get.items() if k[0] > 2016})
    get = {k: v for k, v in get.items() if k[0] == 2017 }
    get_len = {k: len(v) for k, v in get.items()}
    print(get_len)