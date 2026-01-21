import os
# This tells HuggingFace to use your project folder for storage
os.environ["HF_HOME"] = os.path.join(os.getcwd(), "hf_cache")

from docling.document_converter import DocumentConverter


def docling_parser(pdf_path):
    converter = DocumentConverter()
    result = converter.convert(pdf_path)
    markdown_output = result.document.export_to_markdown()
    return markdown_output



full_text = docling_parser("./extreme_rag_test.pdf")
with open("./nvidia_report_docling_output.txt", 'w') as f:
    f.write(full_text)