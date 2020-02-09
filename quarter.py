import trade_ticket

class Quarter(object):
    def __init__(self, p, d):
        self.purchases = p
        self.disposals = d
        self.trade_tickets = []

    def validate(self):
        ret = Quarter_Report(self)
        ret.purchase_discrepancy = self.purchases
        ret.disposal_discrepancy = self.disposals
        for t in self.trade_tickets:
            if t.valid:
                if t.transaction_type == 'Buy':
                    ret.purchase_discrepancy -= t.amount
                else:
                    ret.disposal_discrepancy += t.amount
            ret.ticket_reports.append(t.validate())
        return ret

    def __str__(self):
        ret = f"Purchases: {self.purchases}\nDisposals: {self.disposals}\nTrade Tickets:\n"
        for t in self.trade_tickets:
            for l in str(t).split('\n'):
                ret += f'\t{l}\n'
        return ret


class Quarter_Report(object):
    def __init__(self, q):
        self.quarter = q
        self.purchase_discrepancy = 0
        self.disposal_discrepancy = 0
        self.ticket_reports = []

    def __str__(self):
        ret = f"Purchase discrepancy: {self.purchase_discrepancy}\nDisposal Discrepancy: {self.disposal_discrepancy}\nTicket Reports:\n"
        for t in self.ticket_reports:
            for l in str(t).split('\n'):
                ret += f'\t{l}\n'
        return ret
