#this is practice storing variables and practicing formatting

famous_person = 'Oscar Wilde'
message = 'Be yourself; everyone else is already taken.'
print(f"{famous_person} once said {message}")

#Practicing using stripping method of white spaces also tabs and new lines

name = '  Brian  '
print(name)
print(name.lstrip())
print(name.strip())
print(f"\t{name}")
print(f"\n{name}")

#Main goal for this practice for me is to practice how syntax must be written out.

#last exercise is to practice removing suffixes. Same Principle as prefixes. 

file_name = 'python-files.txt'
print(file_name.removesuffix('.txt'))

#practing saving a new variable when a prefix or suffix of a value is changed.  

file_name = file_name.removesuffix('.txt')
print(file_name)