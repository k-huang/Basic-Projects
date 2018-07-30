derp = [1,2,3,4]
def infiniteloop():
    i = 0
    while i<5:
        i +=1
        return "cat"

print(infiniteloop())
