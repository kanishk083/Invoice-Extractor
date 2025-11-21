#  Invoice Extractor : Invoice Understanding Model

The **Invoice Extractor** is an GENAI Streamlit application that intelligently reads invoices whether clean PDFs or low-quality scanned images and extracts all the important information automatically.  
Powered by **Google Gemini**, this tool transforms any invoice into a clear, human-friendly explanation and summary.

---

##  Features

###  AI-Based Invoice Extraction  
- Extracts seller details, buyer details, items, totals, tax values, payment terms, dates, and more.  
- Works with **digital PDFs**, **scanned invoices**, **photos**, and **handwritten** or **rotated** images.

###  Smart Storytelling Prompt  
A custom-crafted prompt helps the model understand and describe the invoice naturally and accurately.

###  Multi-Format Image Support  
Accepts:
- JPG  
- JPEG  
- PNG  

Automatically converts the image into the correct format for Gemini.

###  Human-Friendly Summary  
Along with extraction, the tool also generates an easy-to-read summary explaining:
- Who issued the invoice  
- What the charges are for  
- Items/services  
- Total payable amount  
- Any notes or deadlines  

###  Simple Streamlit UI  
A clean interface where users can upload an invoice and instantly see extraction + summary.

---

##  Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API (Generative AI)**
- **Pillow (PIL)** — Image Processing
- **python-dotenv** — Environment variable handling

---

##  How It Works

1. User uploads an invoice image.  
2. The app processes the image into a model-ready format.  
3. Gemini receives:  
   - A storytelling extraction prompt  
   - The invoice image  
   - Optional user input  
4. Gemini returns:  
   - A detailed invoice breakdown  
   - A human-readable summary  
5. Streamlit displays the extraction neatly on screen.

---

