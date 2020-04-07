import os

a = open("country_names.txt", "w")
for path, subdirs, files in os.walk(r'Countries File'):
   for filename in files:
      a.write(filename + os.linesep) 
a.close()

b=open("country_names.txt","r")


Lines = b.readlines() 
c=open("country_names.txt","w")

# Strips the newline character 
for line in Lines: 
    line = line.replace(' ', '_')
    c.write(line)
