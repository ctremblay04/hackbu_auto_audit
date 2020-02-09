import PyPDF2
import re
#from pdf_annotate import PdfAnnotator, Appearance, Location

class Scraped_PDF(object):
    def __init__(self, path):
        self.path = path
        self.scrape_pdf()

    def scrape_pdf(self, path):
        pdfFileObject = open(path, 'rb')
        pdf_info = PyPDF2.PdfFileReader(pdfFileObject).getPage(0).extractText().split('\n')
        self.company_name = pdf_info[2]
        self.transaction_type = pdf_info[pdf_info.index('Trans.Type') + 2]
        q = pdf_info[pdf_info.index('Quantity') + 2].replace(',', '')
        pps = pdf_info[pdf_info.index('PPS') + 2]
        self.quantity = int(q) if q else None
        self.price_per_share = int(pps[1:]) if pps else None
        self.date_of_order = pdf_info[pdf_info.index('Date of Order: ') + 1]
        self.custodian = pdf_info[pdf_info.index('Custodian: ') + 1]
        self.security = pdf_info[pdf_info.index('Security') + 2]:
        self.type = pdf_info[pdf_info.index('Type of ') + 2]:
        self.broker_dealer = pdf_info[pdf_info.index('Broker/Dealer') + 2]:
        self.phone = pdf_info[pdf_info.index('Phone:') + 2]:
        self.ammount = quantity * price_per_share
        pdfFileObject.close()



class trade_ticket(object):
    def __init__(self, obj):
        self.company_name = obj.company_name
        self.transaction_type = obj.transaction_type
        self.ammount = self.ammount

    
    def __str__(self):
        return f"Company name: {self.company_name}\nTransaction Type: {self.transaction_type}\nAmmount: {self.ammount}\n"


if __name__ == "__main__":
    alex = trade_ticket('trade1.pdf')



