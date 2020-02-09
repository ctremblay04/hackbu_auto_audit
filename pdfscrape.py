import PyPDF2
import re
import os

class Scraped_PDF(object):
    def __init__(self, path):
        self.path = path
        self.scrape_pdf()

    def scrape_pdf(self):
        pdfFileObject = open(os.getcwd()+self.path, 'rb')
        pdf_info = list(filter(lambda x : any(c.isalnum() for c in x), PyPDF2.PdfFileReader(pdfFileObject).getPage(0).extractText().split('\n')))
        print(pdf_info)
        try:
            self.company_name = pdf_info[2]
        except:
            self.company_name = None
        
        try:
            self.transaction_type = pdf_info[pdf_info.index('Trans Type') + 2]
        except:
            self.transaction_type = None
        
        try:
            self.quantity = int(pdf_info[pdf_info.index('Quantity') + 2].replace(',', '')[1:])
        except:
            self.quantity = None

        try:
            self.price_per_share = int(pdf_info[pdf_info.index('PPS') + 2][1:])
        except:
            self.price_per_share = None

        try:
            self.date_of_order = pdf_info[pdf_info.index('Date of Order: ') + 1]
        except:
            self.date_of_order = None
    
        try:
            self.custodian = pdf_info[pdf_info.index('Custodian: ') + 1]
        except:
            self.custodian = None

        try:
            self.security = pdf_info[pdf_info.index('Security') + 2]
        except:
            self.security = None

        try:
            self.type = pdf_info[pdf_info.index('Type of ') + 2]
        except:
            self.type = None
        
        try:
            self.broker_dealer = pdf_info[pdf_info.index('Broker/Dealer') + 2]
        except:
            self.broker_dealer = None
        
        try:
            self.phone = pdf_info[pdf_info.index('Phone:') + 2]
        except:
            self.phone = None
        
        try:
            self.amount = quantity * price_per_share
        except:
            self.amount = None
        
        self.valid_pdf = self.amount != None and self.transaction_type != None and self.quantity != None
        pdfFileObject.close()

    def __str__(self):
        return ''


class trade_ticket(object):
    
    def __init__(self, obj):
        self.company_name = obj.company_name
        self.transaction_type = obj.transaction_type
        self.amount = obj.amount
    
    def __str__(self):
        return f'Company name: {self.company_name}\nTransaction Type: {self.transaction_type}\nAmount: {self.amount}\n'


if __name__ == "__main__":
    spdf = Scraped_PDF('/trade_tickets/CompanyA_Q2_p1.pdf')
    alex = trade_ticket(spdf)
    print(alex)



