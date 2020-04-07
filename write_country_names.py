import os

a = open("country_names.txt", "w")
for path, subdirs, files in os.walk(r'Countries File'):
   for filename in files:
      filename_new= filename.replace(' ', '_')
      a.write(filename_new + os.linesep) 
      os.rename("Countries File\\"+str(filename),"Countries File\\"+str(filename_new))
a.close()

