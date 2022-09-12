# coding: utf-8
colors = {'red', 'orange', 'yello', 'green', 'red', 'blue'}
colros
colros
colors
len(colors)
'red' in colors
for color in colors:
    print(color.upper(), end=' ')
    
numbers = list(range(10)) + list(range(5))
numbers
set(numbers)
text = ('Roses are red Violets are blue Now can you guess How much I love you')
unique_words = set(text.split())
for word in sorted(unique_words):
    print(word, end=' ')
    
set('abc def ghi jkl mno').issuperset('hi mom')
{10, 20, 30} - {5, 10, 15, 20}
{10, 20, 30} ^ {5, 10, 15, 20}
{10, 20, 30} | {5, 10, 15, 20}
{10, 20, 30} & {5, 10, 15, 20}
country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
country_codes.clear()
country_codes
numbers.clear()
numbers
numbers = [1, 2, 3, 2, 4, 5, 6, 6, 7, 8, 9, 10, 10]
evens = {item for item in numbers if item % 2 == 0}
evens
