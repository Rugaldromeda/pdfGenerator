Automação que tem como propósito transformar cada página de qualquer arquivo docx em um pdf, desde que existam quebras de página inseridas, o sistema identifica as quebras de página verificando a camada de informações xml através da lib python-docx. 

Para gerar um executável deve-se utilizar os comandos:
pip install pyinstaller
pyinstaller --onefile --console main.py

E clicar no executável "main" dentro da pasta dist, que será gerada após os comandos. 