"""
required libraries, use:
pip install pyttsx3 - text to speech
pip install PyPDF2 - PDF-interpreter
"""
import pyttsx3
import PyPDF2

book_file = 'FOLDER ADDRESS TO PDF HERE'
#sets the reading speed
read_speed = 140
#uses the built in voices of the operating system
voice_id = 0

speak = pyttsx3.init()
book = open(book_file, 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)

pages = pdf_reader.numPages
print(pages)

def reader():
"""
sets a range of pages that the user wants recorded. 
Books are saved to the same folder as the project.  
"""
    for num in range(0, 10):
        page = pdf_reader.getPage(num)
        text = page.extractText()

        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[voice_id].id)
        #speak.say(f"Page {num + 1}" + ", -" + text)
        speak.setProperty('rate', read_speed)
        speak.runAndWait()
        speak.save_to_file(f"Page {num + 1}" + ", -" + text, "FILENAME.mp3")

book.close()