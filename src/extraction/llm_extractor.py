 # import numpy as np
# import pandas as pd
import pdfplumber as pp
from dotenv import load_dotenv
from groq import Groq
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
    client = Groq(api_key = API_KEY)

    chat = client.chat.completions.create(
        messages=[
            {
                
                "role" : "system",
                "content" : '''You are a data extraction bot. output valid raw JSON and 
                dont include anything related to conversation''',
                
            },
            {
                
                "role" : "user",
                "content" : f'''{extracted_text} You are given a raw data from an invoice in pdf format. extract all the
                necessary fields. if a field is missing return null.Amount is equal to quantity times rate and total 
                equal to subtotal + shipping''',
                
            }
        ],
        model = "llama-3.3-70b-versatile",
    )

    print(chat.choices[0].message.content)
    
if __name__=="__main__":
    invoice_pdf = "../../data/raw/invoice_Scot Coram_29686.pdf"
    extracted_text = extract_text_from_pdf(invoice_pdf)
    llm_extracted_fields = extract_invoice_fields(extracted_text)


