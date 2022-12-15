from datetime import datetime


def decorator_format_date(is_indo=True):
    def decorator_format_date_in(func):
        def wrapper(param_date):
            list_days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jum\'at',
                         'Sabtu', 'Minggu']
            list_months = ['Januari', 'Februari', 'Maret', 'April', 'Mei',
                           'Juni', 'Juli', 'Agustus', 'September',
                           'Oktober', 'November', 'Desember']
            if not is_indo:
                list_days.clear()
                list_months.clear()

                list_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                             'Friday', 'Saturday', 'Sunday']
                list_months = ['January', 'February', 'March', 'April', 'May',
                               'June', 'July', 'August', 'September',
                               'October', 'November', 'December']

            tmp_date = datetime.strftime(param_date, '%d-%m-%Y')
            tmp_day = datetime.strftime(param_date, '%d')
            tmp_month = datetime.strftime(param_date, '%m')
            tmp_year = datetime.strftime(param_date, '%Y')
            tmp_out_days = datetime.strptime(tmp_date, '%d-%m-%Y').date()
            tmp_detail_date = f'{tmp_day}-{list_months[int(tmp_month)-1]}-{tmp_year}'
            list_out_data = []
            list_out_data.append(list_days[tmp_out_days.weekday()])
            list_out_data.append(', ')
            list_out_data.append(tmp_detail_date)

            return ''.join(list_out_data)
        return wrapper
    return decorator_format_date_in


@decorator_format_date(is_indo=True)
def format_local_datetime(param_date):
    return f'{param_date}'
