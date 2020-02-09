import pdfscrape

class Trade_Ticket(object):
    def __init__(self, obj, q):
        self.company_name = obj.company_name
        self.transaction_type = obj.transaction_type
        self.amount = obj.amount
        self.valid = obj.valid_pdf
        self.quarter = q
        self.report = Trade_Ticket_Report(self)

    def validate(self):
        return self.report

    def __str__(self):
        return f'Company name: {self.company_name}\nTransaction Type: {self.transaction_type}\nAmount: {self.amount}\n'

class Trade_Ticket_Report(object):
    def __init__(self, ticket):
        self.ticket = ticket

    def __str__(self):
        #TODO
        return 'THIS IS A TRADE TICKET REPORT'
