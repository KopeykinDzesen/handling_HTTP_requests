class FourDigitYearConverter:
    regex = '[12][0-9]{3}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '{}'.format(value)


class TwoDigitMonthConverter:
    regex = '0[1-9]|1[0-2]'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        str = '{}'.format(value)
        if len(str) == 1: str = '0' + str
        return str