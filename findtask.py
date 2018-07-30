tasklist = {'data': [101, 30, 'medical'], 'next': {'data': [103, 25, 'der'], 'next': {'data': [102, 20, 'medical'], 'next': {'data': [104, 5, 'derp'], 'next': None}}}}

def finddetails(tasklist,ID):
    while tasklist['data'][0] != ID:
        tasklist = tasklist['next']
    return tasklist['data']
jobdata = finddetails(tasklist,104)
print('Job', str(jobdata[0]),'is of type "', jobdata[2],'"and has a priority of', str(jobdata[1]) + ".")
