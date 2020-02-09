import PyPDF2
import re
import os
import sys
from pdf_annotate import PdfAnnotator, Appearance, Location
import trade_ticket
from company import *

class Scraped_PDF(object):
    def __init__(self, path):
        self.path = path
        self.scrape_pdf()

    def scrape_pdf(self):
        pdfFileObject = open(os.getcwd()+"/"+self.path, 'rb')
        pdf_info = list(filter(lambda x : any(c.isalnum() for c in x), PyPDF2.PdfFileReader(pdfFileObject).getPage(0).extractText().split('\n')))
        for i, x in enumerate(pdf_info):
            pdf_info[i] = x.strip()

        annotator = PdfAnnotator(os.getcwd()+self.path)
        annotated = False

        self.company_name = pdf_info[1]

        if pdf_info.index('Trans Type') == pdf_info.index('Quantity') - 2:
            self.transaction_type = pdf_info[pdf_info.index('Trans Type') + 1]
        else:
            self.transaction_type = None
            annotator.add_annotation('square',Location(x1=80, y1=435, x2=140, y2=490, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        if pdf_info.index('Quantity') == pdf_info.index('PPS') - 2:
            self.quantity = int(pdf_info[pdf_info.index('Quantity') + 1].replace(',', ''))
        else:
            self.quantity = None
            annotator.add_annotation('square',Location(x1=160, y1=435, x2=220, y2=490, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        if pdf_info.index('PPS') == pdf_info.index('Security') - 2:
            self.price_per_share = int(pdf_info[pdf_info.index('PPS') + 1][1:len(pdf_info[pdf_info.index('PPS') + 1])-3])
        else:
            self.price_per_share = None
            annotator.add_annotation('square',Location(x1=225, y1=435, x2=285, y2=490, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        if len(pdf_info[3]) > 14:
            self.date_of_order = pdf_info[3][15:]
        else:
            print("date of order missing")
            self.date_of_order = None
            annotator.add_annotation('square',Location(x1=150, y1=570, x2=280, y2=590, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        if len(pdf_info[4]) > 10:
            self.custodian = pdf_info[4][11:]
        else:
            self.custodian = None
            annotator.add_annotation('square',Location(x1=130, y1=540, x2=280, y2=565, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        if pdf_info.index('Security') == pdf_info.index('Type of Order') - 2:
            self.security = pdf_info[pdf_info.index('Security') + 1]
        else:
            self.security = None
            annotator.add_annotation('square',Location(x1=295, y1=435, x2=360, y2=490, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        if pdf_info.index('Type of Order') == pdf_info.index('Instructions') - 2:
            self.type = pdf_info[pdf_info.index('Type of Order') + 1]
        else:
            self.type = None
            annotator.add_annotation('square',Location(x1=360, y1=435, x2=460, y2=490, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        if pdf_info.index('Broker/Dealer') == pdf_info.index('Broker/Dealer Representative') - 2:
            self.broker_dealer = pdf_info[pdf_info.index('Broker/Dealer') + 1]
        else:
            self.broker_dealer = None
            annotator.add_annotation('square',Location(x1=70, y1=330, x2=285, y2=400, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        if pdf_info.index('Broker/Dealer Representative') == pdf_info.index('Comments:') - 2:
            self.broker_dealer_representative = pdf_info[pdf_info.index('Broker/Dealer Representative') + 1]
        else:
            self.broker_dealer_representative = None
            annotator.add_annotation('square',Location(x1=300, y1=330, x2=500, y2=400, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        if pdf_info.index('Phone:') == pdf_info.index('Signature:') - 3:
            self.phone = pdf_info[pdf_info.index('Phone:') + 1] + "-" + pdf_info[pdf_info.index('Phone:') + 2]
        else:
            self.phone = None
            annotator.add_annotation('square',Location(x1=300, y1=265, x2=500, y2=330, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
            annotated = True

        try:
            self.amount = self.quantity * self.price_per_share
        except:
            self.amount = None

        if annotated:
            # os.mkdir(os.getcwd() + "/ANNOTATED/trade_tickets")
            annotator.write(os.getcwd()+"/ANNOTATED"+self.path)
            # else maybe move it to the completed folder

        self.valid_pdf = self.amount != None and self.transaction_type != None and self.quantity != None
        pdfFileObject.close()

    def __str__(self):
        return ''

'''
class trade_ticket(object):

    def __init__(self, obj):
        self.company_name = obj.company_name
        self.transaction_type = obj.transaction_type
        self.amount = obj.amount

    def __str__(self):
        return f'Company name: {self.company_name}\nTransaction Type: {self.transaction_type}\nAmount: {self.amount}\n'
'''

if __name__ == "__main__":
    #companyName = sys.argv[1]
    companies = Company.construct("CostRollExample.xlsx")
    trade_tickets = []
    for subdir, dir, files in os.walk(os.getcwd() + "/trade_tickets/") :
        for file in files:
            q = int(file[file.index('_')+2])
            scraped = Scraped_PDF("/trade_tickets/" + file)
            tradeticket = trade_ticket.Trade_Ticket(scraped, q)
            companies[tradeticket.company_name].quarters[q-1].trade_tickets.append(tradeticket)

    company_reports = []
    for c in companies:
        company_reports.append(companies[c].validate())
        print(companies[c])

    for c in company_reports:
        print(c)





