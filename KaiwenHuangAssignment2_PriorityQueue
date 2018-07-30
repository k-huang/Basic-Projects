
# Sorting by priority:
# Take each task, iterate through, move through until current task priority
# is greater than iteration task priority.
# Then, insert this task at that index.
# Insert by priority instead of sorting.

from time import sleep
# This line calls the main function to initiate the program
# dispatch()

# This is the main function, that takes a text file with commands and executes
# the dispatch functions.
def dispatch():
    tasklist = {}
    tasks = open("emergencies.txt",'r')
    for line in tasks:
        # STORE PRIORITY AS INT
        job = line.split()
        ops = whatops(job)
        # This adds a task
        if ops == 1:
            tasklist = addtask(tasklist,int(job[1]),int(job[2]),job[3])
            print("Job",job[1],'has been added.')
        # This responds to a job
        elif ops == 2:
            tasklist = respond(tasklist)
        # This prints the number of jobs in the queue and the average priority
        elif ops == 3:
            activecalls(tasklist)
        # # This modifies the priority of a job
        elif ops == 4:
            tasklist = modifypriority(tasklist,int(job[1]),int(job[2]))
            print('Job',job[1] + "'s priority has been modified to",job[2] + '.')
        # This removes a job from the list by ID
        elif ops == 5:
            tasklist = deletetask(tasklist,int(job[1]))
            print("Job",job[1],"has been removed.")
        # This prints the details for a specific job
        elif ops == 6:
            jobdata = finddetails(tasklist,int(job[1]))
            print("Job", str(jobdata[0]),'is of type "' + jobdata[2] + '" and has a priority of', str(jobdata[1]) + ".")
        # # This prints the number of types of each job
        elif ops == 7:
            stats = statistics(tasklist)
            for type in stats:
                if stats[type] == 1:
                    print("There is",stats[type],'job of the type "' + type +'".')
                else:
                    print("There are",stats[type],'jobs of the type "' + type +'".')
        sleep(0.5)


# This function translates each command into numbers indicating the type of
# operations that need to be performed. It returns these numbers
def whatops(jobs):
    if 'received' in jobs:
        return 1
    elif 'respond' in jobs:
        return 2
    elif 'show' in jobs:
        return 3
    elif 'modify' in jobs:
        return 4
    elif 'remove' in jobs:
        return 5
    elif 'details' in jobs:
        return 6
    elif 'statistics' in jobs:
        return 7
# This function adds a task to the task list and returns the updated tasklist
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

# This function finds a job by ID and returns the data in that job
def finddetails(tasklist,ID):
    while tasklist['data'][0] != ID:
        tasklist = tasklist['next']
    return tasklist['data']

# This function finds the type of a job by it's ID then returns that ID
def jobtypefinder(tasklist,ID):
    while tasklist['data'][0] != ID:
        tasklist = tasklist['next']
    return tasklist['data'][2]

# This function takes a task off the top of the list, effectively responding to
# the highest priority task. It returns the updated tasklist.
def respond(tasklist):
    if tasklist == {}:
        print("No current emergencies - time for a coffee break!")
    else:
        print("Responding to job",tasklist['data'][0])
        tasklist = tasklist ['next']
    return tasklist

# This function takes the tasklist and prints the number of jobs in queue
# and the average priority
def activecalls(tasklist):
    howmanyjobs = 0
    prioritysum = 0
    if tasklist == {}:
        print("There are no jobs in the queue.")
    else:
        while tasklist != None:
            howmanyjobs += 1
            prioritysum += tasklist['data'][1]
            tasklist = tasklist['next']
            avgpriority = round(prioritysum/howmanyjobs,1)
        if howmanyjobs == 1:
            print("There is", howmanyjobs, 'job in the queue. The average priority is',str(avgpriority) + '.')
        else:
            print("There are", howmanyjobs, 'jobs in the queue. The average priority is',str(avgpriority) + '.')

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

# This function tallies the number of jobs of each type in the queue and returns it
# as a dictionary
def statistics(tasklist):
    jobtypes = {}
    while tasklist != None:
        type = tasklist['data'][2]
        if type in jobtypes:
            jobtypes[type] += 1
        else:
            jobtypes[type] = 1
        tasklist = tasklist['next']
    return jobtypes

#This line initiates the main function and starts the program.
dispatch()
