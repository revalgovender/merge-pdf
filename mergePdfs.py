from PyPDF2 import PdfFileMerger

pdfs = [
    'file-1',
    'file-2',
    'file-3',
    'file-4',
]

merger = PdfFileMerger(strict=False)

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('result.pdf', 'wb') as fout:
    merger.write(fout)