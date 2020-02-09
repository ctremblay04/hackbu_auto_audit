class Quarter(object):
    def __init__(self, p, d):
        self.purchases = p
        self.disposals = d
        self.trade_tickets = []
    
    def validate(self):
        ret = Quarter_Report(self)
        ret.purchase_discrepancy = self.purchases
        ret.disposal_discrepancy = self.disposals
        for t in trade_tickets:
            if t.valid:
                if t.transaction_type = 'Buy':
                    ret.purchase_discrepancy -= t.amount
                else:
                    ret.disposal_discrepancy += t.amount
            ret.ticket_reports.append(t.generate_report())
        return ret

    def __str__(self):
        return f"Purchases: {self.purchases}\nDisposals: {self.disposals}\n"

        
class Quarter_Report(object):
    def __init__(self, q):
        self.quarter = q
        self.purchase_discrepancy = 0
        self.disposal_discrepancy = 0
        self.ticket_reports = []

    def __str__(self):
        #TODO
        return ''
