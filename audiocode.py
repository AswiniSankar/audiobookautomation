import pyttsx3 
import PyPDF2

book = open('oscarstory.pdf', 'rb') #pdf to read
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages #get the page count of pdf
#print(pages)
page = pdfReader.getPage(3) #get starting page of the pdf
speaker = pyttsx3.init() 
speaker.setProperty("rate", 120)
speaker.setProperty('volume', 0.4)
for num in range(3, pages): #reading each page
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()  

