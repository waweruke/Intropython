#1 Tuples
cars = ("bmw","r34","skyline","supra","gtr")
print(cars)

print(cars[2])
print(cars[1:4])

for gari in cars:
    print(gari)

#2. Lists
colors = ["red","green","purple","blue","gray","black"]
print(colors)
print(colors[2])
colors[3] = "navy blue"
print(colors[1:4])

for rangi in colors:
    print(rangi)
#reverse
    colors.reverse()
    print(colors)
#delete
    colors.pop(0)
    print(colors)
#sort
colors.sort()
print(colors)

#3 . Dictionaries
students = {"adm1": "tracy","adm2": "moses","adm3": "eugene"}
print(students["adm1"])

for funguo in students.keys():
    print(funguo)

    for jina in students.values():
        print(jina)

#4 . sets
ranks = {1,5,8,4,0,5,3,2,1,6,8,10,11,12,10}
print(ranks)



sports = ["basketball","soccer","tennis","golf","tabletennis"]
generatedlist = []
for n in sports:
    if len(n) > 5:
        generatedlist.append(n)

        for x in generatedlist:
            print(x)