'''
sentence = "Once upon a time there was a little girl name Tanni"

word = sentence.split()
length = []

for i in word:
    length.append(len(i))

print length

'''

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int (x) for x in numbers if x > 0]

print newlist
