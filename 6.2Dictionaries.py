# coding: utf-8
country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
country_codes
len(country_codes)
if country_codes:
    print('Country codes is not empty')
else:
    print('Country codes is empty')
    
clear('South Africa')
clear(country-codes)
clear(country_codes)
del country_codes['South Africa']
country_codes
country_codes['Great Britain'] = 'gb'
country_codes
country_codes['fi']
country_codes['Finland']
for country_names in country_codes.keys():
    print(country_names, end=" ")
    
for country_abbs in country_codes.values():
    print(country_abbs, end=" ")
    
for country_names in sorted(country_codes.key()):
    print(country_names, end=' ')
    
country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
for country_names in sorted(country_codes.key()):
    print(country_names, end=' ')
    
for country_names in sorted(country_codes.keys()): 
    print(country_names, end=' ')
    
student_names1 = {'Jason': 'Jay', 'Alexis': 'Al', 'Samantha': 'Sam'}
student_names2 = {'Hilda': 'Hildi', 'Beauregard': 'Jr', 'Ava': 'A'}
student_names1 == student_names2
student_names1 != student_names2
text = ('this is a sample text with several words ' \n'this is more text with some different words')
text = ('this is a sample text with several words ' \n 'this is more text with some different words')
text = ('this is a sample text with several words ' 'this is more text with some different words')
word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else: 
        word_counts[word] = 1
        
print(f'{"WORD":<12}COUNT')
for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')
    
print('\nNumber of unique words:' len(word_counts))
print('\nNumber of unique words:', len(word_counts))
get_ipython().run_line_magic('save', '6.2Dictionaries')
text = ('Roses are red Violets are blue Now can you guess How much I love you')
word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        
print(f'{"WORD":<12}COUNT')
for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')
    
country_codes = {}
country_codes.update({'Canada': 'ca'})
country_codes
country_codes.update('United States' = 'us')
country_codes.update(United States = 'us')
country_codes.update(UnitedStates = 'us')
country_codes
{number: number ** 3 for number in range(1, 6)}
