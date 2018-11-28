import docx2txt

s=docx2txt.process("C:\\Users\\cidro\\Desktop\\pythonpip\\real.docx")
start = 'Nombre:'
end = 'RUT:'
print ("Nombre"+s[s.find(start)+len(start):s.rfind(end)])

