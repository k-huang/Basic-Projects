# This function modifies the priority of a task by storing the data of the task in 'updatedata'
# and then updating the priority. It then deletes the old task with that ID and adds a new
# job with the data from updatadata
def modifypriority(tasklist,ID,priority):
    jobtype = jobtypefinder(tasklist,ID)
    updatedata = [ID,0,jobtype]
    updatedata[1] = int(priority)
    tasklist = deletetask(tasklist,ID)
    tasklist = addtask(tasklist,updatedata[0],updatedata[1],updatedata[2])
    return tasklist

def jobtypefinder(tasklist,ID):
    while tasklist['data'][0] != ID:
        tasklist = tasklist['next']
    return tasklist['data'][2]

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

tasklist ={'data': [101, 30, 'medical'], 'next': {'data': [102, 20, 'medical'], 'next': {'data': [103, 15, 'der'], 'next': {'data': [104, 5, 'derp'], 'next': None}}}}

print('shit' in {"shit": 6})


# WHY DOES THIS RUN INFINITELY
