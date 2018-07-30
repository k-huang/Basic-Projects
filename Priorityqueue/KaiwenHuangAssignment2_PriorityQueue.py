# This is Assignment 2 for CISC121, written by Kaiwen Huang

# This program simulates a police dispatch. It stores jobs in a linked list by
# priority and can add, delete, respond to, or modify jobs.
# It can also print details of a job and statistics about the jobs currently in queue.


# I used the sleep function to introduce a 0.5 second delay between the
# outputs of each command, for better readability.
from time import sleep

# This is the main function, that takes a text file with commands and executes
# the dispatch functions. It assumes the textfile is named "emergencies.txt"
# and is in the same directory as this .py file
def dispatch():
    print("Welcome to the police dispatch program.")
    sleep(0.5)
    print("")
    tasklist = {}
    tasks = open("emergencies.txt",'r')
    for line in tasks:
        job = line.split()
        ops = whatops(job)
        # This adds a task
        if ops == 1:
            tasklist = addtask(tasklist,int(job[1]),int(job[2]),job[3])
            print("Adding job",job[1],'to the queue. It has a priority of',job[2],'and is of the type "' + str(job[3])+ '".')
        # This responds to a job
        elif ops == 2:
            tasklist = respond(tasklist)
        # This prints the number of jobs in the queue and the average priority
        elif ops == 3:
            if tasklist == None:
                print("There are no jobs in the queue.")
                tasklist = {}
            else:
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
            if tasklist == None or tasklist == {}:
                print("There are no jobs in queue, of any type.")
                tasklist == {}
            else:
                stats = statistics(tasklist)
                for type in stats:
                    if stats[type] == 1:
                        print("There is",stats[type],'job of the type "' + type +'".')
                    else:
                        print("There are",stats[type],'jobs of the type "' + type +'".')
        sleep(0.5)
        print('')
    # This leaves the python window open after the program finishes running
    # if the output needs to be looked at in detail.
    input('The program has finished. Press enter to exit.')


# This function takes the list of words from each line of the
# text file and translates each command into numbers indicating the type of
# operations that need to be performed. It returns these numbers.
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
# It takes the tasklist, task ID, priority, and tasktype
def addtask(tasklist,ID,priority,tasktype):
    newnode = {}
    newnode['data'] = [ID,priority,tasktype]
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
# It takes the tasklist and an ID
def finddetails(tasklist,ID):
    while tasklist['data'][0] != ID:
        tasklist = tasklist['next']
    return tasklist['data']

# This function finds the type of a job by it's ID then returns that ID
# It takes the tasklist and an ID
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
        print("Responding to job",str(tasklist['data'][0])+'.')
        tasklist = tasklist ['next']
    return tasklist

# This function takes the tasklist and prints the number of jobs in queue
# and the average priority. It does not return any value.
def activecalls(tasklist):
    howmanyjobs = 0
    prioritysum = 0
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

# This function takes the tasklist and tallies the number of jobs of each
# type in the queue and returns it as a dictionary.
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
