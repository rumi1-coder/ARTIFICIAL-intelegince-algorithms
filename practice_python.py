print('saad is my bro')
#\n\b\t\a\r
print("saad is my bro")
print("saad's my bro")
#
namef="saad"
namel="shahid"
print(f'{namef}')
print('{},{}'.format(namef,namel))
#
print(namef.title())
print(namef.upper())
print(namel.lower())
#
name_space=' saad   '
print(name_space.rstrip())
print(name_space.lstrip())
print(name_space.strip())

a,b,c=2,3,4
#
number=10_000_00
print(number)
#
friends=['zainullah','uqail']
print(friends)
print(friends[0])
print(friends[-1])
#
names=[]
names2=['saad','talha','maryam']
names.append('wania')
names.insert(3,'ali')
del names[0]
print(names)
print(names.pop())
print(names.pop(0))
print(names.remove('maryam'))
names.append('wania')
names.insert(3,'ali')
names.sort()
names.sort(reverse=True)
print(sorted(names))
names.reverse()
print(len(names))
