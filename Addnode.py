# This function takes the task list and adds a new task with
# task data (number, priority, type). It returns the updated tasklist
#OG
# tasklist={'data':[100,30,'a'],'next':{'data':[101,15,'b'],'next':None}}
tasklist = {'data': [101, 30, 'medical'], 'next': None}
def addtask(tasklist,tasknum,priority,tasktype):
    newnode = {}
    newnode['data'] = [tasknum,priority,tasktype]
    nodebefore = tasklist
    if tasklist == {}:
        newnode['next'] = None
        tasklist = newnode
        return tasklist
    else:
        while nodebefore['next'] != None:
            # If newest is higher priority than first
            if newnode['data'][1] > nodebefore['data'][1]:
                newnode['next'] = tasklist
                return newnode
            # If newest is lower or equal than next, point to next
            elif newnode['data'][1] <= nodebefore['next']['data'][1]:
                nodebefore = nodebefore['next']
            # If newest is greater than next, but less than or equal to current
            else:
                newnode['next'] = nodebefore['next']
                nodebefore['next'] = newnode
                return tasklist
        # If pointing at last element, this means it was less than or equal to last element
        # So it becomes the last element
        newnode['next'] = None
        nodebefore['next'] = newnode
        return tasklist


tasklist = addtask(tasklist,102,20,'medical')
print(tasklist)

# Outside, write something like
# tasklist = addfunction or w.e
