def challenge(names):
    print("names > 4 and < 7 characters")
    for name in names :
        if len(name) > 4 and len(name) <7:
            print(name)

    print("sorted names >7 characters")
    names.sort()
    for name in names:
        if len(name) > 7:
            print(name)

    print("palindromic names")
    for name in names :
        if name == name[::-1]:
         print(name)


majina = ["reagan", "millicent", "emilly", "mark", "joseph", "maczuckerbug", "jamesbond", "abdallah", "bob"]
challenge(majina)