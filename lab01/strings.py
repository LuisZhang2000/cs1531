strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for i in strings:
    sentence += str(i) + " "
sentence = sentence[:-1]
    
print(sentence)

print(' '.join(strings))
