a=dict({1001:"zhang",1004:"li"})
b=dict(((1001,"zhang"),(1004,"li")))
c=dict([(1001,"zhang"),(1004,"li")])
d=dict(zip([1001,1004],["zhang","li"]))
e={}
f=dict()

a[1003]="wang"
print(a,b,c,d,e,f,type(e),type(f),a[1001],a.pop(1003))
print(a.items(),a.keys(),a.values())

for key in a.keys():
    print(str(key))
for key in a.values():
    print(str(key))
for key in a.items():
    print(str(key))