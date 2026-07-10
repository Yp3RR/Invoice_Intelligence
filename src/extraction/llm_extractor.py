# import numpy as np
# import pandas as pd
import pdfplumber as pp
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

def extract_text_from_pdf(invoice_pdf):
    with pp.open(invoice_pdf) as pdf:
        extracted_text = ""
        for i,page in enumerate(pdf.pages):
            text = page.extract_text()
            extracted_text += text
        return extracted_text

def extract_invoice_fields(extracted_text):
    client = groq(api_key = API_KEY)


    
if __name__=="__main__":
    invoice_pdf = "../../data/raw/invoice_Scot Coram_29686.pdf"
    extracted_text = extract_text_from_pdf(invoice_pdf)
    print(text)


