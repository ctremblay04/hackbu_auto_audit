import pandas as pd
from quarter import Quarter
import math

class Company(object):
    def __init__(self, name, ticker, quarters):
        self.name = name
        self.ticker = ticker
        self.quarters = quarters

    def validate(self):
        ret = Company_Report(self)
        for q in self.quarters:
            ret.quarter_reports.append(q.validate())
        return ret

    def __str__(self):
        ret = f"Company Name: {self.name}\nCompany Ticker: {self.ticker}\nQuarters:\n"
        for i in range(4):
            ret += f"\tQuarter {i+1}:\n"
            for l in str(self.quarters[i]).split('\n'):
                ret += f'\t\t{l}\n'
        return ret

    @staticmethod
    def construct(filename):
        get_val = lambda s : 0 if math.isnan(s) else int(s)
        df = pd.read_excel(filename)
        company_list = {}
        for i in range(len(df)):
            fields = list(df.loc[i])
            if not str(fields[0]).startswith('Company') or fields[0] == 'Company Name':
                continue
            quarters = [None]*4
            for j in range(4):
                quarters[j] = Quarter(get_val(fields[4*j+5]), get_val(fields[4*j+6]))
            c = Company(fields[0], fields[1], quarters)
            company_list[c.name] = c
        return company_list


class Company_Report():
    def __init__(self, c):
        self.company = c
        self.quarter_reports = []

    def __str__(self):
        ret = f"Company: {self.company.name} Quarter Reports:\n"
        for i in range(4):
            ret += f"\tQuarter {i+1} Report:\n"
            for l in str(self.quarter_reports[i]).split('\n'):
                ret += f'\t\t{l}\n'
        return ret
