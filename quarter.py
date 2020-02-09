class Quarter(object):
    def __init__(self, p, d):
        self.purchaces = p
        self.disposals = d
        self.trade_tickets = []
    
    def validate(self):
        return True

    def __str__(self):
        return f"Purchaces: {self.purchaces}\nDisposals: {self.disposals}\n"

        
class Quarter_Error(object):
    def __init__(self, q):
        self.quarter = q
        self.errors = []

    def __str__(self):
        return ''
