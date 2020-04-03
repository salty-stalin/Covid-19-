import os

a = open("country_names.txt", "w")
for path, subdirs, files in os.walk(r'Countries File'):
   for filename in files:
      a.write(filename + os.linesep) 
