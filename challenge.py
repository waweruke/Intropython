students = ["reagan", "millicent", "emilly", "mark", "joseph", "maczuckerbug", "jamesbond", "abdallah", "bob","hannah"]
requestedlist = []
for s in students:
    if len(s) > 4 and len(s) < 7 :
        requestedlist.append(s)

        for s in requestedlist:
            print(s)


students.sort()
for n in students:
    if len(n) > 7:

            print(n)

def is_palindrome(word):
    word = word.replace("", "").lower()
    return word == word[::-1]
names = ["reagan", "millicent", "emilly", "mark", "joseph", "maczuckerbug", "jamesbond", "abdallah", "bob","hannah"]

for name in names:
    if is_palindrome(name):
        print(name)
