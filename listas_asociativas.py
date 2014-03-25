#!/usr/bin/python

l = {'nombre':'Hector','apellido':'Poli'}
print(l)
print(l['nombre'])
c = l.keys()
print(c)
print(l[c[0]])
l.update({'cedula':'15712796'})
print(l)

for key in l.keys():
	print "%s -> %s"%(key,l[key])
