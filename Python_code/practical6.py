import re
# findall, search, split, sub, finditer
s = 'KBCNMU: A university department of computer science.'

match = re.search(r'.', s)
print(match)
 
# using \
match = re.search(r'\.', s)
print(match)

#extracting numbers from string

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'


result = re.findall(pattern, string) 
print(result)

patt = re.compile(r'\d{5}-\d{4}')
matches = patt.finditer(string)
for match in matches:
    print(match)

    
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string) 
print(new_string)
