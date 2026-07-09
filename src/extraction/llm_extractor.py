# import numpy as np
# import pandas as pd
import pdfplumber as pp

invoice_pdf = "../../data/raw/invoice_Scot Coram_29686.pdf"

with pp.open(invoice_pdf) as pdf:
    for i,page in enumerate(pdf.pages):
        text = page.extract_text()
        print(f"---{i+1}---")
        print(text)

