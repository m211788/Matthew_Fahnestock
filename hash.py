import os
import sys
import hashlib
Path = "/"
Dirs = os.listdir(Path)
Direct = []
Hashed = []
for file in Dirs:
  if (file=="dev") or (file=="proc") or (file=="sys") or (file=="tmp") or (file =="var/lib") or (file=="var/run"):
    direct.append("/" + file)
    continue
  else:
    if "." in file or "+" in file:
      direct.append("/" + file)
      continue
    else:
      Newpath = "/" + file
      for root, dirs, files in os.walk(Newpath topdown=False):
        for name in files:
          direct.append(os.path.join(root, name))
        for name in dirs:
          direct.append(os.path.join(root, name))

for i in Direct:
  m=hashlib.sha256()
  m.update(i)
  FullHash=m.digest()
  Hashed.append(FullHash)

with open('hashed.txt', 'w') as f: #stackbuse.com/writing-to-a-file-with-pythons
  for k in Hashed:
    print(k, file=f)
