from pypdf import PdfReader

def traditional_parse(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text = full_text + page.extract_text() + "\n"
    return full_text

full_text = traditional_parse("./extreme_rag_test.pdf")
with open("./nvidia_report_traditional_output.txt", 'w') as f:
    f.write(full_text)