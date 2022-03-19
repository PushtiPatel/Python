"""
@author Pushti(20CE099)
AIM: Generate PDF file of your 3rd Semester Mark-sheet
"""
import aspose.words as aw
# load the PDF file
doc = aw.Document("result.pdf")
# convert PDF to Word DOCX format
doc.save("pushti_result_new.docx")
# Load word document
doc = aw.Document("pushti_result_new.docx")
# Save as PDF
doc.save("pushti_result_new2.pdf")