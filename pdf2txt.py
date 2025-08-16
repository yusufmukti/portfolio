from pdfminer.high_level import extract_text

pdf_path = "doc/Resume.pdf"  # Change to your PDF file path
text = extract_text(pdf_path)

with open("doc/Resume.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("PDF converted to doc/Resume.txt")