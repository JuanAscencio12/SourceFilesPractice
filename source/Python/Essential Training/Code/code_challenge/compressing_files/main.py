import os
# Python code​​​​​​‌‌‌​​​​‌‌‌‌‌‌‌‌​​​‌​​‌‌‌​ below
def encodeString(stringVal):
    if not stringVal:
        return []

    result = []
    prevChar = stringVal[0]
    count = 1
    
    for char in stringVal[1:]:
        if char == prevChar:
            count += 1
        else:
            result.append((prevChar,count))
            prevChar = char
            count = 1 

    result.append((prevChar,count))
    return result

def decodeString(encodedList):
    if not encodedList:
        return None
    
    phraseList = [key * value for key,value in encodedList]
    phrase = "".join(phraseList)

    return phrase

#hacer decode y encode por cuenta propia
# The filename that will be passed to this function
# is code_challenge/compressing_files/file.txt

'''
#Video solution
#import json
def encodeFile(filename, newFilename):
    with open(filename, 'r') as f:
        data = encodeString(f.read())
    
    with open(filename, 'w') as f:
        f.write(json.dumps(data))

        
def decodeFile(filename):
    with open(filename) as f:
        data = f.read()
    return decodeString(json.loads(data))

'''
     

def encodeFile(filename, newFilename):
    with open(filename, 'r') as f:
        with open(newFilename, 'w') as nf: 
            for line in f:
                encoded = encodeString(line.strip('\n'))
                encoded_str = ''.join([f'{char}{count}' for char, count in encoded])
                nf.write(encoded_str + '\n')

def decodeFile(filename):
    decoded_lines = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                decoded_lines.append('')
                continue

            decoded = []
            i = 0
            while i < len(line):
                char = line[i]
                i += 1
                count_str = ''
                while i < len(line) and line[i].isdigit():
                    count_str += line[i]
                    i += 1
                decoded.append((char, int(count_str)))
            decoded_lines.append(decodeString(decoded))

    return "\n".join(decoded_lines)


original_path = "code_challenge/compressing_files/file.txt"
encoded_path = "code_challenge/compressing_files/new_file.txt"

print(f'Original file size: {os.path.getsize(original_path)}')
encodeFile(original_path, encoded_path)
print(f'New file size: {os.path.getsize(encoded_path)}')

decoded = decodeFile(encoded_path)
print(decoded)

#10_04_challenge_art.txt