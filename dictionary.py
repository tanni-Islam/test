phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}


phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print "Jake is listed in the phonebook."
if "Jill" not in phonebook:
    print "Jill is not listed in the phonebook."

'''Phonebook = {
    "john" : 0232334134,
    "jill" : 0232334156
}

del phonebook["john"]
for name, number in phonebook.iteritems():
    print "phone number of %s is %d" % (name, number)
'''
