from collections import defaultdict

class Node:
  def __init__(self,name,par=None) :
    self.name=name
    self.par=par
  def display(self) :
    print(self.name)

data = defaultdict(list)
data['A']=['B','C','D']
data['B']=['E','F']
data['C']=['G','H']
data['D']=['I','J']
data['F']=['K','L','M']
data['H']=['N','O']

def equal(O,G):
  return O.name==G.name
def checkInArray(temp,Open) :
  for x in Open:
    if equal(x,temp):
      return True
    return False
def path(O):
  print(O.name)
  if O.par != None:
    path(O.par)
  else:
    return

def BFS(S = Node('A') , G = Node('M')) :
  Open=[]
  Closed=[]
  Open.append(S)
  while True:
    if len(Open)==0 :
      print('Tim kiem khong thanh cong')
      return
    O=Open.pop(0)
    Closed.append(O)
    if equal(O,G)==True:
      print('Tim kiem thanh cong')
      path(O)
      return
    for x in data[O.name] :
      tmp = Node(x)
      tmp.par=O
      ok1=checkInArray(tmp,Open)
      ok2=checkInArray(tmp,Closed)
      if not ok1 and not ok2:
        Open.append(tmp)

def DFS(S = Node('A') , G = Node('M')) :
  Open=[]
  Closed=[]
  Open.append(S)
  while True:
    if len(Open)==0 :
      print('Tim kiem khong thanh cong')
      return
    O=Open.pop(0)
    Closed.append(O)
    if equal(O,G)==True:
      print('Tim kiem thanh cong')
      path(O)
      return
    pos=0
    for x in data[O.name] :
      tmp = Node(x)
      tmp.par=O
      ok1=checkInArray(tmp,Open)
      ok2=checkInArray(tmp,Closed)
      if not ok1 and not ok2:
        Open.insert(pos,tmp)
        pos=pos+1;

def main():
    DFS(Node('A'), Node('F'))
    BFS(Node('A'), Node('F'))
if __name__ == "__main__":
    main()

