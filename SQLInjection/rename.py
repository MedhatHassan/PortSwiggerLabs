import os

line = input("Enter lab name: ")
line = line.replace(',','')
line = line.replace(" ","-",)
cwd = os.getcwd()
path = cwd + '/SQLInjection/' + line
os.mkdir(path)
os.system(f"touch {path}/Findings")

print(line)
