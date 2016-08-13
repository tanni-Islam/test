import re

item = []

for i in dir(re):
    if "find" in i:
        item.append(i)


print sorted(item)
