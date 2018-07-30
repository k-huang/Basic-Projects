# This function takes a task off the top of the list, effectively responding to
# the highest priority task. It returns the updated tasklist
def respond(tasklist):
    if tasklist == {}:
        print("No current emergencies - time for a coffee break!")
    else:
        print("Responding to job",tasklist['data']['0])
        tasklist = tasklist ['next']
    return tasklist

tasklist={'data':[100,30,'a'],'next':{'data':[101,15,'b'],'next':{'data':[102,10,'b'],'next':None}}}
print(respond(tasklist))
