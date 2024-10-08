import docx
from docx.enum.text import WD_BREAK
from docx.oxml.ns import nsdecls, qn

def findBreak(doc,i):
    finded = False
    for run in doc.paragraphs[i].runs:
            for elem in run._r:
                if elem.tag == qn('w:br') and elem.get(qn('w:type')) == 'page':
                    finded = True
                    break

            if finded == True:
                break
    
    return finded