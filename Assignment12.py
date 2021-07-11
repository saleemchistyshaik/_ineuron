1.In what modes should the PdfFileReader() and PdfFileWriter() File objects will be opened?
A.PdfFileReader() needs to be opened in read-binary mode by passing 'rb' as the second argument to open(). Likewise, the File object passed to PyPDF2.PdfFileWriter() needs to be opened in write-binary mode with 'wb'

2.From a PdfFileReader object, how do you get a Page object for page 5?
A.To extract text from a page, you need to get a Page object, which represents a single page of a PDF, from a PdfFileReader object. You can get a Page object by calling the getPage() method

3.What PdfFileReader variable stores the number of pages in the PDF document?
A.The total number of pages in the document is stored in the numPages attribute of a PdfFileReader object

4 If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?
import PyPDF2
pdfFile = open('temp.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
           pdfWriter.addPage(pdfReader.getPage(pageNum))
pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()

5.What methods do you use to rotate a page?
A.While viewing a PDF document, press the "Ctrl+Shift+L" keys or "Ctrl+Shift+R" keys to rotate the current page to the left or right.

6.What is the difference between a Run object and a Paragraph object?
A.The Document object contains a list of Paragraph objects for the paragraphs in the document.
A Run object is a contiguous run of text with the same style.

7.How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?
A.When we call len() on doc.paragraphs, it returns x, which tells us that there are some x a list of Paragraph objects for a Document object that is stored in a variable named doc

8.What type of object has bold, underline, italic, strike, and outline variables?
A.A Run object has these variables (not a paragraph)

9.What is the difference between False, True, and None for the bold variable?
A.True always makes the Run object bolded and False makes it always not bolded, no matter what the style's bold setting is. None will make the Run object just use the style's bold setting.

10.How do you create a Document object for a new Word document?
A.Call the docx.Document() function

11.How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?
A.doc.add_paragraph('Hello there!')

12.What integers represent the levels of headings available in Word documents?
A.The integers 0,1,2,3, and 4
