import os

line = input("Enter lab name: ")
line = line.replace(" ","-",)
cwd = os.getcwd()
path = cwd + '/XXE/' + line
os.mkdir(path)
os.system(f"touch {path}/Findings")

print(line)
