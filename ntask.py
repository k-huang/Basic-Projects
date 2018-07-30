tasklist={'data':[100,30,'a'],'next':{'data':[101,15,'b'],'next':{'data':[102,10,'b'],'next':None}}}

def jobfinder(tasklist,ID):
    if tasklist['data'][0] == ID:
        return tasklist
    while tasklist['next']['data'][0] != ID:
        if tasklist['next'] == None:
            print('A job with that ID was not found')
            return None
        else:
            tasklist = tasklist['next']
    return tasklist
# Outside, set this equal to whatever, newnode, nodebefore, etc
# This will not modify the tasklist, however.

print(jobfinder(tasklist,102))
