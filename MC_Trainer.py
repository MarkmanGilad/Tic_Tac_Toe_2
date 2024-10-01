from TicTacToe import TicTacToe
from State import State
from Human_Agent import Human_Agent
from Random_Agent import Random_Agent
from AI_Agent import AI_Agent

PATH = 'Data/Q_MC_4.pth'

env = TicTacToe(State())
player1 = AI_Agent(1, env, graphics=None, Q_table_PATH=None)
player2 = Random_Agent(-1, env,graphics=None)

gamma = 0.9

def main ():
    player = player1    
    
    '''
    השלימו את הקוד המאמן את הסוכן לפי אלגוריתם מנטו קרלו

    חובה להשתמש בפונקציה 
    Generate_episode
    '''


    player.save_Q(PATH)
    print(test(100))

def Generate_episode (player, epoch):
    episods = []
    
    '''
    השלימו את הקוד היוצר רשימה של צעדים מתחילת משחק ועד לסיומו.

    מבנה הרשימה:
    episods = [(state, action, reward), (state, action, reward), ...]

    ניתן להשתמש בפונקציה אפסילון-גרידי מתוך הסוכן החכם, אותו עליכם לבנות.
    '''

    return episods

def test (num):
    x_win = 0
    o_win = 0
    tie = 0
    player = player1
    player.train=False
    player.load_Q(PATH)
    for n in range(num):
        player = player1
        state = State()
        while not env.end_of_game(state):
            action = player.get_action(state=state)
            state, _ = env.next_state(state,action)
            player = switch_players(player)
        if state.end_of_game == 1:
            x_win +=1
        elif state.end_of_game == -1:
            o_win += 1
        else:
            tie +=1
        state.reset()
        print(n, end = "\r")    
    return x_win, o_win, tie

def print_episodes (episode):
    for i, e in enumerate(episode):
        print(f'\n i= {i} player = {e[0].player} ')
        for i in e:
            print (i, end=" ")

def switch_players(player):
    if player == player1:
        return player2
    else:
        return player1

if __name__ == '__main__':
    main()
    # print(test(100))