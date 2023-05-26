curso = 'pYthon'

print(curso.upper())
print(curso.lower())
print(curso.title())

print("-----------------------------------------")

curso = "          Python          "
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())

texto = "         Teste strip   "
print(texto)
print(texto.strip() + ".")
print(  "." + texto.lstrip() + "." )
print(texto.rstrip())

print("--- JUNÇÃO E CENTRALIZAÇÃO ---")
curso = "Java"
print(curso.center(12,"#"))
print(curso.center(10))
print("-".join(curso))