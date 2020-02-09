import pdfscrape

class Trade_Ticket(object):
    def __init__(self, obj):
        self.company_name = obj.company_name
        self.transaction_type = obj.transaction_type
        self.amount = obj.amount
        self.valid = obj.valid_pdf
    
        self.generate_report()
    
    def validate():
        return Trade_Ticket_Report(self)
    
    def __str__(self):
        return f'Company name: {self.company_name}\nTransaction Type: {self.transaction_type}\nAmount: {self.amount}\n'

class Trade_Ticket_Report(object):
    def __init__(self, ticket):
        self.ticket = ticket
    
    def __str__(self):
        #TODO
        return ''

if __name__ == "__main__":
    spdf = Scraped_PDF('/tmp/trade_tickets/CompanyA_Q2_p3.pdf')
    alex = trade_ticket(spdf)
    print(alex)
