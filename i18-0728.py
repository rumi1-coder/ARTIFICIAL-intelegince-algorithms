#Assignment_1
#sohaib_shahid_ul _haq
#18i0728
#####################################################datastructure for file data
filename='data0.txt'
table_1={}
table_2={}
table_3={}
table_4={}
table_5={}
#################################################reading data from file to memory
with open(filename) as file_object:
    for line in file_object:
        if line[0]=='1':
            if line[3]!='}' and line[4]!=',':
               score=line[6:12]
               table_1[line[3]]=float(line[6:12])
            elif line[3]!='}' and line[4]==',':
                table_1[line[3]] =float(line[8:14])
                table_1[line[5]] =float(line[8:14])
            else:
                table_1[0]=float(line[5:11])
        elif line[0]=='2':
                if line[3] != '}' and line[4] != ',':
                    table_2[line[3]] =float(line[6:12])
                elif line[3] != '}' and line[4] == ',':
                    score = line[8:14]
                    table_2[line[3]] =float(line[8:14])
                    table_2[line[5]] =float(line[8:14])
                else:
                   table_2[0]=float(line[5:11])
        elif line[0] == '3':
            if line[3]!='}' and line[4]!=',':
               table_3[line[3]]=float(line[6:12])
            elif line[3]!='}' and line[4]==',':
                score = line[8:14]
                table_3[line[3]] =float(line[8:14])
                table_3[line[5]] =float(line[8:14])
            else:
               table_3[0]=float(line[5:11])
        elif line[0]=='4':
             if line[3]!='}' and line[4]!=',':
               table_4[line[3]]=float(line[6:12])
             elif line[3]!='}' and line[4]==',':
                score = line[8:14]
                table_4[line[3]] =float(line[8:14])
                table_4[line[5]] =float(line[8:14])
             else:
                table_4[0] =float(line[5:11])
        else:
            if line[3]!='}' and line[4]!=',':
               table_5[line[3]]=float(line[6:12])
            elif line[3]!='}' and line[4]==',':
                score = line[8:14]
                table_5[line[3]] =float(line[8:14])
                table_5[line[5]] =float(line[8:14])
            else:
                table_5[0] =float(line[5:11])

############################# loaded data display
print(table_1)
print(table_2)
print(table_3)
print(table_4)
print(table_5)

stuff=[1,2,3,4,5]
minimum_cost=0
#######################################################swap function
def swap(list_v,m,n):
    t=list_v[m]
    list_v[m]=list_v[n]
    list_v[n]=t
#swap(stuff,1,2)

#######################################################cost calculator
def cost_calculator(list_v):
    cost = 0
    for i in range(0,len(list_v)):
        if list_v[i] == 1:
            minimum = 0
            for key, value in table_1.items():
                minimum = table_1[key]
                break
            for key, value in table_1.items():
                if table_1[key] < minimum:
                    minimum = table_1[key]
            #print(f'{minimum} + ')
            cost+=minimum
        elif list_v[i] == 2:
            minimum = 0
            for key, value in table_2.items():
                minimum = value
                break
            for key, value in table_2.items():
                if value < minimum:
                    minimum = value
            #print(f'{minimum} + ')
            cost += minimum
        elif list_v[i] == 3:
            minimum = 0
            for key, value in table_3.items():
                minimum = value
                break
            for key, value in table_3.items():
                if  value<minimum:
                    minimum = value
            #print(f'{minimum} + ')
            cost += minimum
        elif list_v[i] == 4:
            minimum = 0
            for key, value in table_4.items():
                minimum = value
                break
            for key, value in table_4.items():
                if minimum < value:
                    minimum = value
            #print(f'{minimum} + ')
            cost += minimum
        else:
            minimum = 0
            for key, value in table_5.items():
                minimum = value
                break
            for key, value in table_5.items():
                if minimum < value:
                    minimum = value
            #print(f'{minimum} + ')
            cost += minimum
    return cost


print(cost_calculator(stuff))

################################################graph generator
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
         else:
             self.data = data

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
    ###################################################breadth first search
   def Breadth_first_search(self):

          #print('############################')
          #print(self.data)
          visited = []
          if self:
              visited.append(self)
              print(cost_calculator(self.data))
          current = self
          counter=0
          while current:
              counter=counter+1
              print(f'step {counter}')
              if current.left:
                  #print(cost_calculator(current.left.data))
                  visited.append(current.left)
              if current.right:
                  #print(cost_calculator(current.right.data))
                  visited.append(current.right)
              visited.pop(0)
              if not visited:
                  break
              current = visited[0]

########################################################depth first search
   def dfs(self):
       mini_cost=(cost_calculator(self.data))
       counter=0
       visited=[]
       stack=[]
       if self:
           stack.append(self)
           #print(cost_calculator(self.data))
       current = self
       while stack:
               counter=counter+1
               vertex = stack.pop()
               if vertex not in visited:
                   visited.append(vertex)
                   # new nodes are added to the start of stack
                   v=self.left
                   stack =[int(''.join(str(i) for i in self.data))]
                   print(f'step {counter}')
               print(mini_cost)
               return visited




###################################################permutation generator
rroot = Node([1,2,3,4,5])
from itertools import permutations
words = [''.join(p) for p in permutations('12345')]
for i in words:
    j=list(map(int,i))
    rroot.insert(j)

rroot.PrintTree()

################################
print('Breadth first search algorithm minimum cost calculated')
rroot.Breadth_first_search()
print(minimum_cost)


################################
print('\n\n\ndepth first search algorithm minimum cost calculated')
rroot.dfs()





