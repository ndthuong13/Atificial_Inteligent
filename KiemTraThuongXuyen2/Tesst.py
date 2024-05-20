from collections import defaultdict
class node:
    def __init__(self, name, par=None):
        self.name = name
        self.par = par
    def display(self):
        print(self.name)

data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['M', 'N']
data['C'] = ['L']
data['D'] = ['O', 'P']
data['M'] = ['X', 'Y']
data['N'] = ['U', 'V']
data['O'] = ['I', 'J']
data['Y'] = ['R', 'S']
data['V'] = ['G', 'H']

def equal(R):
    return R.name
def checkInArray(temp, open):
    for x in open:
        if equal(x, temp):
            return True
        return False
def path(R):
    print(R.name)
    if R.par != None:
        path(R.par)
    else:
        return
