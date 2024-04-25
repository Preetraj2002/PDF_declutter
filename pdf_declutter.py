from PyPDF2 import PdfReader,PdfWriter

duplicate = set()

pdf_reader = PdfReader("Hashing.pdf")
pages = pdf_reader.pages

for pg_no,page in enumerate(pdf_reader.pages):
    print("Page: ", pg_no)
    print("==========================")
    if pg_no == len(pages)-1:
        break
    
    if pages[pg_no].extract_text() == pages[pg_no+1].extract_text():
        duplicate.add(pg_no)


pdf_writer = PdfWriter()
print("Duplicates: ", duplicate)
    
for i in range(len(pages)):
    if i not in duplicate:
        p = pdf_reader.pages[i]
        pdf_writer.add_page(p)
    
with open("newHash.pdf","wb") as f:
    pdf_writer.write(f)
    
    

    
    