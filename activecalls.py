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
            avgpriority = str(prioritysum/howmanyjobs)
        print("There are", howmanyjobs, 'jobs in the queue. The average priority is',avgpriority + '.')

tasklist={'data':[100,30,'a'],'next':{'data':[101,15,'b'],'next':{'data':[102,0,'b'],'next':None}}}

activecalls(tasklist)
