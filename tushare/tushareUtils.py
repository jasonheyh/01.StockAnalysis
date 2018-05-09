#
# import datetime
# # 该模块主要提供一些处理交易日的简单函数
#
#
# def get_monthend_trading_day_list(begin_day="2007-01-01", end_day="2015-12-31"):
#     """获取每月的最后一个交易日"""
#     cal_dates = DataAPI.TradeCalGet(exchangeCD=u"XSHG", beginDate=begin_day, endDate=end_day, field="calendarDate,isMonthEnd")
#     trading_days = cal_dates[cal_dates['isMonthEnd' ] == 1]["calendarDate"].tolist()
#     trading_days = [day[0:4] + day[5:7] + day[8:] for day in trading_days]  # 更改日期的格式，将'2014-01-03'转化为'20140103'
#     return trading_days
#
# def get_monthend(date_str='2016-01-04'):
#     """获取该日的月底的最后一个交易日"""
#     begin_date = datetime.strptime(date_str, '%Y-%m-%d')
#     end_date = begin_date + 100 * timedelta(days=1)
#
#     begin_day_str = begin_date.strftime('%Y-%m-%d')
#     end_day_str = end_date.strftime('%Y-%m-%d')
#
#     return get_monthend_trading_day_list(begin_day_str, end_day_str)[0]
#
# def get_specific_trading_day(date_str='2016-01-04', window=20, direction='back'):
#     """给定日期，可以通过这个函数获取前后N天的那个交易日"""
#     date = datetime.strptime(date_str, '%Y-%m-%d')
#     if direction =='back':
#         begin_day = date - (window +5) * 4 * timedelta(days=1)   # 可以获取冗余的交易日，防止最终取不到有效数据
#         end_day = date
#     elif direction =='forward':
#         begin_day = date
#         end_day = date + (window +5)  * 4 * timedelta(days=1)
#
#     begin_day_str = begin_day.strftime('%Y-%m-%d')
#     end_day_str = end_day.strftime('%Y-%m-%d')
#
#     cal_dates = DataAPI.TradeCalGet(exchangeCD=u"XSHG", beginDate=begin_day_str, endDate=end_day_str, field="calendarDate,isOpen")
#     trading_days = cal_dates[cal_dates['isOpen'] == 1]["calendarDate"].tolist()
#     # trading_days = [day[0:4] + day[5:7] + day[8:] for day in trading_days]  # 更改日期的格式，将'2014-01-03'转化为'20140103'
#     try:
#         if direction =='back':
#             return trading_days[-window]
#         return trading_days[window]
#     except:
#         print date_str ,window ,direction
#
#
# def get_trading_days_with_window(date_str='2016-01-04', window=20, direction='forward'):
#     """给定日期，可以通过这个函数获取前后N天的交易日列表"""
#     date = datetime.strptime(date_str, '%Y-%m-%d')
#     if direction =='back':
#         begin_day = date - (window +5)  * 4 * timedelta(days=1)
#         end_day = date
#     elif direction =='forward':
#         begin_day = date
#         end_day = date + (window +5)  * 4 * timedelta(days=1)
#
#     begin_day_str = begin_day.strftime('%Y-%m-%d')
#     end_day_str = end_day.strftime('%Y-%m-%d')
#
#     cal_dates = DataAPI.TradeCalGet(exchangeCD=u"XSHG", beginDate=begin_day_str, endDate=end_day_str, field="calendarDate,isOpen")
#     trading_days = cal_dates[cal_dates['isOpen' ] == 1]["calendarDate"].tolist()
#     # trading_days = [day[0:4] + day[5:7] + day[8:] for day in trading_days]  # 更改日期的格式，将'2014-01-03'转化为'20140103'
#     try:
#         if direction == 'back':
#             return trading_days[-window:]
#         return trading_days[:window]
#     except:
#         pass
#         # print date_str ,window ,direction
