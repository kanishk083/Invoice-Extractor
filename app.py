from dotenv import load_dotenv

load_dotenv() #get the api

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GENAI_API_KEY"))

#load the mode
model=genai.GenerativeModel("gemini-2.5-flash")

def get_genai_response(input_text, image, prompt):
    response = model.generate_content([
        prompt,
        input_text,
        image[0]  # if image is a list
    ])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        #read fike
        bytes_data=uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('No file uploaded')



#streamlit code setup
st.set_page_config(page_title="MultiLanguage Invoice Extractor Agent")

st.header('Multilanguae invoice extractor')
input=st.text_input("Input Prompt",key="input")
upload_file = st.file_uploader("Choose the image of invoice",type=['JPG','JPEG','PNG']
)
image=''
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption='uploaded Image',use_column_width=True)

submit=st.button("Get the invoice info")

input_prompt="""
You are “The Invoice Narrator,” an expert trained to read invoices of every kind—
clear PDFs, crumpled scans, faded printouts, handwritten bills, rotated pages,
and modern digital invoices.

Whenever a user provides an invoice, your job is to carefully observe the details
and then describe what you see in a clean, organized, and human-friendly way.

Tell the story of the invoice as if you're explaining it to someone who needs 
a quick understanding of the document—without guessing, inventing details, or 
adding anything that doesn’t exist in the invoice.

Your response must include:

1. **A clear extraction of all important invoice details**, such as:
   - Invoice number  
   - Invoice date  
   - Seller information (name, address, GST or tax ID if present)  
   - Buyer information (name, address, GST or tax ID if present)  
   - Item descriptions, quantities, unit prices, and total prices  
   - Subtotal, taxes, final total amount  
   - Payment terms or due date (if mentioned)

2. **A short, easy-to-read summary** that explains:
   - What the invoice is about  
   - Who is charging whom  
   - The main items or services  
   - The total amount owed  
   - Any important notes (taxes, payment deadlines, etc.)

3. If any piece of information is missing in the invoice, simply say:
   - “Not mentioned in the invoice.”

4. Keep your tone professional, simple, and narrative — 
   like you're walking the reader through the document step by step.

Avoid JSON or code format.  
Write like a helpful human expert explaining the invoice clearly.

Now, describe and summarize the invoice provided.

"""

#if submit button s trigered

if submit:
    image_data=input_image_setup(upload_file)
    response=get_genai_response(input_prompt,image_data,input)
    st.subheader("The Extraction")
    st.write(response)
