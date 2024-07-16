# inventory/utils.py

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa

def generate_pdf(context):
    
    buffer = BytesIO()
    
    
    html = render_to_string('inventory/pdf_template.html', context)
    
    
    pisa_status = pisa.CreatePDF(html, dest=buffer)
    
    
    if pisa_status.err:
        return None
    return buffer.getvalue()
