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

print(whatops(['details',101,10,'medical']))
