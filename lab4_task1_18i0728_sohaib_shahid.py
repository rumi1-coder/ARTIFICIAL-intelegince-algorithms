import random
goal_state=[]
puzzle_board=[]

def depth_search_algo():
  i=0
  for v in puzzle_board:
    if v==0:
      i=puzzle_board.index(v)
      break
  if i==0:
      check1=i+1
      check2=i+3
      if puzzle_board[check1]!=goal_state[check1]
          

  elif i==1:
      check1=i-1
      check2=i+1
      check3=i+3
  elif i==2:
      check1=i-1
      check2=i+3
  elif i==3:
      check1=i-3
      check2=i+1
      check3=i+3
  elif i==4:
      check1=i=3
      check2=i-1
      check3=i+1
      check4=i+3
  elif i==5:
      check1=i-3
      check2=i-1
      check3=i+3
  elif i==6:
      check1=i+3
      check2=i+1
  elif i==7:
      check1=i-1
      check2=i-3
      check3=i+1
  else:
      check1=i-1
      check2=i-3







def printer1():
    str=''
    for i in goal_state:
        str+=(f'{i} ')
        if i%3==0:
          str+='\n'
    print(str)
def printer2():
    str=''
    counter=0
    for i in puzzle_board:
        counter+=1
        str += (f'{i} ')
        if counter%3==0:
           str+='\n'


    print(str)
def main():
  print('8 Puzzle problem')
  for i in range(1,10):
      if i==9:
        goal_state.append(0)
      else:
        goal_state.append(i)
  printer1()

  for i in range(0,9):
      puzzle_board.append(i)
      random.shuffle(puzzle_board)
  printer2()
  depth_search_algo()




main()
