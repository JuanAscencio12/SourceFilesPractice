import csv
import os

os.system('cls')

'''
#print data without header
with open('working_with_files/data/10_02_us.csv','r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)#To skip the header
    for row in reader:
        print(row)

print(type(data))
'''

'''
#Make the data into a list
with open('working_with_files/data/10_02_us.csv','r') as f:
    reader = list(csv.reader(f, delimiter='\t'))
    for row in reader[1:]:
        print(row)
'''

'''
#Make the data into a dicy
with open('working_with_files/data/10_02_us.csv','r') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
        print(row)
'''

with open('working_with_files/data/10_02_us.csv','r') as f:
    data = list(csv.DictReader(f,delimiter='\t'))

primes = []
for number in range(2,99999):
    for factor in range(2, int(number ** 0.5)):
        if number % factor == 0:
            break
    else:
        primes.append(number)
#print(primes)

data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']

print(len(data))    
os.system('pause')
print(data)

print(data)    

with open('working_with_files/data/10_ma_prime.csv','w') as f:
    writter = csv.writer(f)
    for row in data:
        writter.writerow([row['place name'], row['state'], row['county']])
