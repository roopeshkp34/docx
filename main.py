import json
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.shared import Inches

def _json_():
    with open("test_data.json", "r") as f:
        data = json.load(f)
    return data

document = Document()
new_height = Inches(8.5)
new_width = Inches(16)
for index, page in enumerate(_json_()):
    section = document.sections[0]
    if index > 0:
        section = document.add_section()

    if page["orientation"] == "landscape":
        section.orientation = WD_ORIENT.LANDSCAPE
        section.page_width = new_width
        section.page_height = new_height
    elif page["orientation"] == "portrait":
        section.orientation = WD_ORIENT.PORTRAIT
        section.page_width = new_height
        section.page_height = new_width

document.save("text.docx")