from pypdf import PdfReader
from docx import Document

def temp(file):
    ...
    print(file, type(file))
    # EXTRACT & SAVE DATA FROM scope FORM FIELDS:


    scope_reader = PdfReader(file)
    scope_number_of_pages = len(scope_reader.pages)
    scope_page = scope_reader.pages[0]
    scope_text = scope_page.extract_text()
    scope_fields = scope_reader.get_fields()

    # pprint(scope_fields)

    extracted_data = {}

    for field in scope_fields:
        question = scope_fields[field]['/T']
        answer = scope_fields[field]['/V']
        extracted_data[question] = answer
        print(f'{question}: {answer}')

    print(extracted_data)


def tempo(file):
    ...

    doc = Document(file)
    
    # Replace placeholders in the document
    for paragraph in doc.paragraphs:
        print(paragraph)
    
    # Save the modified document
    doc.save('output.docx')