edad=18
m_edad=18
#condicion
if edad >= m_edad:
    print "Eres mayor de edad"
    if True:
        print 'Esto se ejecuta siempre que sea mayor de edad'
#"else" debe ir en la misma indentacion que el "if" al que corresponde
    else:
        print "Lo que sea"
else:
    print "No eres mayor de edad"

##encouding: utf-8 para que aparesca la ñ
if edad >= 0 and edad < 18:
    print "Eres un niño"
elif edad >= 18 and edad <27:
    print "Eres un joven"
elif edad >=27 and edad <60:
    print "Eres un adulto"
else:
    print "Eres de la tercera edad"
