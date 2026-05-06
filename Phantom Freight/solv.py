import sys,struct

def R16(d,o):return struct.unpack(">H",d[o:o+2])[0]
def R32(d,o):return struct.unpack(">I",d[o:o+4])[0]

def F(j):
 s=[];i=2
 while i+4<=len(j)and j[i]==255:
  m=j[i+1];i+=2
  if m in(216,217):continue
  if i+2>len(j):break
  l=R16(j,i);i+=2
  if m==237:s.append(j[i:i+l-2])
  i+=l-2
 return s

def P(p):
 r=[];i=14
 while i+8<=len(p):
  id=R16(p,i+4);i+=6
  nlen=p[i];i+=1
  n=p[i:i+nlen];i+=nlen
  if(1+nlen)%2:i+=1
  if i+4>len(p):break
  sz=R32(p,i);i+=4
  if i+sz>len(p):break
  d=p[i:i+sz];i+=sz
  if sz%2:i+=1
  r.append({'id':id,'n':n,'d':d})
 return r

def X(d):
 v=d[4];l=R16(d,7)
 pw=d[9:9+l]
 return pw.hex()

f=sys.argv[1]
j=open(f,'rb').read()
for s in F(j):
 if s.startswith(b"Photoshop 3.0\x00"):
  for i in P(s):
   if i['id']==0x1FFF and i['n']==b'auth':
    print(X(i['d']))
