# write your code here
import random
winning_pos=[((0,0),(0,1),(0,2)),
             ((1,0),(1,1),(1,2)),
             ((2,0),(2,1),(2,2)),
             ((0,0),(1,0),(2,0)),
             ((0,1),(1,1),(2,1)),
             ((0,2),(1,2),(2,2)),
             ((0,0),(1,1),(2,2)),
             ((0,2),(1,1),(2,0)),
             ]

def ttprint(cell_list):
    print('---------')
    for l in cell_list:
        print('|',' '.join(l),'|')
    print('---------')

def judge(cell_list):
    empty_flag=False

    for cl in cell_list:
        if cl.count('X')==3:
            print('X wins')
            return True
        elif cl.count('O')==3:
            print('O wins')
            return True
        elif ' ' in cl:
            empty_flag=True
    diag1=[cell_list[0][0], cell_list[1][1],cell_list[2][2]]
    diag2=[cell_list[2][0], cell_list[1][1],cell_list[0][2]]
    if diag1.count('X')==3 or diag2.count('X')==3 :
        print('X wins')
        return True
    if diag1.count('O')==3 or diag2.count('O')==3 :
        print('O wins')
        return True
    col1=[cell_list[0][0], cell_list[1][0],cell_list[2][0]]
    col2=[cell_list[0][1], cell_list[1][1],cell_list[2][1]]
    col3=[cell_list[0][2], cell_list[1][2],cell_list[2][2]]
    if col1.count('X')==3 or col2.count('X')==3 or col3.count('X')==3:
        print('X wins')
        return True
    if col1.count('O')==3 or col2.count('O')==3 or col3.count('O')==3:
        print('O wins')
        return True
    if empty_flag:
        # print('Game not finished')
        return False
    else:
         print('Draw')
         return True
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

def make_bestMove(cell_list,mark):
    bestScore=-1000
    bestMove=None
    empty=[(i,j) for i,v in enumerate(cell_list)
           for j,s in enumerate(v) if s==' ']
    for availableSpot in empty:
        cell_list[availableSpot[0]]=replace_str_index(cell_list[availableSpot[0]],availableSpot[1],mark)
        score=Minimax(cell_list,0,mark,False)
        cell_list[availableSpot[0]]=replace_str_index(cell_list[availableSpot[0]],availableSpot[1],' ')
        if score>bestScore:
            bestScore=score
            bestMove=availableSpot
    cell_list[bestMove[0]]=replace_str_index(cell_list[bestMove[0]],bestMove[1],mark)

def evaluate(cell_list,depth,mark):
    str_win=[''.join([cell_list[loc[0]][loc[1]] for loc in pairs]) for pairs in winning_pos ]
    win_mark = 'X'*3 if mark=='X' else 'OOO'
    win_mark_human = 'X'*3 if mark=='O' else 'OOO'

    if win_mark in str_win:
        return 10-depth
    elif win_mark_human in str_win:
        return depth-10
    elif any([' ' in win for win in str_win]):
        return None # not done
    else:
        return 0

def Minimax(cell_list,depth,mark,isMaximizer):
    score = evaluate(cell_list,depth,mark)
    if score is not None:
        return score

    other_mark='O' if mark=='X' else 'X'
    empty=[(i,j) for i,v in enumerate(cell_list)
           for j,s in enumerate(v) if s==' ']
    if isMaximizer:
        bestScore=-1000
        for availablespot in empty:
            cell_list[availablespot[0]]=replace_str_index(cell_list[availablespot[0]],availablespot[1],mark)
            score=Minimax(cell_list,depth+1,other_mark,not isMaximizer)
            cell_list[availablespot[0]]=replace_str_index(cell_list[availablespot[0]],availablespot[1],' ')
            bestScore=max(score, bestScore)
        return bestScore

    if not isMaximizer:
        bestScore= 1000
        for availablespot in empty:
            cell_list[availablespot[0]]=replace_str_index(cell_list[availablespot[0]],availablespot[1],other_mark)
            score=Minimax(cell_list,depth+1,mark,not isMaximizer)
            cell_list[availablespot[0]]=replace_str_index(cell_list[availablespot[0]],availablespot[1],' ')
            bestScore=min(score, bestScore)
        return bestScore

def robot_medium_AI(cell_list,mark):
    for pairs in winning_pos:
        count=0
        for loc in pairs:
            if cell_list[loc[0]][loc[1]]==mark:
                count+=1
            elif cell_list[loc[0]][loc[1]]==' ':
                next_Move=loc
            else:
                next_Move=[]
        if count==2 and next_Move:
            cell_list[next_Move[0]]=cell_list[next_Move[0]][:next_Move[1]]\
                                    + mark+ cell_list[next_Move[0]][next_Move[1]+1:]
            return

    other_mark='O' if mark=='X' else 'X'
    for pairs in winning_pos:
        count=0
        for loc in pairs:
            if cell_list[loc[0]][loc[1]]==other_mark:
                count+=1
            elif cell_list[loc[0]][loc[1]]==' ':
                next_Move=loc
        if count==2 and next_Move:
            cell_list[next_Move[0]]=cell_list[next_Move[0]][:next_Move[1]]\
                                    + mark+ cell_list[next_Move[0]][next_Move[1]+1:]
            return

    robot(cell_list,mark)

def robot(cell_list,mark):
    while True:
        row=random.randint(0,2)
        col=random.randint(0,2)
        if cell_list[row][col]==' ':
            break
    cell_list[row]=cell_list[row][:col]+ mark+ cell_list[row][col+1:]

    # return cell_list
def human(cell_list,mark):
    ipt = input('Enter the coordinates: ')
    cood=ipt.split()
    if len(cood)<2 or any([not c.isnumeric() for c in cood]):
        print('You should enter numbers!')
        return False
    col = int(cood[0])-1
    row = 3-int(cood[1])
    if col>2 or row<0:
        print('Coordinates should be from 1 to 3!')
        return False
    if cell_list[row][col] in ['X','O']:
        print('This cell is occupied! Choose another one!')
        return False
    else:
        cell_list[row]=cell_list[row][:col]+ mark+ cell_list[row][col+1:]
        return True

# construct an cell_list of 3 blank strings
cell_list=['   ' for x  in range(3)]
row_count=-1

while True:
    cmd = input('Input command: ')
    cmds=cmd.split()
    if cmd=='exit':
        break
    elif len(cmds)==3 and cmds[1] in ['easy','medium','hard','user'] and cmds[2] in ['easy','hard','medium','user']:
        cell_list=['   ' for x  in range(3)]
        ttprint(cell_list)
        # machine vs machine
        if cmds[1]=='easy' and cmds[2]=='easy':
            while True:
                robot(cell_list,'X')
                ttprint(cell_list)
                game_end=judge(cell_list)
                if game_end:
                    break
                else:
                    print('Making move level "easy"')
                    robot(cell_list,'O')
                    game_end=judge(cell_list)
                    ttprint(cell_list)
                    if game_end:
                        break
                    else:
                        print('Making move level "easy"')
        #human vs human
        if cmds[1]=='user' and cmds[2]=='user':
            while True:
                human(cell_list,'X')
                ttprint(cell_list)
                game_end=judge(cell_list)
                if game_end:
                    break
                else:
                    human(cell_list,'O')
                    game_end=judge(cell_list)
                    ttprint(cell_list)
                    if game_end:
                        break
        if cmds[1]=='user' and cmds[2]=='easy':
            while True:
                human(cell_list,'X')
                ttprint(cell_list)
                game_end=judge(cell_list)
                if game_end:
                    break
                else:
                    robot(cell_list,'O')
                    game_end=judge(cell_list)
                    ttprint(cell_list)
                    if game_end:
                        break
                    else:
                        print('Making move level "easy"')
        if cmds[1]=='easy' and cmds[2]=='user':
            while True:
                robot(cell_list,'X')
                ttprint(cell_list)
                game_end=judge(cell_list)
                if game_end:
                    break
                else:
                    print('Making move level "easy"')
                    human(cell_list,'O')
                    game_end=judge(cell_list)
                    ttprint(cell_list)
                    if game_end:
                        break
 # user with medium AI
        if cmds[1]=='user' and cmds[2]=='medium':
            while True:
                validmove=human(cell_list,'X')
                ttprint(cell_list)
                game_end=judge(cell_list)
                if game_end:
                    break
                elif validmove:
                    print('Making move level "medium"')
                    robot_medium_AI(cell_list,'O')
                    ttprint(cell_list)
                    game_end=judge(cell_list)
                    if game_end:
                        break
                    else:
                        continue
                else:
                    continue
 # user with medium AI
        valid_move=True
        if cmds[1]=='medium' and cmds[2]=='user':
            while True:
                if valid_move:
                    robot_medium_AI(cell_list,'X')
                    print('Making move level "medium"')
                    ttprint(cell_list)
                    game_end=judge(cell_list)
                    if game_end:
                        break
                    else:
                        valid_move=human(cell_list,'O')
                        game_end=judge(cell_list)
                        ttprint(cell_list)
                        if game_end:
                            break
                else:
                    valid_move=human(cell_list,'O')
                    game_end=judge(cell_list)
                    ttprint(cell_list)
                    if game_end:
                        break

# user with hard AI
        if cmds[1]=='user' and cmds[2]=='hard':
            while True:
                validmove=human(cell_list,'X')
                ttprint(cell_list)
                game_end=judge(cell_list)
                if game_end:
                    break
                elif validmove:
                    print('Making move level "hard"')
                    make_bestMove(cell_list,'O')
                    ttprint(cell_list)
                    game_end=judge(cell_list)
                    if game_end:
                        break
                    else:
                        continue
                else:
                    continue

 # hard AI with user
        valid_move=True
        if cmds[1]=='hard' and cmds[2]=='user':
            while True:
                if valid_move:
                    make_bestMove(cell_list,'X')
                    print('Making move level "hard"')
                    ttprint(cell_list)
                    game_end=judge(cell_list)
                    if game_end:
                        break
                    else:
                        valid_move=human(cell_list,'O')
                        game_end=judge(cell_list)
                        ttprint(cell_list)
                        if game_end:
                            break
                else:
                    valid_move=human(cell_list,'O')
                    game_end=judge(cell_list)
                    ttprint(cell_list)
                    if game_end:
                        break

    else:
        print('Bad parameters!')
        continue







