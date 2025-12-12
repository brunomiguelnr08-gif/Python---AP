
#Tabelas de Verdade (Op. lóg. and, or, not 
print("--TABELA DE VERDADE OP. LÓG. AND") 
print ("A\tB\t\tA and B")
a=b=True
print (a,"\t",b,"\t\t", a and b)
a=True 
b=False
print (a,"\t",b,"\t\t", a and b) 
a=False
b=True
print (a,"\t",b,"\t\t", a and b) 
a=b=False
print (a,"\t",b,"\t\t", a and b) 
print ("--TABELA DE VERDADE - OP. LÓG. OR")
print("A\tB\t\tA and B") 
a=b=True
print (a,"\t",b,"\t\t", a or b) 
a=True
b=False
print (a,"\t",b,"\t\t", a or b) 
a=False
b=True
print (a,"\t",b,"\t\t", a or b) 
a=b=False
print (a,"\t",b,"\t\t", a or b)
print ("--TABELA DE VERDADE - OP. LÓG. NOT") 
print ("A\t\tnot(a)")
a=True
print (a,"\t\t", not a)
a=False
print (a,"\t\t", not a)