import pygame
from copy import deepcopy
pygame.font.init()
run=True
clock = pygame.time.Clock()
sudoku=[
        ["7", '8', '.', '4', '.', '.', '1', '2', '.'],
        ['6', '.', '.', '.', '7', '5', '.', '.', '9'],
        ['.', '.', '.', '6', '.', '1', '.', '7', '8'],
        ['.', '.', '7', '.', '4', '.', '2', '6', '.'],
        ['.', '.', '1', '.', '5', '.', '9', '3', '.'],
        ['9', '.', '4', '.', '6', '.', '.', '.', '5'],
        ['.', '7', '.', '3', '.', '.', '.', '1', '2'],
        ['1', '2', '.', '.', '.', '7', '4', '.', '.'],
        ['.', '4', '9', '2', '.', '6', '.', '.', '7']
    ]
temp=deepcopy(sudoku)

def draw_board(screen,x,y):
  for i in range(0,450,50):
    for j in range(0,450,50):
      pygame.draw.rect(screen, (240,240,240), [x+i,y+j,50,50])
      font = pygame.font.SysFont('Calibri', 50)
      if sudoku[j//50][i//50]!=".":
        text = font.render(sudoku[j//50][i//50], 1, (0,0,0))
        screen.blit(text, [x+i+10,y+j+10])
      elif temp[j//50][i//50]!=".":
        font = pygame.font.SysFont('Calibri', 50)
        text = font.render(temp[j//50][i//50], 1, (200,200,0))
        screen.blit(text, [x+i+10,y+j+10])

      
  thick=2
  for i in range(0,451,50):
    if i%3==0:
      thick=5
    pygame.draw.line(screen, (0,0,0), [x+i,y+0], [x+i,y+450],thick)
    thick=2
  thick=3
  for j in range(0,451,50):
    if j%3==0:
      thick=5
    pygame.draw.line(screen, (0,0,0), [x+0,y+j], [x+450,y+j],thick)
    thick=3

def check_valid_pos(pos,key):
  pygame.draw.rect(screen, (0,255,0), [(pos[0]//50)*50,50*(pos[1]//50),50,50], 5)
  x=pos[0]-50
  y=pos[1]-50
  if key==".":
    temp[y//50][x//50]=key
  elif key!=None:
    temp[y//50][x//50]=str(key)
    
def isvalid():
        b=deepcopy(temp)
        row={0:set(b[0]),1:set(b[1]),2:set(b[2]),
             3:set(b[3]),4:set(b[4]),5:set(b[5]),
             6:set(b[6]),7:set(b[7]),8:set(b[8])}
        col={0:set(),1:set(),2:set(),
            3:set(),4:set(),5:set(),
            6:set(),7:set(),8:set()}
        box={(0,0):set(),(0,1):set(),(0,2):set(),
             (1,0):set(),(1,1):set(),(1,2):set(),
             (2,0):set(),(2,1):set(),(2,2):set()}
        for i in range(9):
            for j in range(9):
                col[i].add(b[j][i])
                box[(i//3,j//3)].add(b[i][j])
        
        def find(b):
          for i in range(9):
              for j in range(9):
                  if b[i][j]==".":
                      return i,j
          return -1,-1

        def check(b,i,j,num,row,col,box):
          if str(num) in row[i]:
              return False
          if str(num) in col[j]:
              return False
          if str(num) in box[(i//3,j//3)]:
              return False
          return True
        
        def solve(b,row,col,box):
          r,c=find(b)
          if r!=-1:
              for i in range(1,10):
                  if check(b,r,c,i,row,col,box):
                      b[r][c]=str(i)
                      row[r].add(str(i))
                      col[c].add(str(i))
                      box[(r//3,c//3)].add(str(i))
                      if solve(b,row,col,box):
                          return True
                      b[r][c]='.'
                      row[r].remove(str(i))
                      col[c].remove(str(i))
                      box[(r//3,c//3)].remove(str(i))
              return False
          else:
              return True
        
        
        
        return solve(b,row,col,box)



def solve_gui():
        b=sudoku
        row={0:set(b[0]),1:set(b[1]),2:set(b[2]),
             3:set(b[3]),4:set(b[4]),5:set(b[5]),
             6:set(b[6]),7:set(b[7]),8:set(b[8])}
        col={0:set(),1:set(),2:set(),
            3:set(),4:set(),5:set(),
            6:set(),7:set(),8:set()}
        box={(0,0):set(),(0,1):set(),(0,2):set(),
             (1,0):set(),(1,1):set(),(1,2):set(),
             (2,0):set(),(2,1):set(),(2,2):set()}
        for i in range(9):
            for j in range(9):
                col[i].add(b[j][i])
                box[(i//3,j//3)].add(b[i][j])
        
        def find(b):
          for i in range(9):
              for j in range(9):
                  if b[i][j]==".":
                      return i,j
          return -1,-1

        def check(b,i,j,num,row,col,box):
          if str(num) in row[i]:
              return False
          if str(num) in col[j]:
              return False
          if str(num) in box[(i//3,j//3)]:
              return False
          return True
        
        def solve(b,row,col,box):
          r,c=find(b)
          if r!=-1:
              for i in range(1,10):
                  if check(b,r,c,i,row,col,box):
                      b[r][c]=str(i)
                      row[r].add(str(i))
                      col[c].add(str(i))
                      box[(r//3,c//3)].add(str(i))
                      draw_board(screen,50,50)
                      pygame.display.update()
                      if solve(b,row,col,box):
                          return True
                      b[r][c]='.'
                      row[r].remove(str(i))
                      col[c].remove(str(i))
                      box[(r//3,c//3)].remove(str(i))
                      draw_board(screen,50,50)
                      pygame.display.update()

              return False
          else:
              return True
        
        
        
        return solve(b,row,col,box)
  

def is_empty(b):
  for i in range(9):
    for j in range(9):
      if b[i][j]==".":
        return False
  return True

def if_correct(b):

  def fil(n):
    try:
      if int(n):
        return True
    except:
      return False
  
  for i in range(9):
    l=[]
    l=list(map(int,(filter(fil,b[i]))))
    if len(l)!=len(set(l)):
      return False
  
  for i in range(9):
    l=[]
    for j in range(9):
      if b[j][i]!=".":
        l.append(int(b[j][i]))
    if len(l)!=len(set(l)):
      return False
 
  
  for i in range(3):
    for j in range(3):
      l=[]
      for p in range(i*3,(i*3)+3):
        for q in range(j*3,(j*3)+3):
          try:
            l.append(int(b[p][q]))
          except:
            pass
      if len(l)!=len(set(l)):
        return False   
  return True






temp_state=False
key=None
pos=0
time=0
fail_time=0
passed_time=1
fail_pass=1
flag=False
while run:
  screen=pygame.display.set_mode((800,600))
  screen.fill((255,255,255))
  draw_board(screen,50,50)
  
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      key=None
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          key = 1
          check_valid_pos(pos,key)
        if event.key == pygame.K_2:
          key = 2
          check_valid_pos(pos,key)
        if event.key == pygame.K_3:
          key = 3
          check_valid_pos(pos,key)
        if event.key == pygame.K_4:
          key = 4
          check_valid_pos(pos,key)
        if event.key == pygame.K_5:
          key = 5
          check_valid_pos(pos,key)
        if event.key == pygame.K_6:
          key = 6
          check_valid_pos(pos,key)
        if event.key == pygame.K_7:
          key = 7
          check_valid_pos(pos,key)
        if event.key == pygame.K_8:
          key = 8
          check_valid_pos(pos,key)
        if event.key==pygame.K_9:
          key=9  
          check_valid_pos(pos,key)    
        if event.key == pygame.K_DELETE:
          key="."
          check_valid_pos(pos,key)
        if event.key==pygame.K_RETURN:
          if if_correct(deepcopy(temp)) and isvalid():
            if is_empty(temp):
              flag=True
            sudoku=deepcopy(temp)
            if not flag:
              time = 10000
              passed_time = clock.tick(60)
          else:
            temp=deepcopy(sudoku)
            fail_time=10000
            fail_pass=clock.tick(60)
        if event.key == pygame.K_SPACE:
          temp=sudoku
          if solve_gui():
            flag=True

      if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        temp_state=True
        ##check button same as enter
        if 600<=pos[0]<=600+150 and 150<=pos[1]<=150+50:
          if if_correct(deepcopy(temp)) and isvalid():
            if is_empty(temp):
              flag=True
            sudoku=deepcopy(temp)
            if not flag:
              time = 10000
              passed_time = clock.tick(60)
          else:
            temp=deepcopy(sudoku)
            fail_time=10000
            fail_pass=clock.tick(60)

        ##reset button
        elif 620<=pos[0]<=620+100 and 260<=pos[1]<=260+30:
          sudoku=[["5","3",".",".","7",".",".",".","."],
                  ["6",".",".","1","9","5",".",".","."],
                  [".","9","8",".",".",".",".","6","."],
                  ["8",".",".",".","6",".",".",".","3"],
                  ["4",".",".","8",".","3",".",".","1"],
                  ["7",".",".",".","2",".",".",".","6"],
                  [".","6",".",".",".",".","2","8","."],
                  [".",".",".","4","1","9",".",".","5"],
                  [".",".",".",".","8",".",".","7","9"]]
          temp=deepcopy(sudoku)
          temp_state=False
          key=None
          pos=0
          time=0
          fail_time=0
          passed_time=1
          fail_pass=1
          flag=False


        ##solve button same as space
        elif 600<=pos[0]<=600+150 and 350<=pos[1]<=350+50:
          temp=sudoku
          if solve_gui():
            flag=True


          
      
        
  draw_board(screen,50,50)
  
  ##buttons
  pygame.draw.rect(screen,(200,200,200), [600,150,150,50])
  font = pygame.font.SysFont('Calibri', 50)
  text = font.render("Check", 1, (0,0,0))
  screen.blit(text, [620,155])

  pygame.draw.rect(screen,(200,200,200), [620,260,100,30])
  font = pygame.font.SysFont('Calibri', 30)
  text = font.render("reset", 1, (0,0,0))
  screen.blit(text, [635,260])

  pygame.draw.rect(screen,(200,200,200), [600,350,150,50])
  font = pygame.font.SysFont('Calibri', 50)
  text = font.render("Solve", 1, (0,0,0))
  screen.blit(text, [630,355])


  if temp_state:
    x=pos[0]-50
    y=pos[1]-50
    try:
      if y//50>=0 and x//50>=0 and sudoku[y//50][x//50]==".":
        check_valid_pos(pos,key)
    except:
      pass
  
  time -= passed_time
  if time >= 0:
    font = pygame.font.SysFont('Calibri', 50)
    text = font.render("CORRECT", 1, (0,255,0))
    screen.blit(text, [200,530])
  
  fail_time -= fail_pass
  if fail_time >= 0:
    font = pygame.font.SysFont('Calibri', 50)
    text = font.render("WRONG", 1, (255,0,0))
    screen.blit(text, [200,530])
  if flag:
    font = pygame.font.SysFont('Calibri', 50)
    text = font.render("SUCCESS", 1, (0,255,0))
    screen.blit(text, [200,530])


  font = pygame.font.SysFont('comicsansms', 20)
  text = font.render("by", 1, (0,0,255))
  screen.blit(text, [700,530])
  text = font.render("Aditya Vardhan", 1, (0,0,255))
  screen.blit(text, [650,550])

  
  pygame.display.update()