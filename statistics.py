# This function tallies the number of jobs of each type in the queue and returns it
# as a dictionary
tasklist = {'data': [101, 30, 'medical'], 'next': {'data': [103, 25, 'der'], 'next': {'data': [102, 20, 'medical'], 'next': {'data': [104, 5, 'derp'], 'next': None}}}}

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

for i in {'a': 1,"b":2}:
    print(i)
