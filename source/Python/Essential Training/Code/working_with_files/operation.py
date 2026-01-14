import os

#Read
os.system('cls')
f = open('working_with_files/data/file.txt', 'r')

'''
print(f)
print(f.readlines())
'''

for line in f.readlines():
    print(line.strip())

f.close()

#Write/Create
f = open('working_with_files/data/output.txt', 'w')
print(f)

f.write('Line 1\n')
f.write('Line 2\n')

f.close()

#Append
f = open('working_with_files/data/output.txt', 'a')
print(f)

f.write('Line 3\n')
f.write('Line 4\n')
f.close()

#Nice way
with open('working_with_files/data/output.txt', 'a') as f:
    f.write('some stuff\n')
    f.write('some other stuff\n')

print(f)