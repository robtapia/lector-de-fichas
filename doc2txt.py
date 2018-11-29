import docx2txt

s=docx2txt.process("C:\\Users\\cidro\\Desktop\\pythonpip\\real.docx")
start = 'Nombre:'
end = 'RUT:'
NOMBRE=s[s.find(start)+len(start):s.rfind(end)]
NOMBRE=NOMBRE.strip()
print("Nombre: "+NOMBRE)
start='RUT:'
end='Edad:'
RUT=s[s.find(start)+len(start):s.rfind(end)]
RUT=RUT.strip()
print("rut: "+RUT)
start='Edad:'
end='F.N.:'
EDAD=s[s.find(start)+len(start):s.rfind(end)]
EDAD=EDAD.strip()
print("Edad: "+EDAD)
start='F.N.:'
end='Dirección:'
FN=s[s.find(start)+len(start):s.rfind(end)]
FN=FN.strip()
print("F.N: "+FN)
start='Dirección:'
end='Teléfono:'
DIRECCION=s[s.find(start)+len(start):s.rfind(end)]
DIRECCION=DIRECCION.strip()
print("Dirección: "+DIRECCION)
start='Teléfono:'
end='Previsión:'
FONO=s[s.find(start)+len(start):s.rfind(end)]
FONO=FONO.strip()
print("Teléfono: "+FONO)
start='Previsión:'
end='Correo:'
PREV=s[s.find(start)+len(start):s.rfind(end)]
PREV=PREV.strip()
print("Previsión: "+PREV)
start='Correo:'
end='Fecha Apertura:'
CORREO=s[s.find(start)+len(start):s.rfind(end)]
CORREO=CORREO.strip()
print("Correo: "+CORREO)
start='Fecha Apertura:'
#end='Fecha Apertura:'
FECHA=s[s.find(start)+len(start):s.find(start)+len(start)+10]
FECHA=FECHA.strip()
print("Fecha de primera consulta: "+FECHA)



