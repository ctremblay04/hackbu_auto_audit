import PyPDF2
import re
#from pdf_annotate import PdfAnnotator, Appearance, Location

def validate_format(pdf_info):
    if not pdf_info[2]:
        print("missing company name")
    if not pdf_info[pdf_info.index('Date of Order: ') + 1]:
        print("missing Date of Order")
    if not pdf_info[pdf_info.index('Custodian: ') + 1]:
        print("missing custodian")
    if not pdf_info[pdf_info.index('Trans.Type') + 2]:
        print("missing transaction type")
    if not pdf_info[pdf_info.index('Quantity') + 2]:
        print("missing Quantity")
    if not pdf_info[pdf_info.index('PPS') + 2]:
        print("missing PPS")
    if not pdf_info[pdf_info.index('Security') + 2]:
        print("missing security")
    if not pdf_info[pdf_info.index('Type of ') + 2]:
        print("missing type of field")
    if not pdf_info[pdf_info.index('Broker/Dealer') + 2]:
        print("missing Broker/Dealer")
    if not pdf_info[pdf_info.index('Phone:') + 2]:
        print("missing Phone")


    # annotator = PdfAnnotator('trade1.pdf')
    # annotator.add_annotation(
    #     'square',
    #     Location(x1=200, y1=600, x2=350, y2=550, page=0),
    #     Appearance(stroke_color=(1, 0, 0), stroke_width=3),
    # )
    # annotator.write('annotated.pdf')



def scrape_pdf(path):
    pdfFileObject = open(path, 'rb')
    pdf_info = PyPDF2.PdfFileReader(pdfFileObject).getPage(0).extractText().split('\n')
    print(pdf_info)
    validate_format(pdf_info)


    company_name = pdf_info[2]
    transaction_type = pdf_info[pdf_info.index('Trans.Type') + 2]
    quantity = int(pdf_info[pdf_info.index('Quantity') + 2])
    price_per_share = int(pdf_info[pdf_info.index('PPS') + 2])

    #error handling

    total_amt = quantity * price_per_share

    print('company_name: ' + company_name)
    print('transaction_type: ' + transaction_type)
    print('total_amt: ' + str(total_amt))
    pdfFileObject.close()
    return (company_name, transaction_type, total_amt)



class trade_ticket(object):
    def __init__(self, path):
        self.company_name, self.transaction_type, self.total_amt = scrape_pdf(path)


if __name__ == "__main__":
    alex = trade_ticket('trade1.pdf')



