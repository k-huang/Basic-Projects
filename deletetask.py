# This function takes the tasklist and ID and removes a task from the list
# it then returns the updated list
def deletetask(tasklist,ID):
    nodebefore = tasklist
    if tasklist['data'][0] == ID:
        tasklist = tasklist['next']
    else:
        while nodebefore['next']['data'][0] != ID:
            nodebefore = nodebefore['next']
        nodebefore['next'] = nodebefore['next']['next']
    return tasklist
tasklist={'data':[100,30,'a'],'next':{'data':[101,15,'b'],'next':{'data':[102,10,'b'],'next':None}}}
print(deletetask(tasklist,102))
