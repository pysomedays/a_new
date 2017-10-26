from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file, 'r').read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
if not exists(to_file):
    pass

print("Ready, hit RETURN to continue, CTRL- C to abort.")

outfile = open(to_file, 'w') #如果有则打开，否则新建
outfile.write(indata)

print("Alright, all done.")

outfile.close()