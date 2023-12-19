from PyPDF2 import PdfReader
from gtts import gTTS
import tkinter as tk
from tkinter import filedialog
import random

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        convert_pdf_to_audiobook(file_path)

def convert_pdf_to_audiobook(pdf_file_path):
    reader = PdfReader(pdf_file_path)
    page = reader.pages[0]
    text = page.extract_text()
    
    tts = gTTS(text, lang='en', slow=False)
    name = rf"C:\Users\SIEMENS\OneDrive\Desktop\_audiobook_{random.randint(1,1000000000000)}.mp3"  //path of the file 
    audio_file_path = name
    tts.save(audio_file_path)

root = tk.Tk()
root.title("PDF to Audiobook Converter")

select_button = tk.Button(root, text="Select PDF File", command=select_pdf_file)
select_button.pack(pady=20)

root.mainloop()
