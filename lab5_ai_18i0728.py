from queue import PriorityQueue

# Define the Puzzle class
class Puzzle:
    # Define the goal state
    goal_state=[1,2,3,8,0,4,7,6,5]
    # Initialize the class variables
    heuristic=None
    evaluation_function=None
    needs_hueristic=False
    num_of_instances=0
    
    # Define the constructor
    def __init__(self,state,parent,action,path_cost,needs_hueristic=False):
        self.parent=parent
        self.state=state
        self.action=action
        # Calculate the path cost
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost
        # Calculate the heuristic value if needed
        if needs_hueristic:
            self.needs_hueristic=True
            self.generate_heuristic()
            self.evaluation_function=self.heuristic+self.path_cost
        # Increment the number of instances
        Puzzle.num_of_instances+=1
    
    # Define the string representation of the object
    def __str__(self):
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])
    
    # Define the heuristic function
    def generate_heuristic(self):
        self.heuristic=0
        for num in range(1,9):
            # Calculate the manhattan distance between the current state and the goal state
            distance=abs(self.state.index(num) - self.goal_state.index(num))
            i=int(distance/3)
            j=int(distance%3)
            self.heuristic=self.heuristic+i+j
    
    # Define the goal test function
    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False
    
    # Define a static method to find the legal actions from a given position
    @staticmethod
    def find_legal_actions(i,j):
        legal_action = ['U', 'D', 'L', 'R']
        if i == 0:  # up is disable
            legal_action.remove('U')
        elif i == 2:  # down is disable
            legal_action.remove('D')
        if j == 0:
            legal_action.remove('L')
        elif j == 2:
            legal_action.remove('R')
        return legal_action
    
    # Define the function to generate the child nodes
    def generate_child(self):
        children=[]
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        legal_actions=self.find_legal_actions(i,j)
        
        # Generate the child nodes based on the legal actions
        for action in legal_actions:
            new_state = self.state.copy()
            if action == 'U':
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]
            elif action == 'D':
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]
            elif action == 'L':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif action == 'R':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            # Append the child node to the list
            children.append(Puzzle(new_state,self,action,1,self.needs_hueristic))
        return children

    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution


# Define the A* search algorithm function
def Astar_search(initial_state):
    # Initialize variables
    count=0
    explored=[]
    start_node=Puzzle(initial_state,None,None,0,True)
    q = PriorityQueue()
    # Add the start node to the priority queue with its evaluation function value as priority
    q.put((start_node.evaluation_function,count,start_node))

    # While there are nodes in the queue
    while not q.empty():
        # Get the node with the highest priority
        node=q.get()
        # Extract the node object from the tuple
        node=node[2]
        # Add the node's state to the list of explored states
        explored.append(node.state)
        # If the goal state is found, return the path to reach it
        if node.goal_test():
            return node.find_solution()

        # Generate child nodes and add them to the priority queue
        children=node.generate_child()
        for child in children:
            if child.state not in explored:
                # Increment the node count and add the child node to the priority queue
                count += 1
                q.put((child.evaluation_function,count,child))
    return

# Import the time module to measure execution time
from time import time

# Define initial states for the puzzle
state=[[1, 3, 4,
        8, 6, 2,
        7, 0, 5],

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [2, 8, 1,
        4, 6, 3,
        0, 7, 5]]

# Loop through the initial states
for i in range(0,1):
    # Reset the number of instances of Puzzle objects
    Puzzle.num_of_instances = 0
    # Get the start time
    t0 = time()
    # Run the A* search algorithm on the initial state
    astar = Astar_search(state[0])
    # Get the execution time
    t1 = time() - t0
    # Print the results
    print('A*:',astar)
    print('space:', Puzzle.num_of_instances)
    print('time:', t1)
    print()