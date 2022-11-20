import datetime


class Date:
    def __get_now() -> datetime.tzinfo:
        t_delta = datetime.timedelta(hours=9)
        JST = datetime.timezone(t_delta, 'JST')
        now = datetime.datetime.now(JST)
        return now
    
    def get_detail_date() -> str:
        date = Date.__get_now().strftime('%Y/%m/%d %H:%M:%S')
        return date
