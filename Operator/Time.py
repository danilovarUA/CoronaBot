import datetime
import re


def current_time(time_string):
    report_datetime = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S Etc/GMT")
    # report_datetime += datetime.timedelta(hours=3)
    new_time_string = "{:02d}/{:02d}/{:04d} {:02d}:{:02d}:{:02d}".format(report_datetime.day, report_datetime.month,
                                                                         report_datetime.year, report_datetime.hour,
                                                                         report_datetime.minute, report_datetime.second)
    return new_time_string
