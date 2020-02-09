from pdfscrape import Scraped_PDF
import PyPDF2
import os
from pdf_annotate import PdfAnnotator, Appearance, Location

annotator = PdfAnnotator(os.getcwd()+'/trade_tickets/Company_Q2_p1.pdf')
annotator.add_annotation('square',Location(x1=300, y1=265, x2=500, y2=330, page=0),Appearance(stroke_color=(1, 0, 0), stroke_width=3),)
annotator.write('annotated.pdf')

class Annotate(object):
    def __init__(self, pdf_obj):
