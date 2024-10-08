import docx
from docx.enum.text import WD_BREAK
from docx.oxml.ns import nsdecls, qn

def findSize(doc,i):
    paragraph = doc.paragraphs[i]

    # Verifica se o estilo é válido
    if paragraph.style and paragraph.style.font:
        font_size = paragraph.style.font.size
        if font_size:
            return font_size.pt  # Retorna o tamanho em pontos se encontrado

    # Se não encontrou no estilo, procura nos runs
    for run in paragraph.runs:
        for elem in run._r:
            sz = elem.find(qn('w:sz'))
            if sz is not None:
                return int(sz.get(qn('w:val'))) / 2  # Divide por 2 para half-points

    return None  # Retorna None se não encontrar 