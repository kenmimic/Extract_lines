def extractlines(file,start,end):
  file=open(file)
  inRecordingMode= False
  for line in file:
    if not inRecordingMode:
      if start in line:
        inRecordingMode= True
    elif end in line:
      inRecordingMode = False
    else:
      yield line

for n in extractlines('./rs.py','start','end'):
  print(n.strip('\n'))

